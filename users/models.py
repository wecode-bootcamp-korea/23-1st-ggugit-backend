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
    
