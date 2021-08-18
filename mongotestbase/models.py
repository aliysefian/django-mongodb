# from django.db import models
from django import forms
from djongo import models 


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)



class CountryDetected(models.Model):
    country  =     models.CharField(max_length=2)
    CNT      =    models.DecimalField(max_digits=5,decimal_places=2)
    BYTE     =   models.DecimalField(max_digits=5,decimal_places=2)

    class Meta:
        abstract=True


        
class Entry(models.Model):
    time_stamp = models.DateTimeField()
    department = models.IntegerField()

    # countries = models.JSONField(default=list,null=True,blank=True)
    countries = models.ArrayField(
        model_container=CountryDetected,
     
    )
    objects = models.DjongoManager()

    # 
class Author(models.Model):
    country = models.CharField(max_length=200)
    CNT = models.DecimalField()
    BYTE = models.DecimalField()


    
    class Meta:
        abstract = True

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        
class EntryTest(models.Model):
    headline = models.CharField(max_length=255)    
    authors = models.ArrayField(
        model_container=Author,
        model_form_class=AuthorForm
    )
    
    objects = models.DjongoManager()