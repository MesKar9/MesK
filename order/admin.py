from django.contrib import admin
from order.models import CustomerBasket, Order, OrderForm, OrderProduct

class CustomerBasketAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product',
        'price',
        'quantity',
        'amount'
    ]

    list_filter = [
        'user'
    ]


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user','product','price','quantity','amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','city','total','status']
    list_filter = ['status']
    readonly_fields = ('user','first_name','last_name','phone','address','city','phone','ip','total')
    can_delete = False
    inlines = [OrderProductline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user','product','price','quantity','amount']
    list_filter = ['user']


admin.site.register(CustomerBasket, CustomerBasketAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)