from django.db import models

# Create your models here.

from django.db import models
from django.db.models.fields import return_None

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='products')

    class Meta:
        db_table = 'products'
    def __str__(self):
        return self.name