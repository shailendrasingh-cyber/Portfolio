from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def Home(request):
    if request.method == "POST":
        contact = Contact()
        name=request.POST.get('name')
        phone = request.POST.get('phone')
        email=request.POST.get('email')
        message = request.POST.get('message')
        contact.name=name
        contact.phone=phone
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse("<h1>Thank you for contact me </h1>")
    
    return render(request ,"index.html")

