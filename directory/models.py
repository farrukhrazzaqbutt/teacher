from django.db import models

# Create your models here.
class register(models.Model):

    user_ID = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=70, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_pic = models.CharField(max_length=200,default="",blank=True)
    phone = models.CharField(max_length=200,default="",blank=True)
    room_number = models.CharField(max_length=200,default="",blank=True)

class subject_detail(models.Model):

    subject_ID = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=200)
    user_ID = models.ForeignKey(register, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

class registerAdmin(models.Model):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
