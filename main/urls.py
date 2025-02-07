from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # URL для страницы с деталями товара
    path('about/', views.about, name='about'),
]
