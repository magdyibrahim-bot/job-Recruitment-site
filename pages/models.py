from django.db import models
from asyncio.windows_events import NULL

class UserForm(models.Model):
    name = models.CharField(max_length=20,null=True)
    mail = models.CharField(max_length=50,null=True) 
    password = models.CharField(max_length=20,null=True)
    talanet = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'User'
    class Meta:
        ordering = ['name']

class AdminForm(models.Model):
    name = models.CharField(max_length=20,null=True)
    mail = models.CharField(max_length=50,null=True) 
    password = models.CharField(max_length=20,null=True)
    companyName = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Admin'
    class Meta:
        ordering = ['name']

class JobForm(models.Model):
    STATUS_CHOICES = (
        ('Opened', 'Opened'),
        ('Closed', 'Closed'),
    )
     
    number = models.CharField(max_length=20,null=True)
    salary=models.CharField(max_length=20,null=True)
    title=models.CharField(max_length=20,null=True)
    companyName=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length = 20,choices = STATUS_CHOICES)
    description=models.CharField(max_length=100,null=True)
    """ def __str__(self):
        return self.number """
    class Meta:
        verbose_name = 'Job'
    class Meta:
        ordering = ['id']
