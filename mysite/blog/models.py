from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# one to one relationship
class teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=100)
    teacher_reg = models.CharField(max_length=100)
    

# manay to many relationship
class student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_reg = models.CharField(max_length=100)