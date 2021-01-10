from django.urls import path
from . import views
from django.contrib import admin

# from .views import contactView, successView


urlpatterns = [
    # /home/
    path('', views.index, name='index'),
    path('update', views.userUpdate, name='userUpdate'),
    path('password', views.userPasswordUpdate, name='userPasswordUpdate'),
    # path('contact/', views.contactView, name='contact'),
    # path('success/', views.successView, name='success'),

    # /home/5/
    # path('<int:question_id>', views.detail, name'detail')
    # /home/5/results/
    # path('<int:question_id>/results/', views.results, name='results')

]