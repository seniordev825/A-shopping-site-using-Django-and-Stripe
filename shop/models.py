from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Registermodel(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    repeatpassword=models.CharField(max_length=50)
    invitecode=models.CharField(max_length=50, blank=True, null=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=50, blank=True, null=True)
class Customermodel(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    addressline1=models.CharField(max_length=50)
    addressline2=models.CharField(max_length=50)
    postalcode=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    cardholder_name=models.CharField(max_length=50,  blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    #expiration_date = models.CharField(max_length=10)
    exp_month = models.CharField(max_length=13, blank=True, null=True)
    exp_year = models.CharField(max_length=13, blank=True, null=True)
class Plan(models.Model):
    pid=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)
    pprice=models.CharField(max_length=50)
    def __str__(self):
        return self.pname
class Subscription(models.Model):
    customerid=models.CharField(max_length=50, blank=True, null=True)
    price=models.IntegerField()
    plan=models.ForeignKey(Plan,
                               on_delete=models.CASCADE,
                               related_name='pp')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.created