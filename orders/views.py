import json, jwt

from django.http  import JsonResponse
from django.views import View

from users.utils  import LoginDecorator
from .models      import User, Product, Cart


class CartView(View):
	@LoginDecorator
	def post(self,request):
		data     = json.loads(request.body)
		user     = request.user
		quantity = data['quantity']

		if not Product.objects.filter(id=data['product_id']).exists():
			return JsonResponse({'message' : 'NOT_FOUND'}, status=400)

		product = Product.objects.get(id=data['product_id'])

		if product.stock < quantity:
			return JsonResponse({'message':'no_stock'}, status=400)

		cart, created = Cart.objects.get_or_create(product=product, user=user, defaults = {'quantity' : quantity})
		if not created:
			if product.stock < quantity + cart.quantity:
				return JsonResponse({'message':'no_stock'}, status=400)
			cart.quantity += data['quantity']
			cart.save()
			return JsonResponse({'message':'ADD_SUCCESS'},status=200)
		return JsonResponse({'message' : 'SUCCESS'}, status=200)

	@LoginDecorator
	def get(self, request):
		user  = request.user
		carts = Cart.objects.filter(user=user)

		if not carts.exists():
			return JsonResponse({'message' : 'NO_CART'}, status=400)
		
		results=[{
		"name"     : cart.product.name,
		"price"    : round(cart.product.price),
		"discount" : round(int(cart.product.price) * 0.9) ,
		"quantity" : cart.quantity} for cart in carts]

		return JsonResponse({'results': results}, status=200)

	@LoginDecorator
	def patch(self,request,cart_id):
		data   = json.loads(request.body)
		user   = request.user
		stocks = Product.objects.get(id = data['product_id']).stock
		cart   = Cart.objects.get(id=cart_id)
		if stocks < cart.quantity + data['quantity']:
			return JsonResponse({'message':'OUT_OF_STOCK'},status = 400)
		if cart.user_id != user.id:
			return JsonResponse({'message':'INVALED_USER'}, status=403)
		cart.quantity += data['quantity']
		cart.save()
		return JsonResponse({'message':'SUCCESS'}, status = 201)

	@LoginDecorator
	def delete(self,request,cart_id):
        
		if not Cart.objects.filter(id = cart_id).exists():
			return JsonResponse({'message': 'NOT_FOUND'}, status = 404)

		if Cart.objects.get(id=cart_id).user_id != request.user.id:
			return JsonResponse({'message':'INVALED_USER'}, status=403)

		if Cart.objects.get(id = cart_id).delete():
			return JsonResponse({'message': 'SUCCESS'}, status = 200)        
