from django.db import models

# Create your models here.

class PhoneBook(models.Model):
    firstname   = models.CharField(max_length=200)
    lastname    = models.CharField(max_length=200)
    workplace   = models.CharField(max_length=100)
    email       = models.EmailField()
    phone       = models.CharField(max_length=12)
    age         = models.IntegerField()

    def __str__(self):
        return self.firstname+' '+self.lastname
