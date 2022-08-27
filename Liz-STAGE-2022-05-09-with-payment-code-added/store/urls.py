from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name="store"),
    path('cart/',views.cart, name="cart"),
    path('favorites/',views.favorites, name="favorites"),
    path('checkout/',views.checkout, name="checkout"),
    path('orderplaced/',views.orderplaced, name="orderplaced"),
    path('history/',views.history, name="history"), 
    
    path('update_item/',views.updateItem, name="update_item"),
    path('update_item1/',views.updateItem1, name="update_item1"),
]