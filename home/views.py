from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactForm, ContactFormMessage, UserProfile, UserProfileForm
from django.core.mail import send_mail, BadHeaderError
from products.models import Product, Category
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from home.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, PasswordChangingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm


# Create your views here.

# /home
def index(request):
    
    reklamData = Product.objects.all()
    categoryData = Category.objects.all()
    context = {
        
        'categoryData': categoryData,
        'page': 'home',
        'reklamData': reklamData
    }

    return render(request, 'index.html', context)


def aboutUs(request):
    
    context = {
        
        'page': 'about'
    }

    return render(request, 'about.html', context)


def categoryProducts(request, id, slug):
    categoryData = Category.objects.all()
    productsFilter = Product.objects.filter(category_id=id)
    context = {
        'categoryData': categoryData,
        'productsFilter': productsFilter,
        'slug': slug,
        'page': 'products'
    }

    return render(request, 'all-items.html', context)


def allProducts(request):
    categoryData = Category.objects.all()
    reklamData = Product.objects.all()
    context = {
        'categoryData': categoryData,
        'reklamData': reklamData,
    }

    return render(request, 'all-items.html', context)


def productDetail(request, id, slug):
    categoryData = Category.objects.all()
    productData = Product.objects.get(pk=id)
    context = {
        'categoryData': categoryData,
        'productData': productData,
    }

    return render(request, 'product-detail.html', context)


def contactUs(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.contact_firstName = form.cleaned_data['contact_firstName']
            data.contact_lastName = form.cleaned_data['contact_lastName']
            data.contact_email = form.cleaned_data['contact_email']
            data.contact_subject = form.cleaned_data['contact_subject']
            data.contact_message = form.cleaned_data['contact_message']
            data.save()
            messages.success(request, "İletişim formunuz başarıyla gönderilmiştir.")
            return HttpResponseRedirect('/contact')

    
    form = ContactForm()
    context = {
        'form': form
    }

    return render(request, 'contact.html')


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

        else:
            messages.warning(request, "Hatalı kullanıcı adı ya da şifre!")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category, }

    return render(request, 'login.html', context)


def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            #data.image="images/users/user.png"
            data.save()
            messages.success(request, 'Üye kaydınız başarılı!')
            return HttpResponseRedirect("/")

        else:
            messages.warning(request, 'Bilgilerinizde hata var!')
            return HttpResponseRedirect('/signup/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form, }

    return render(request, 'customer-register.html', context)


def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')


def customerAccount(request):
    current_user = request.user  # access user session info
    profileData = UserProfile.objects.get(user_id = current_user)

    context = {
        'profileData': profileData
    }

    return render(request, 'customer-account.html', context)

@login_required(login_url="/login")
def userUpdate(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, 'Profil bilgileriniz güncellendi!')
            return HttpResponseRedirect('/customer-account')
        
        else:
            context = {
            'userForm':userForm,
            'profileForm':profileForm
            }
            messages.warning(request,'Bilgilerinizde hata var!')
            
            return render(request, 'customer-account.html', context)

    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'userForm':userForm,
            'profileForm':profileForm
        }
        return render(request, 'customer-account.html', context)

    
@login_required(login_url="/login")
def userPasswordUpdate(request):
    if request.method == 'POST':
        form_password = PasswordChangeForm(request.user, request.POST)
        if form_password.is_valid():
            user_password2 = form_password.save()
            update_session_auth_hash(request, user_password2)
            messages.success(request, 'Şifreniz Başarıyla Değiştirildi')
            return HttpResponseRedirect('/customer-account')
        else:
            
            messages.warning(request,'Şifreniz Değiştirilemedi!')
                
            return render(request, 'customer-account.html')
        
    else:
        form_password = PasswordChangeForm(request.user)
        return render(request, 'customer-account.html', {'form':'form'})
    

def testView(request):
    return render(request, 'deneme.html')