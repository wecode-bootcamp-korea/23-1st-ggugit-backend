from django.db       import models

from users.models    import User
from products.models import Product
    

class Review(models.Model):
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    product   = models.ForeignKey(Product,on_delete=models.CASCADE)
    text      = models.TextField()
    score     = models.DecimalField(max_digits=2,decimal_places=1)
    create_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField()

    class Meta:
        db_table = 'reviews'

class Order(models.Model):
    user         = models.ForeignKey(User,on_delete=models.CASCADE)
    address      = models.CharField(max_length=200)
    order_status = models.ForeignKey('OrderStatus',on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderItem(models.Model):
    order             = models.ForeignKey('Order',on_delete=models.CASCADE)
    product           = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity          = models.PositiveIntegerField()
    order_item_status = models.ForeignKey('OrderItemStatus',on_delete=models.CASCADE)

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

class Cart(models.Model):
    quantity = models.PositiveIntegerField()
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    user     = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'carts'