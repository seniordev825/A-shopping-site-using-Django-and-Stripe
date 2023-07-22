from django import forms
from .models import Registermodel, Customermodel, Subscription
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registermodel
        fields = ['password', 'repeatpassword', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'password'}),
            'repeatpassword': forms.PasswordInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'email': forms.EmailInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Enter your email'}),}


    def clean_email(self):
        data = self.cleaned_data['email']
        if Registermodel.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data

    
class LoginForm(forms.ModelForm):
    class Meta:
        model = Registermodel
        fields = ['repeatpassword', 'email']
        widgets = {
            'repeatpassword': forms.PasswordInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'email': forms.EmailInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Enter your email'}),}
class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customermodel
        fields = ['username', "email",'phone', "addressline1","addressline2", "postalcode", "city","state","country"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'phone': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'addressline1': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'addressline2': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'postalcode': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'city': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'state': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'country': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'email': forms.EmailInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Enter your email'}),}
    def clean_username(self):
        data = self.cleaned_data.get('username')
        # Custom validation logic for username field
        if data.isnumeric():
            raise forms.ValidationError('Name cannot be numeric.')
        return data
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model=Subscription
        fields=['price','plan']
        widgets = {
            'price': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Repeat password'}),
            'plan': forms.TextInput(attrs={'class': 'peer bg-transparent h-10 w-full rounded-lg text-gray-700 placeholder-transparent ring-2 px-2 ring-gray-500 focus:ring-sky-600 focus:outline-none focus:border-rose-600', 'placeholder': 'Enter your email'}),}