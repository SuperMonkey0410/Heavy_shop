from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.index, name='search'),
    path('catalog/<slug:category_slug>', views.index, name='product_catalog'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),

]
