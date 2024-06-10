from django.db import models

# Create your models here.
class Member(models.Model):
    computing_id = models.CharField(max_length=7, primary_key=True),
    first_name = models.CharField(max_length=100),
    last_name = models.CharField(max_length=100),
    provie_semester = models.CharField(max_length=100),
    member_type = models.CharField(max_length=100),
    dues_paid = models.BooleanField(default=False)