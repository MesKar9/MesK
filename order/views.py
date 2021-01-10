from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactForm, ContactFormMessage, UserProfile, UserProfileForm, UserProfile
from django.core.mail import send_mail, BadHeaderError
from products.models import Product, Category
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from home.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from order.models import CustomerBasket, CustomerBasketForm, Order, OrderForm, OrderProduct
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'shop-basket.html')


@login_required(login_url='/login')
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    productControl = CustomerBasket.objects.filter(product_id = id)
    productBskt = Product.objects.get(pk=id)
    if productControl:
        basketControl = 1 #sepette aynı üründen var
    else:
        basketControl = 0 #sepette aynı üründen yok

    if request.method == 'POST':
        form = CustomerBasketForm(request.POST)
        if form.is_valid():
            if basketControl == 1:
                data = CustomerBasket.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
                
            
            else:
                data = CustomerBasket()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
                
        request.session['cart_items'] = CustomerBasket.objects.filter(user_id=current_user.id).count()
        messages.success(request, "Ürün sepete eklendi!")
        return HttpResponseRedirect(url)
        
        
    context = {
        'productControl':productControl,
        'productBskt':productBskt
    }

    messages.warning(request, "Ürün sepete eklenemedi!")
    return HttpResponseRedirect(url)

@login_required(login_url="/login")
def basket(request):
    category = Category.objects.all()
    current_user = request.user
    basket = CustomerBasket.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = CustomerBasket.objects.filter(user_id=current_user.id).count()
    total = 0
    for rs in basket:
        total += rs.product.price * rs.quantity

    
    context = {
        'basket':basket,
        'category':category,
        'total':total
    }

    return render(request, 'shop-basket.html', context)





@login_required(login_url='/login')
def deletefrombasket(request,id):
    CustomerBasket.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = CustomerBasket.objects.filter(user_id=current_user.id).count()
    messages.success(request, "Ürün sepetinizden çıkarıldı!")
    return HttpResponseRedirect("/basket")



@login_required(login_url='/login')
def productOrder(request):
    category = Category.objects.all()
    current_user = request.user
    basket = CustomerBasket.objects.filter(user_id = current_user.id)
    total = 0
    for rs in basket:
        total += rs.product.price * rs.quantity
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()


            basket = CustomerBasket.objects.filter(user_id=current_user.id)
            for rs in basket:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity

                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()

                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()
            
            CustomerBasket.objects.filter(user_id = current_user.id).delete()
            request.session['cart_items']=0
            messages.success(request, "Sipariş tamamlandı!")
            return render(request, 'shop-basket.html',{'ordercode':ordercode,'category':category})
        
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct")
    
    form = OrderForm()
    profile = UserProfile.objects.get(user_id = current_user.id)
    context = {
        'basket':basket,
        'total':total,
        'form':form,
        'profile':profile
    }

    return render(request, 'shop-checkout1.html', context)