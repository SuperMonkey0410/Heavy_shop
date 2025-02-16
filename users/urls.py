from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('users-cart/', users_cart, name='users_cart'),
    path('logout/', logout, name='logout'),
]
