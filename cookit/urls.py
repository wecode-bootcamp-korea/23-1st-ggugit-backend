"""cookit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

urlpatterns = [
    path('users', include('users.urls')),
<<<<<<< HEAD
    path('products', include('products.urls')),
<<<<<<< HEAD
=======
>>>>>>> a7cceedbbb27dea648dc0c2368dd33366330582d
=======
<<<<<<< HEAD
    path('orders', include('orders.urls'))
>>>>>>> f0f0025 (Add : 장바구니 기능 추가, (CREATE, READ))
=======
    path('orders', include('orders.urls')),
>>>>>>> eff5d33 (Add: 장바구니 삭제)
>>>>>>> 59a0e54e37dc179adbb3e30755f8cc516210d1aa
]
