from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ObjectDoesNotExist

from products.models        import Product, Type, Taste

class ProductView(View):
    def get(self, request):
        theme  = request.GET.get('theme', None) #type or taste
        number = request.GET.get('number',1)
        order  = request.GET.get('order',1)
        main = request.GET.get('main', None)
        try:
            products = Product.objects.all()

            filter_taste = {taste.id : taste.name for taste in Taste.objects.all()}
            
            filter_type = {type.id : type.name for type in Type.objects.all()}
            
            order_number = {
                1 : '-created_at',
                2 : '-sales',
                3 : '-price',
                4 : 'price',
            }
            if theme == 'taste':
                taste    = Taste.objects.get(name=filter_taste[int(number)])
                products = Product.objects.filter(producttaste__taste=taste)
            if theme == 'type':
                type     = Type.objects.get(name=filter_type[int(number)])
                products = Product.objects.filter(type=type)
            if main :
                tastes = Taste.objects.all()
                return JsonResponse({'results':[{'id': taste.id, 'taste' : taste.name }for taste in tastes] })

            products = products.order_by(order_number[int(order)])
            results = [{
                'id'           : product.id,
                'name'         : product.name,
                'image_url'    : [image.image_url for image in product.image_set.all()],
                'cooking_time' : product.cooking_time,
                'price'        : round(product.price),
                'discount'     : round(int(product.price)*0.9),
                'limited'      : product.event_set.get().limited,
                'new'          : product.event_set.get().new,
                'sales'        : product.sales,
                'taste'        : product.taste_set.get().name,
                'stock'        : product.stock} for product in products]
        except ObjectDoesNotExist:
            return JsonResponse({'message':'NOT_FOUND'}, status = 404)
        return JsonResponse({'results':results}, status=200)

class ProductDetailView(View):
    def get(self, request, product_id):
        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({'message':'NOT_FOUND'}, status=404)
        
        product      = Product.objects.get(id=product_id)
        images       = product.image_set.all()
        descriptions = product.description_set.get()
        tastes       = product.taste_set.get()

        results = [{
            'id'          : product.id,
            'name'        : product.name,
            'sub_name'    : product.sub_name,
            'price'       : round(product.price),
            'discount'    : round(int(product.price)* 0.9),
            'cooking_time': product.cooking_time,
            'image_url'       : [product.image_url for product in images],
            'description_image': {'description_image1' : descriptions.image_url_1,
                                    'description_image2' : descriptions.image_url_2,
                                    'description_image3' : descriptions.image_url_3},
            'description_text' :  descriptions.text,
            'taste'        : tastes.name,
            'stock'        : product.stock
        }]

        return JsonResponse({'results':results}, status=200)
        
