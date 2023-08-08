from django.db import models

class Court(models.Model):
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    estd_date = models.DateField(default='9999-99-99')
    address=models.CharField(max_length=200)
    contact_no=models.CharField(max_length=200)
    description=models.CharField(max_length=200)

    def __str__(self): 
        return self.name 

class Jurisdiction(models.Model):
    name=models.CharField(max_length=200)
    area=models.CharField(max_length=200)
    court=models.ForeignKey(Court, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name 
    
class Association(models.Model):
    name=models.CharField(max_length=200)
    estd_date=models.DateField(default='9999-99-99')
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    website=models.CharField(max_length=200)
    contact_no=models.CharField(max_length=200)
    email=models.EmailField()