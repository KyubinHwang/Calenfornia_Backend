from django.db import models
from accounts.models import User
from subjects.models import Subject
# Create your models here.
class UserSubject(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name = "user")
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name="subject")
    professor_id = models.IntegerField()
    classnum = models.IntegerField()