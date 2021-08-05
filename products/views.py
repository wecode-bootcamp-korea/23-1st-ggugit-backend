from django.http import JsonResponse
from django.views import View

from products.models import Product, Type, Taste

class ProductView(View):
	def get(self, request):
		
		theme  = request.GET.get('theme',None) #type or taste
		number = request.GET.get('number',1)
		order  = request.GET.get('order',1)
		
		products = Product.objects.all()
		results = []
		
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
						}
		order_number = {
							1 : '-created_at',
							2 : '-sales',
							3 : '-price',
							4 : 'price',
							#5 : '-score'
						}
		if theme == 'taste':
			taste 	  = Taste.objects.get(name=filter_taste[int(number)])
			products = Product.objects.filter(producttaste__taste_id=taste.id)
		if theme == 'type':
			type 	  = Type.objects.get(name=filter_type[int(number)])
			products = Product.objects.filter(type=type)
						
		products = products.order_by(order_number[int(order)])
		for product in products:
				results.append({
					'id' 			: product.id,
					'name' 			: product.name,
					'image_url' 	: [image.image_url for image in product.image_set.all()],
					'cooking_time'  : product.cooking_time,
					'price' 		: product.price,
					'limited' 		: product.event_set.first().limited,
					'new' 			: product.event_set.first().new,
					'sales' 		: product.sales,
					'taste' 		: product.taste_set.first().name
                    })
	
		return JsonResponse({'results':results}, status=200)


class ProductDetailView(View):
    def get(self,request,product):

        product      = Product.objects.get(id = product)
        images       = product.image_set.all()
        descriptions = product.description_set.all()
        
        result=[{
                'name'         : product.name,
                'sub_name'     : product.sub_name,
                'price'        : product.price,
                'cooking_time' : product.cooking_time,
                'image'        :[product.image_url for product in images],
                'description'  :[{'description_image' : product.image_url for product in descriptions},
                                 {'text' : product.text for product in descriptions}],
				#'taste'		   : product.taste_set.get(product=product),
            }]
        return JsonResponse({'result':result}, status = 200)








        
