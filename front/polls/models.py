import datetime

from django.db import models
from django.utils import timezone
import os

class Group_project(models.Model):
    owner = models.CharField(max_length=100)
    coowner = models.CharField(max_length=100)
    optional_description = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    validity_flag = models.BooleanField()
    
class Group_task(models.Model):
    project_name = models.CharField(max_length=100)
    optional_description = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    validity_flag = models.BooleanField()

class FramaOutput(models.Model):
    phrase = models.CharField(max_length=200)
    output = models.CharField(max_length=30000)
    
    def __str__(self):
        return self.phrase
        
    def outputt(self):
        return self.output


class User(models.Model):
    name = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    validity_flag = models.BooleanField()
    
    def __str__(self):
        return self.login
        
    def passw(self):
        return self.password
    


class Status_data(models.Model):
    status_data_field = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.status_data_field
        
class Directory(models.Model):
    name = models.CharField(max_length=50)
    optional_description = models.CharField(max_length=500, blank=True)
    creation_date = models.DateTimeField('creation_date')
    owner = models.CharField(max_length=30)
    validity_flag = models.BooleanField()
    
    def __str__(self):
        return self.name
    def ret_name(self):
        return self.name
    def is_active(self):
        return self.validity_flag
            
class Section_status(models.Model):
    status_data_field = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date_published')
    validity_flag = models.BooleanField()
    
    def __str__(self):
        return self.status_data_field
    
class Section_category(models.Model):
    category = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date_published')
    validity_flag = models.BooleanField()
    
    def __str__(self):
        return self.category
        
class File(models.Model):
    name = models.CharField(max_length=50)
    optional_description = models.CharField(max_length=500, blank=True)
    creation_date = models.DateTimeField('creation_date')
    owner = models.CharField(max_length = 30)
    validity_flag = models.BooleanField()
    directory_name = models.CharField(max_length=50)
    filepath= models.FileField(upload_to='files', verbose_name="")
    def __str__(self):
        return self.name
    def ret_name(self):
        return self.name
    def ret_owner(self):
        return self.owner
    def is_active(self):
        return self.validity_flag
    def ret_content(self):
        return self.filepath
        
class File_section(models.Model):
    name = models.CharField(max_length=50, blank=True)
    optional_description = models.CharField(max_length=500, blank=True)
    creation_date = models.DateTimeField('date_published')
    owner = models.CharField(max_length=30)
    validity_flag = models.BooleanField()
    file = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    def ret_name(self):
        return self.name
    def ret_owner(self):
        return self.owner
        
        
class Group(models.Model):
    name = models.CharField(max_length=50, blank=True)
    login_1 = models.CharField(max_length=50, blank=True)
    login_2 = models.CharField(max_length=50, blank=True)
    creation_date = models.DateTimeField('date_published')


            
