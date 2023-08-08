from django.db import models
from association.models import Court, Association
from advocates.models import Address

ROLE_CHOICES = (
    ('netmagics_admin', 'netmagics_admin'),
    ('association_super_admin', 'association_super_admin'),
    ('association_normal_admin', 'association_normal_admin'),
    ('advocate', 'advocate')
)

class Advocate(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    enrollment_id=models.CharField(max_length=200)
    specialization=models.CharField(max_length=200)
    address=models.OneToOneField(Address)
    password=models.CharField(max_length=200)
    profile_image=models.ImageField(null=True,blank=True)
    document_image=models.ImageField(null=True,blank=True)
    role=models.CharField(choices=ROLE_CHOICES, max_length=200, default='advocate')
    association=models.ManyToManyField(Association,on_delete=models.CASCADE)

    def __str__(self): 
        return self.name 


class Registrar(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    profile_image=models.ImageField(null=True,blank=True)
    document_image=models.ImageField(null=True,blank=True)
    court=models.ForeignKey(Court, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name 

