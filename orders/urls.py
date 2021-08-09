from django.urls import path

from orders.views import CartView

urlpatterns = [
    path('/cart', CartView.as_view()),
    path('/<int:cart_id>',CartView.as_view()),
]