from django.db import models
from datetime import datetime
# Create your models here.



class PhoneModel(models.Model):
    name = models.CharField(max_length=300,default='')
    operation_system = models.CharField(max_length=200,default='')
    price = models.IntegerField(default=0)
    cameras = models.CharField(max_length=100,default=1)
    created_at = models.DateTimeField(default=datetime.now)
    desc = models.TextField(default='Samsung or Iphone ?')


    class Meta:
        db_table = 'PhoneModel'
    def __str__(self) -> str:
        return self.name