from django.urls import path
from . import views
from .views import question_list

urlpatterns = [
    path('', views.home, name='home'),
    path('questions/', views.question_list, name='question_list'),
]