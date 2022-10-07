import numbers
from django.http import HttpResponse
from django.shortcuts import render

from home.forms import BookingForm

from .models import *

# Create your views here.


def index(request):
    # person = {
    #     'name': 'Divya priya',
    #     'age': 22,
    #     'place': 'palayad nada'
        
    # }
    # numbers = {
    #     'num1':10
    # }
    
    numbers={
        'num1':{1,2,3,4,5,6,7}
    }
    
    # return render(request, 'index.html', numbers)
    return render(request, 'index.html', numbers)


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
            
    form = BookingForm()
    dict_form = {
        'form':form
    }
    return render(request, 'booking.html',dict_form)


def doctors(request):
    dict_doc = {
        'doc':Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_doc)


def contact(request):
    return render(request, 'contact.html')


def department(request):
    dict_dep = {
        'dept':Department.objects.all()
    }
    return render(request, 'department.html',dict_dep)
