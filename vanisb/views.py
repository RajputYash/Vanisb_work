from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register
# Create your views here.
def register(request):
    if request.method=='POST':

        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        obj=Register(name=name,email=email,password=password,phone=phone)
        obj.save()
        return redirect('login')
    else:
        return render(request, 'vanisb/register.html')

def login(request):
    return HttpResponse('Registration successfull.Try Login')



