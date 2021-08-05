<<<<<<< HEAD
<<<<<<< HEAD
from django.http import JsonResponse
from django.views import View
=======
from django.http  	 		import JsonResponse
from django.views  	 		import View
=======
from django.http            import JsonResponse
from django.views           import View
>>>>>>> f774d90 (Add: productdetail views작성4)
from django.core.exceptions import ObjectDoesNotExist
>>>>>>> c8a3d8e (Add: productdetail views2)

from products.models        import Product, Type, Taste

class ProductView(View):
<<<<<<< HEAD
	def get(self, request):
		
		theme  = request.GET.get('theme',None) #type or taste
		number = request.GET.get('number',1)
		order  = request.GET.get('order',1)
		try:

			products = Product.objects.all()

			filter_taste = {
				1 : '매콤한맛',
				2 : '짭짤한맛',
				3 : '새콤한맛',
				4 : '느끼한맛',
				5 : '담백한맛'
			}
			filter_type = {
				1 : '한식',
				2 : '중식',
				3 : '일식',
				4 : '양식',
				5 : '기타'
=======
    def get(self, request):
        theme  = request.GET.get('theme', None) #type or taste
        number = request.GET.get('number',1)
        order  = request.GET.get('order',1)
        try:
            products = Product.objects.all()
            filter_taste = {
                1 : '매콤한맛',
                2 : '짭짤한맛',
                3 : '새콤한맛',
                4 : '느끼한맛',
                5 : '담백한맛'
            }
            filter_type = {
                1 : '한식',
                2 : '중식',
                3 : '일식',
                4 : '양식',
                5 : '기타'
<<<<<<< HEAD
>>>>>>> 38403f9 (Add: productdetail views작성3)
			}
=======
            }
>>>>>>> f53abbd (Add: productdetail views작성4)
            order_number = {
                1 : '-created_at',
                2 : '-sales',
                3 : '-price',
                4 : 'price',
<<<<<<< HEAD
			}
<<<<<<< HEAD
			if theme == 'taste':
				taste 	  = Taste.objects.get(name=filter_taste[int(number)])
				products = Product.objects.filter(producttaste__taste_id=taste.id)
			if theme == 'type':
				type 	  = Type.objects.get(name=filter_type[int(number)])
				products = Product.objects.filter(type=type)

			products = products.order_by(order_number[int(order)])
			results = [{
				'id' 		   : product.id,
				'name' 		   : product.name,
				'image_url'    : [image.image_url for image in product.image_set.all()],
				'cooking_time' : product.cooking_time,
				'price' 	   : product.price,
				'limited' 	   : product.event_set.first().limited,
				'new' 		   : product.event_set.first().new,
				'sales' 	   : product.sales,
				'taste' 	   : product.taste_set.first().name} for product in products]
		except KeyError:
			return JsonResponse({'message':'KEY_ERROR'}, status = 400)
		return JsonResponse({'results':results}, status=200)










        
=======
=======
            }
>>>>>>> f774d90 (Add: productdetail views작성4)
            if theme == 'taste':
                taste    = Taste.objects.get(name=filter_taste[int(number)])
                products = Product.objects.filter(producttaste__taste_id=taste.id)
            if theme == 'type':
                type     = Type.objects.get(name=filter_type[int(number)])
                products = Product.objects.filter(type=type)
            products = products.order_by(order_number[int(order)])
            results = [{
                'id'           : product.id,
                'name'         : product.name,
                'image_url'    : [image.image_url for image in product.image_set.all()],
                'cooking_time' : product.cooking_time,
                'price'        : product.price,
                'limited'      : product.event_set.first().limited,
                'new'          : product.event_set.first().new,
                'sales'        : product.sales,
                'taste'        : product.taste_set.first().name} for product in products]
        except ObjectDoesNotExist:
            return JsonResponse({'message':'NOT_FOUND'}, status = 404)
        return JsonResponse({'results':results}, status=200)

class ProductDetailView(View):
    def get(self, request, product):
        if Product.objects.filter(id=product).exists():
<<<<<<< HEAD
            product      = Product.objects.get(id=product)
            images       = product.image_set.all()
            descriptions = product.description_set.all()
            tastes       = product.taste_set.all()
    
            results = [{
                'name'		   : product.name,
                'sub_name'	   : product.sub_name,
                'price'		   : round(product.price),
                'discount'     : round(int(product.price)* 0.9),
                'cooking_time' : product.cooking_time,
                'image'		   : [product.image_url for product in images],
                'description'  :[{'description_image': product.image_url for product in descriptions},
                               	 {'description_text': product.text for product in descriptions}],
                'taste' 	   : [product.name for product in tastes],
            }]
            return JsonResponse({'result':results}, status=200)
        return JsonResponse({'message':'KEY_ERROR'}, status=400)
>>>>>>> c8a3d8e (Add: productdetail views2)
=======
            return JsonResponse({'message':'NOT_FOUND'}, status=404)
        product      = Product.objects.get(id=product)
        images       = product.image_set.all()
        descriptions = product.description_set.all()
        tastes       = product.taste_set.all()

        results = [{
            'name'         : product.name,
            'sub_name'     : product.sub_name,
            'price'        : round(product.price),
            'discount'     : round(int(product.price)* 0.9),
            'cooking_time' : product.cooking_time,
            'image'        : [product.image_url for product in images],
            'description'  :[{'description_image': product.image_url for product in descriptions},
                             {'description_text': product.text for product in descriptions}],
            'taste'        : [product.name for product in tastes],
        }]
        return JsonResponse({'result':results}, status=200)
        
>>>>>>> f774d90 (Add: productdetail views작성4)
