from django.db import models

# Create your models here.
class Aadhar(models.Model):
    Aadhar=models.IntegerField(max_length=50)
    Created_date=models.DateTimeField
    Created_by=models.CharField(max_length=50)
    def __str__ (self):
        return str(self. Aadhar)
class student(models.Model):
    stu_name=models.CharField
    stu_city=models.CharField
    stu_email=models.EmailField(max_length=30)
    Aadhar=models.OneToOneField(Aadhar,on_delete=models.CASCADE) 

    

