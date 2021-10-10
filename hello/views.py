from django.shortcuts import render
from .models import MyString

def index(request):
    strings = MyString.objects.all().delete()
    newString = MyString(mystring = "hu1")
    newString.save()
    newString = MyString(mystring = "hu2")
    newString.save()
    strings = MyString.objects.all()
    return render(request, 'hello/index.html', {'strings': strings})
