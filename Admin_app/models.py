from django.db import models
from django.contrib import auth
# Create your models here.
from django.db import models
from student import models as md
# Create your models here.

status_choice=(
('confirmed','confirmed'),
('pending','pending'),
('rejected','rejected'),
)
class Requests(models.Model):
    user = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    req_no =models.ForeignKey(md.Application,on_delete=models.CASCADE)
    status=models.CharField(choices=status_choice,default='pending',max_length=20)
    def __str__(self):
        return self.req_no.name

class Rejected(models.Model):
    message = models.CharField(max_length=256)
    req = models.ForeignKey(Requests,on_delete=models.CASCADE)

class Accepted(models.Model):
    user=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    Registration_Number=models.PositiveIntegerField(unique=True)
