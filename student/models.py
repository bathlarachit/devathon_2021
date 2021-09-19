from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Application(models.Model):
    #special fields
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    birthdate=models.DateField()
    aadhar=models.IntegerField()
    address=models.CharField(max_length=300)
    gender=models.CharField(max_length=10)
    department=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    documents=models.FileField(upload_to="student/pdf",default="")
    photo=models.ImageField(upload_to="student/images", default="")
    notes=models.CharField(max_length=255)
    #special fields
    submitted=models.CharField(max_length=25)

    def __str__(self):
        return self.name
