from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm, CustomerForm, SubscriptionForm
from .models import Registermodel
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import stripe
from django.conf import settings
from .models import  Customermodel, Subscription
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def project_index(request):
    return render(request, 'index.html')

def sign_up(request):
    if request.method=='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            email= user_form.cleaned_data['email']
            request.session['email'] = email
            return redirect("checkout")
    else:
        user_form = UserRegistrationForm()
    return render(request,"register.html",{'user_form': user_form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})
    
    
def sign_in(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data['email']
            password = form.cleaned_data['repeatpassword']
            if Registermodel.objects.filter(email=email).exists() and Registermodel.objects.filter(repeatpassword=password).exists():
                return redirect('checkout')
            else:
                return HttpResponse('Disabled account')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def privacy(request):
    return render(request, "privacy.html")

def about(request):
    return render(request, "about.html")

def product(request):
    return render(request,"product.html")

def terms(request):
    return render(request, "terms.html")



def checkout(request):
    
    if request.method == 'POST':
        

        # Create a new CardModel instance
        

        # Save the new card to the database
        form = CustomerForm(request.POST)
        form1=SubscriptionForm(request.POST)
        token = request.POST.get('stripeToken')
        if form.is_valid() and form1.is_valid():
            
            stripe.api_key = settings.STRIPE_SECRET_KEY
            price=form1.cleaned_data['price']
            a=price*100
            plan=form1.cleaned_data['plan']
            
            email= form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            name = form.cleaned_data['username']
            address = {
                'line1': form.cleaned_data['addressline1'],
                'line2': form.cleaned_data['addressline2'],
                'city': form.cleaned_data['city'],
                'state': form.cleaned_data['state'],
                'postal_code': form.cleaned_data['postalcode'],
                'country': form.cleaned_data['country'],
                }
            charge = stripe.Charge.create(
                
                amount=a,  # Amount in cents
                currency='usd',
                description='Example charge',
                source=token,
                shipping={
                'name': name,
                'phone': phone,
                'address': {
                'line1': address['line1'],
                'line2': address['line2'],
                'city': address['city'],
                'state': address['state'],
                'postal_code': address['postal_code'],
                'country': address['country'],
            }
                },
                receipt_email=email
                
            )

            created_customer = stripe.Customer.create(name=name, email=email)
            id1=created_customer.id
            card_model_json = request.POST.get('card_model')
            card_model = json.loads(card_model_json)
            cardholder_name=request.POST.get('cardholder_name')
            m=Customermodel(cardholder_name=cardholder_name, username=name,email=email, phone=phone, addressline1=address['line1'], addressline2=address['line2'],city=address['city'], postalcode=address['postal_code'], state=address['state'],country=address['country'],card_number=card_model['cardNumber'],
            exp_month=card_model['expMonth'],
            exp_year=card_model['expYear'])
            m.save()
            m1=Subscription(plan=plan, price=price, customerid=id1)
            m1.save()
            
            return redirect('index')
    email = request.session.get('email')
    c=CustomerForm(initial={'email': email})
    subform=SubscriptionForm()
    return render(request, 'checkout.html', {'stripe_public_key': settings.STRIPE_PUBLIC_KEY,'form':c,'subform':subform})

def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = json.loads(payload)
    except ValueError as e:
        return HttpResponse(status=400)

    # Handle the specific event type you want to capture
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        card_details = payment_intent['charges']['data'][0]['payment_method_details']['card']

        # Save the card information in the database
        card = Card.objects.create(
            cardholder_name=card_details['name'],
            card_number=card_details['last4'],
            expiration_date=f"{card_details['exp_month']}/{card_details['exp_year']}",
            cvc=card_details['cvc_check'],
            zip_code=card_details['address_zip']
        )

        # Perform any additional actions or logic here

    return HttpResponse(status=200)