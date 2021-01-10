"""ticaretSitem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home import views
from order import views as OrderViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls'), name='home'),
    path('about/', views.aboutUs, name='about'),
    path('contact/', views.contactUs, name='contact'),
    path('products/', include('products.urls')),
    path('allproducts/', views.allProducts, name='allProducts'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.categoryProducts, name='categoryProducts'),
    path('products/<int:id>/<slug:slug>/', views.productDetail, name='productDetail'),
    path('signup/', views.signupView, name='signupView'),
    path('logout/', views.logoutView, name='logoutView'),
    path('login/', views.loginView, name='loginView'),
    path('customer-account/', views.customerAccount, name='customerAccount'),
    path('order/', include('order.urls')),
    path('deneme/', views.testView, name='testView'),
    path('basket/', OrderViews.basket, name="basket"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


