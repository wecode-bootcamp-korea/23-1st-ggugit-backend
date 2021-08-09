<<<<<<< HEAD
import json
=======
import json, jwt
>>>>>>> 59a0e54e37dc179adbb3e30755f8cc516210d1aa

from django.http  import JsonResponse
from django.views import View

<<<<<<< HEAD
from users.models    import User
from products.models import Product
from orders.models   import Cart
from users.utils     import LoginDecorator 

class CartView(View):
	@LoginDecorator
	def post(self,request):
		data = json.loads(request.body)
		user = request.user
		if not Product.objects.filter(id=data['product_id']).exists():
			return JsonResponse({'message' : 'NOT_FOUND'}, status=400)

		product = Product.objects.get(id=data['product_id'])

		cart, created = Cart.objects.get_or_create(product=product, user=user, quantity=data['quantity'])
		if not created:
		    cart.quantity += data['quantity']
		    cart.save()
		    return JsonResponse({'message':'ADD_SUCCESS'},status=200)
		return JsonResponse({'message' : 'SUCCESS'}, status=200)

	@LoginDecorator
	def get(self, request):
		user  = request.user
		carts = Cart.objects.filter(user=user)

		if not carts.exists():
			return JsonResponse({'message' : 'NO_CART'}, status=200)
		
		results=[{
		"name"     : cart.product.name,
		"price"    : round(cart.product.price),
		"discount" : round(int(cart.product.price) * 0.9) ,
		"quantity" : cart.quantity} for cart in carts]

		return JsonResponse({'results': results}, status=200)
					

=======
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
    
    
            
>>>>>>> 59a0e54e37dc179adbb3e30755f8cc516210d1aa
