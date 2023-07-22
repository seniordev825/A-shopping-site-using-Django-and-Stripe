from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.project_index, name="index"),
    path('signup/',views.sign_up, name="signup"),
    path('signin/', views.sign_in, name="signin"),
    path('privacy/', views.privacy, name="privacy"),
    path('about/',views.about, name="about"),
    path('product/', views.product, name="product"),
    path('terms/', views.terms, name="terms"),
    path('checkout/', views.checkout, name="checkout"),
    path('get/', views.stripe_webhook, name="get")
  
]
