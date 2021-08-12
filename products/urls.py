from django.urls import path

from products.views import MainView, ProductView, ProductDetailView, SearchView

urlpatterns = [
    path('/main', MainView.as_view()),
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/search', SearchView.as_view())
]