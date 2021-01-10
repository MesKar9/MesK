from django.urls import path
from . import views

urlpatterns = [
    # /home/
    path('', views.index, name='index')
    # /home/5/
    # path('<int:question_id>', views.detail, name'detail')
    # /home/5/results/
    # path('<int:question_id>/results/', views.results, name='results')

]
