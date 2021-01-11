from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from products.models import Product


class CustomerBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.title

    @property
    def amount(self):
        return self.quantity * self.product.price
    
    @property
    def price(self):
        return self.product.price
    

class CustomerBasketForm(ModelForm):
    class Meta:
        model = CustomerBasket
        fields = [
            'quantity'
        ]


class Order(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Accepted', 'Onaylandı'),
        ('Preaparing', 'Hazırlanıyor'),
        ('OnShipping', 'Kargoda'),
        ('Completed', 'Tamamlandı'),
        ('Cancelled', 'İptal Edildi'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5,editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=20)
    total = models.FloatField()
    status = models.CharField(max_length=20,choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminNote = models.CharField(max_length=100, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
    

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'phone',
            'address',
            'city'
        ]


class OrderProduct(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Accepted', 'Onaylandı'),
        ('Cancelled', 'İptal Edildi'),
    )

    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title