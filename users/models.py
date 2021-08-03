from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=45)
    email        = models.CharField(max_length=200)
    password     = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=45)
    birthday     = models.DateField()
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        
    def __str__(self):
    		return self.name
    
class Review(models.Model):
    user      = models.ForeignKey('User',on_delete=models.CASCADE, related_name='user')
    product   = models.ForeignKey('Product',on_delete=models.CASCADE, related_name='product')
    text      = models.TextField()
    score     = models.DecimalField(max_digits=2,decimal_places=1)
    create_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField()

    class Meta:
        db_table = 'reviews'

class Order(models.Model):
    user         = models.ForeignKey('User',on_delete=models.CASCADE, related_name='user')
    address      = models.CharField(max_length=200)
    order_status = models.ForeignKey('OrderStatus',on_delete=models.CASCADE, related_name='orderstatus')

    class Meta:
        db_table = 'orders'

class OrderItem(models.Model):
    order             = models.ForeignKey('Order',on_delete=models.CASCADE, related_name='order')
    product           = models.ForeignKey('Product',on_delete=models.CASCADE, related_name='product')
    quantity          = models.PositiveIntegerField()
    order_item_status = models.ForeignKey('OrderItemStatus',on_delete=models.CASCADE, related_name='orderitemstatus')

    class Meta:
        db_table = 'order_items'

class OrderStatus(models.Model):
    order_status = models.CharField(max_length=45)

    class Meta:
        db_table ='order_status'

class OrderItemStatus(models.Model):
    status = models.CharField(max_length=45)

    class Meta:
        db_table = 'order_item_status'


class Product(models.Model):
	name 		  = models.CharField(max_length=50)
	cooking_time  = models.PositiveSmallIntegerField()
	price 		  = models.DecimalField(decimal_places=2)
	type 		  = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='type')
	sales 		  = models.PositiveIntegerField()
	stock 		  = models.PositiveIntegerField()
	created_at    = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'products'

	def __str__(self):
		return self.name

class Type(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		db_table = 'types'


class Taste(models.Model):
	name    = models.CharField(max_length=30)
	product = models.ManytToManyField('Product', related_name='taste')

	class Meta:
		db_table = 'tastes'

	def __str__(self):
		return self.name

class Image(models.Model):
	image_url = models.URLField()
	product   = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='image')

	class Meta:
		db_table = 'images'

class Description(models.Model):
	image_url  = models.URLField()
	text 	   = models.TextField(max_length=1000)
	product    = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='description')

	class Meta:
		db_table = 'descriptions'

class Event(models.Model):
	limited  = models.BooleanField(default=False)
	new 	 = models.BooleanField(default=False)
	product  = models.ForeignKey('Product', on_delete=models.CASCADE)

	class Meta:
		db_table = 'events'

class MainPage(models.Model):
	image_url = models.URLField()

	class Meta:
		db_table = 'main_pages'

class Cart(models.Model):
	quantity 	 = models.PositiveIntegerField()
	product 	 = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product')
	user 		 = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user')

	class Meta:
		db_table = 'carts'
