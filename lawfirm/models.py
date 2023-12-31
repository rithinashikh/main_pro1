from django.db import models
from userapp.models import Advocate

class LawFirm(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    contact_no=models.CharField(max_length=200)
    specialization=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    estd_date=models.DateField(default='9999-99-99')
    advocate=models.ManyToManyField(Advocate)

