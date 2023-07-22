from django.contrib import admin

# Register your models here.
from shop.models import Registermodel, Customermodel, Plan, Subscription

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['email']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone','card_number','cardholder_name']
class PlanAdmin(admin.ModelAdmin):
    list_display = ['pid', 'pname', 'pprice']
class SubscriptionAdmin(admin.ModelAdmin):
    list_display=['price','customerid','plan','created','updated']
admin.site.register(Plan, PlanAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Customermodel, CustomerAdmin)
admin.site.register(Registermodel, RegisterAdmin)

