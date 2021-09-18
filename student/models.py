from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    birthdate=models.DateField()
    aadhar=models.IntegerField()
    address=models.CharField(max_length=300)
    gender=models.CharField(max_length=10)
    department=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    documents=models.FileField()
    passport=models.FileField()
    notes=models.CharField(max_length=255)

    def __str__(self):
        return self.name

