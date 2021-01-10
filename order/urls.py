from django.urls import path
from . import views
from django.contrib import admin

# from .views import contactView, successView


urlpatterns = [
    # /home/
    path('', views.index, name='index'),
    path('addtocart/<int:id>', views.addtocart, name="addtocart"),
    path('deletefrombasket/<int:id>', views.deletefrombasket, name="deletefrombasket"),
    path('productorder/', views.productOrder, name="productOrder")
]