from django.urls import path
from . import views

urlpatterns = [
    path('home_page/', views.home_page, name='home_page'),
    path('page/', views.page, name='page'),
    path('login/', views.login, name='login'),
]