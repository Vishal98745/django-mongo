from djongo import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    is_created = models.DateField(auto_now=True)
