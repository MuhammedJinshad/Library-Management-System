from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    Department      =   models.CharField(max_length=200)


class Cususer(models.Model):
    profile         =   models.ImageField(upload_to='profile')
    first_name      =   models.CharField(max_length=200)
    last_name       =   models.CharField(max_length=100)
    address         =   models.TextField()
    dob             =   models.DateField()
    phonenumber     =   models.BigIntegerField()
    department      =   models.ForeignKey(Department,on_delete=models.CASCADE)
    username        =   models.ForeignKey(User,on_delete=models.CASCADE)


class Book(models.Model):
    book_name       =   models.CharField(max_length=200)
    stock           =   models.IntegerField()

    
class Issuedbooks(models.Model):
    book_name       =   models.ForeignKey(Book,on_delete=models.CASCADE)
    username        =   models.ForeignKey(Cususer,on_delete=models.CASCADE)
    datetime        =   models.DateTimeField()


class IssuedHistorys(models.Model):
    book_name       =   models.CharField(max_length=200)
    username        =   models.CharField(max_length=200)
    datetime        =   models.DateTimeField()



