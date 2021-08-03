from django.db import models

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

class Cart(models.Model):
    quantity = models.PositiveIntegerField()
    product  = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product')
    user     = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user')

    class Meta:
        db_table = 'carts'