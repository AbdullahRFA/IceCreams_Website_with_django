from django.shortcuts import render, HttpResponse
from datetime import datetime
from IceCream_web.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context={
        'variable' : 'this is sent',
        'name':'Abdullah Nazmus-Sakib'
    }
    # messages.success(request,"This is a test message")
    # return HttpResponse("This is home page")
    return render(request, 'index.html',context)

def about(request):
    # return HttpResponse("This is about page")
    return render(request,"about.html")
def services(request):
    # return HttpResponse("This is services page")
    return render(request,"services.html")
def contact(request):
    # return HttpResponse("This is contact page")
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today().date())
        contact.save()
        messages.success(request, "Your message has been sent successfully!")

    return render(request,"contact.html")