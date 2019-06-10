from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    phone=models.IntegerField()


    def __str__(self):
        return self.name
