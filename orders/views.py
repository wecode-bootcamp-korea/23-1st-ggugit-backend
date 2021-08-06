import json

from django.http  import JsonResponse
from django.views import View

from users.models	   import User
from products.models import Product
from orders.models   import Cart
from users.utils 	   import LoginDecorator 

class CartView(View):
	@LoginDecorator
	def post(self,request):
		data = json.loads(request.body)
		user = request.user
		if not Product.objects.filter(id=data['product_id']).exists():
			return JsonResponse({'message' : 'NOT_FOUND'}, status=400)

		product = Product.objects.get(id=data['product_id'])

		if Cart.objects.filter(product=product).exists():
			cart = Cart.objects.get(product=product)
			cart.quantity += data['quantity']
			cart.save()
			return JsonResponse({'message':'ADD_SUCCESS'},status=200)
		
		Cart.objects.create( 
			user_id    = user.id,
			product_id = product.id,
			quantity   = data['quantity']
			)
		return JsonResponse({'message' : 'SUCCESS'}, status=200)

	@LoginDecorator
	def get(self, request):
		user = request.user
		results = []
		carts = Cart.objects.filter(user=user)

		if not carts.exists():
			return JsonResponse({'results' : []}, status=200)

		for cart in carts:
			product = Product.objects.get(id=cart.product_id)
			results.append({
				"product_name" : product.name,
				"price" : round(product.price),
				"discount" : round(int(product.price) * 0.9) ,
				"quantity" : cart.quantity
				})

		return JsonResponse({'results': results}, status=200)
					

