import json

from django.http  import JsonResponse
from django.views import View

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

		cart, flag = Cart.objects.get_or_create(product=product, user=user, quantity=data['quantity'])
		if not flag:
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
					

