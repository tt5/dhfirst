from django.db import models

class MyString(models.Model):
    mystring = models.CharField(max_length=50)

