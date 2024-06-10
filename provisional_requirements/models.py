from django.db import models
from members.models import Member

# Create your models here.
class ProvisionalRequirement(models.Model):
    requirement_ID = models.AutoField(primary_key=True),
    member = models.ForeignKey(Member, on_delete=models.CASCADE),
    completed = models.BooleanField(default=False),
    attendance = models.BooleanField(default=False),
    full_meeting = models.BooleanField(default=False),
    history_tour = models.BooleanField(default=False),
    major_service = models.BooleanField(default=False),
    minor_service = models.BooleanField(default=False),
    debate = models.BooleanField(default=False),
    literary_presentations = models.BooleanField(default=False)