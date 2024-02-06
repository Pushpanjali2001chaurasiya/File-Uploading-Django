from django.shortcuts import render
from . models import *
from .forms import *


def create(request):
    data = registration.objects.all()
    fm=registrationForm(request.POST,request.FILES)
    if fm.is_valid():
        fm.save()
    else:pass
    return render(request,'index.html',{'form':fm,'a':data})

# Create your views here.
