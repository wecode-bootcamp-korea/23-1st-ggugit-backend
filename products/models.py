from django.db import models

class Product(models.Model):
    name          = models.CharField(max_length=50)
    sub_name      = models.CharField(max_length=100)
    cooking_time  = models.PositiveSmallIntegerField()
    price         = models.DecimalField(max_digits=12 ,decimal_places=2)
    type          = models.ForeignKey('Type', on_delete=models.CASCADE)
    sales         = models.PositiveIntegerField()
    stock         = models.PositiveIntegerField()
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

    class Meta:
        db_table = 'tastes'

    def __str__(self):
        return self.name

class ProductTaste(models.Model):
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    taste   = models.ForeignKey('Taste', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_tastes'


class Image(models.Model):
    image_url = models.URLField()
    product   = models.ForeignKey('Product',on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Description(models.Model):
    image_url  = models.URLField()
    text       = models.TextField(max_length=1000)
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'descriptions'

class Event(models.Model):
    limited = models.BooleanField(default=False)
    new     = models.BooleanField(default=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'events'

class MainPage(models.Model):
    image_url = models.URLField()

    class Meta:
        db_table = 'main_pages'