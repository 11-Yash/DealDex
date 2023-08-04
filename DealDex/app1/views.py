from django.shortcuts import render,redirect
from app1.models import signupfrom

# Create your views here.

def signupview(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password1')
        en=signupfrom(email=email,password=password)
        en.save()
    return render(request, 'signup.html')
                  
def signinview(request):
    return render(request, 'signin.html')