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
<<<<<<< HEAD

=======
=======
    @LoginDecorator
    def post(self,request):
        data     = json.loads(request.body)
        user     = request.user
        quantity = data['quantity']
        if not Product.objects.filter(id=data['product_id']).exists():
            return JsonResponse({'message' : 'NOT_FOUND'}, status=400)

        product = Product.objects.get(id=data['product_id'])

        if product.stock < quantity:
            return JsonResponse({'message':'NO_STOCK'}, status=400)

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
<<<<<<< HEAD
        "name"      : cart.product.name,
        "price"     : round(cart.product.price),
        "discount"  : round(int(cart.product.price) * 0.9),
        "image_url" : [image.image_url for image in cart.product.image_set.all()],
        "quantity"  : cart.quantity} for cart in carts]
>>>>>>> f64812b (Add: 장바구니 이미지 추가)
=======
        "cart_id"    : cart.id,
        "product_id" : cart.product.id,
        "name"       : cart.product.name,
        "price"      : round(cart.product.price),
        "discount"   : round(int(cart.product.price) * 0.9),
        "image_url"  : cart.product.image_set.get().image_url,
        "quantity"   : cart.quantity} for cart in carts]
>>>>>>> 468fa89 (Add: 장바구니 이미지 추가 및 id 추가)

<<<<<<< HEAD
>>>>>>> fbef7ea (Add: 장바구니 이미지 추가 및 id 추가)
		return JsonResponse({'results': results}, status=200)
					

=======
from users.utils  import LoginDecorator
from .models      import User, Product, Cart

<<<<<<< HEAD

class CartView(View):
    @LoginDecorator
    def delete(self,request,cart_id):
=======
	@LoginDecorator
<<<<<<< HEAD
=======
<<<<<<< HEAD
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
>>>>>>> 391dd2f (장바구니 patch 추가)
=======
>>>>>>> 1475178 (장바구니 patch 수정)
	def delete(self,request,cart_id):
>>>>>>> 0cb7524 (모델링 수정 (description_image 칼럼 추가),)
        
		if not Cart.objects.filter(id = cart_id).exists():
			return JsonResponse({'message': 'NOT_FOUND'}, status = 404)

		if Cart.objects.get(id=cart_id).user_id != request.user.id:
			return JsonResponse({'message':'INVALED_USER'}, status=403)

<<<<<<< HEAD
        if Cart.objects.get(id = cart_id).delete():
            return JsonResponse({'message': 'SUCCESS'}, status = 200)
    
    
            
<<<<<<< HEAD
>>>>>>> 59a0e54e37dc179adbb3e30755f8cc516210d1aa
=======
>>>>>>> 9ce9051810cfc45e4a75a6114dfe7e3a1d419b5e
=======
		if Cart.objects.get(id = cart_id).delete():
			return JsonResponse({'message': 'SUCCESS'}, status = 200)        
>>>>>>> 0cb7524 (모델링 수정 (description_image 칼럼 추가),)
>>>>>>> a6fc452 (모델링 수정 (description_image 칼럼 추가),)
