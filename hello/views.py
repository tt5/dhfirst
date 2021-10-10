from django.shortcuts import render
from .models import MyString

def index(request):
    objects = MyString.objects.all().delete()
    newString = MyString(mystring = "huhu")
    newString.save()
    objects = MyString.objects.all()
    res="res: "
    for elt in objects:
        res += "( " + elt.mystring + " )"
    someString = res
    context = {'string': someString}
    return render(request, 'hello/index.html', context)
