from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username=models.CharField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)
    UserType=models.CharField(max_length=50,null=True,blank=True)

class ContractorTable(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    dob=models.CharField(max_length=50,null=True,blank=True)
    qualification=models.CharField(max_length=50,null=True,blank=True)
    mobilenumber=models.BigIntegerField(null=True,blank=True)
    gender=models.CharField(max_length=250,null=True,blank=True)
    LOGIN = models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)

class BinTable(models.Model):
    BinName=models.CharField(max_length=50,null=True,blank=True)
    BinPlace=models.CharField(max_length=50,null=True,blank=True)
    BinStatus=models.CharField(max_length=50,null=True,blank=True,default='pending')
    CollectionStatus=models.CharField(max_length=50,null=True,blank=True, default='pending')
    Date = models.DateField(auto_now_add=True,null=True,blank=True)
    # CONTRACTORID=models.ForeignKey(ContractorTable,on_delete=models.CASCADE,null=True,blank=True)

    
class StudentTable(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    age=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    department=models.CharField(max_length=250,null=True,blank=True)
    mobilenumber=models.BigIntegerField(null=True,blank=True)
    gender=models.CharField(max_length=250,null=True,blank=True)
    email=models.CharField(max_length=250,null=True,blank=True)
    LOGIN = models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)

   
class RewardTable(models.Model):
    STUDENT =models.ForeignKey(StudentTable,on_delete=models.CASCADE,null=True,blank=True)
    BinId=models.ForeignKey(BinTable,on_delete=models.CASCADE,null=True,blank=True)
    RewardPoint=models.FloatField(null=True,blank=True)
    Date =models.DateTimeField(auto_now_add=True,null=True,blank=True) 





class ComplaintTable(models.Model):
    STUDENT=models.ForeignKey(StudentTable,on_delete=models.CASCADE,null=True,blank=True)
    Complaint=models.CharField(max_length=250,null=True,blank=True)
    Date=models.DateTimeField(auto_now_add=True, null=True,blank=True)
    Reply=models.CharField(max_length=250,null=True,blank=True)
    