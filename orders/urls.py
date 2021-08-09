from django.urls import path

from orders.views import CartView

urlpatterns = [
<<<<<<< HEAD
    path('/cart', CartView.as_view()),
=======
    path('/<int:cart_id>',CartView.as_view()),
>>>>>>> 59a0e54e37dc179adbb3e30755f8cc516210d1aa
]