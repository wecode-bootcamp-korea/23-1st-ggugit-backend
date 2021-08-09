import json, jwt

from django.http  import JsonResponse
from django.views import View

from users.utils  import LoginDecorator
from .models      import User, Product, Cart


class CartView(View):
    @LoginDecorator
    def delete(self,request,cart_id):
        
        if not Cart.objects.filter(id = cart_id).exists():
            return JsonResponse({'message': 'NOT_FOUND'}, status = 404)

        if Cart.objects.get(id=cart_id).user_id != request.user.id:
            return JsonResponse({'message':'INVALED_USER'}, status=403)

        if Cart.objects.get(id = cart_id).delete():
            return JsonResponse({'message': 'SUCCESS'}, status = 200)
    
    
            
