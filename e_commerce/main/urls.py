from django.urls import path
from . import views
urlpatterns = [
   path('home/', views.home),
   path('shop/',views.shop),
   path('shop_details/',views.shop_details),
   path('shop_cart/',views.shop_cart)
]
