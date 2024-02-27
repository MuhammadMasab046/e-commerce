from django.db import models
from uuid import uuid4
from aut.models import User

class categary(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return self.title
    


class products(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='media/', blank=False, null=False)
    description = models.TextField()
    categary = models.ForeignKey(categary, on_delete = models.CASCADE) 
 
    def __str__(self):
        return self.title


class cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class billing(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.TextField()
    post_code = models.CharField(max_length=50, blank=False, null=False)
    notes = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return self.first_name + self.last_name 
    
class order(models.Model):
    billing = models.ForeignKey(billing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.billing    
        