from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out door','Out door'),
    )
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=250, null=True, choices=CATEGORY)
    description = models.TextField(max_length=250, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=250, null=True, choices=STATUS)
    note = models.CharField(max_length=250, null=True)
    def __str__(self):
        return self.product.name