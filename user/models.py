from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class travel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    travelname=models.CharField(max_length=100)
    returndate=models.DateField()
    durationoftravel=models.TimeField()

    def __str__(self):
        return self.travelname


CATEGORY_CHOICES = (
    ('low','low'),
    ('medium','medium'),
    ('high','high'),
)
class Items(models.Model):
    travel=models.ForeignKey(travel,on_delete=models.CASCADE)
    itemname = models.CharField(max_length=100)
    ispacked=models.BooleanField(default= False)
    priority = models.CharField(choices=CATEGORY_CHOICES,max_length=10,blank=True)

    def __str__(self):
        return self.itemname

    