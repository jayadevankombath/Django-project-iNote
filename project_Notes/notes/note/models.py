from django.db import models

class Users(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=200)
class Note(models.Model):
    User_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    Title=models.CharField(max_length=200)
    Subtitle=models.CharField(max_length=200)
    Description=models.CharField(max_length=500)
    Date=models.DateField(auto_now_add=True)
