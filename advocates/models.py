from django.db import models

class Address(models.Model):
    official=models.CharField(max_length=200)
    residential=models.CharField(max_length=200)
