from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=250)
    image= models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class Man(models.Model):
    name1=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    des=models.TextField()

    def __str__(self):
        return self.name1

# Create your models here.
