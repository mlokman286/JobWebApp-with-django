from django.db import models
from company.models import Company
from users.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class State(models.Model):
    name= models.CharField( max_length=100)
    def __str__(self):
        return self.name
    
class Industry(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Job(models.Model):
    JOB_TYPE = (
        ('Remote','Remote'),
        ('Onsite','Onsite'),
        ('Hybrid','Hybrid'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.PositiveBigIntegerField(default=2000)
    requirements = RichTextField()
    ideal_candidate = RichTextField()
    is_available = models.BooleanField(default = True)
    published = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)
    deadline= models.DateField(auto_now=False, auto_now_add=False,null=True)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING,null=True,blank=True)
    state =models.ForeignKey(State,on_delete=models.DO_NOTHING,null=True,blank=True)
    job_type= models.CharField(max_length=100,choices=JOB_TYPE,null=True,blank=True,default='Onsite')
    def __str__(self):
        return self.title
    
class ApplyJob(models.Model):
    STATUS_CHOICES = {
        ('Accepted','Accepted'),
        ('Declined','Declinned'),
        ('Pending','Pending')
    }
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_time=models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES)