from django.shortcuts import render

# Create your views here.
def project_index(request):
    return render(request, 'index.html')

def sign_up(request):
    return render(request,"register.html")

def sign_in(request):
    return render(request,"login.html")

def privacy(request):
    return render(request, "privacy.html")

def about(request):
    return render(request, "about.html")

def product(request):
    return render(request,"product.html")

def terms(request):
    return render(request, "terms.html")