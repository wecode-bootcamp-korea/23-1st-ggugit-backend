from django.http             import JsonResponse
from django.views            import View
from django.core.exceptions import ObjectDoesNotExist

from products.models        import Product, Type, Taste, MainPage

class MainView(View):
    def get(self, request):
        main_pages   = MainPage.objects.all()
        first_pages  = main_pages.order_by('id')[:6]
        second_pages = main_pages.order_by('id')[6:12]

        first_banner  = [first_page.image_url for first_page in first_pages]
        second_banner = [second_page.image_url for second_page in second_pages]

        return JsonResponse({'first_banner':first_banner, 'second_banner':second_banner}, status=200)

class ProductView(View):
    def get(self, request):
        theme  = request.GET.get('theme', None) #type or taste
        number = request.GET.get('number',1)
        order  = request.GET.get('order',1)
        main   = request.GET.get('main', None)
        search = request.GET.get('KeyWord', None)

        try:
            products = Product.objects.all()      
            
            order_number = {
                1 : '-created_at',
                2 : '-sales',
                3 : '-price',
                4 : 'price',
                5 : '-stock',
            }

            if theme == 'taste':
                filter_taste = {taste.id : taste.name for taste in Taste.objects.all()}
                taste        = Taste.objects.get(name = filter_taste[int(number)])
                products     = Product.objects.filter(producttaste__taste = taste)
            
            if theme == 'country':
                filter_type = {type.id : type.name for type in Type.objects.all()}
                country     = Type.objects.get(name = filter_type[int(number)])
                products    = Product.objects.filter(type = country)
            
            if main:
                tastes = Taste.objects.all()
                return JsonResponse({'results':[{'id': taste.id, 'taste' : taste.name} for taste in tastes]})
            
            if search:
                products = Product.objects.filter(name__icontains = search)

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
            return JsonResponse({'message':'NOT_FOUND'}, status=404)
        except KeyError :
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        return JsonResponse({'results':results}, status=200)

class ProductDetailView(View):
    def get(self, request, product_id):
        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({'message':'NOT_FOUND'}, status=404)
        
        product = Product.objects.get(id=product_id)
        images  = product.image_set.all()
        taste   = product.taste_set.get()

        results = [{
            'id'                : product.id,
            'name'              : product.name,
            'sub_name'          : product.sub_name,
            'price'             : round(product.price),
            'discount'          : round(int(product.price)* 0.9),
            'cooking_time'      : product.cooking_time,
            'image_url'         : [product.image_url for product in images],
            'taste'             : taste.name,
            'stock'             : product.stock,
            'description_text'  : product.description.text,
            'description_images': {
                'first_image' : product.description.image_url_1,
                'second_image': product.description.image_url_2,
                'third_image' : product.description.image_url_3
                },
        }]
        return JsonResponse({'results':results}, status=200)