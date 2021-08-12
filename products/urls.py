from django.urls import path

from products.views import ProductView

urlpatterns = [
    path('', ProductView.as_view()),
<<<<<<< HEAD
    
=======
<<<<<<< HEAD
<<<<<<< HEAD
    
=======
    path('/<int:product>', ProductDetailView.as_view())
>>>>>>> c1b7b8f (Add: productdetail views)
=======
    path('/<int:product_id>', ProductDetailView.as_view())
>>>>>>> 2e13ceb (상품목록 : 쿼리 파라미터 main 추가 , 하드코딩 수정)
>>>>>>> d4b4c81 (상품목록 : 쿼리 파라미터 main 추가 , 하드코딩 수정)
]