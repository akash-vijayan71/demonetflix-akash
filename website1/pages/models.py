from django.db import models

# Create your models here.

class Contact(models.Model):
    con_name=models.CharField(max_length=255)
    con_email=models.EmailField()
    con_message=models.TextField()
    
    def __str__(self):
        return self.con_name

class Register(models.Model):
    reg_name=models.CharField(max_length=255)
    reg_email=models.EmailField()
    reg_phone=models.TextField()
    reg_uname=models.CharField(max_length=255)
    reg_pwd=models.CharField(max_length=255)

    def __str__(self):
        return self.reg_name

class Video(models.Model):
    v_name=models.CharField(max_length=255)
    v_video=models.FileField(upload_to='videos')
    v_thumbnail=models.FileField(upload_to='videos',null=True)

    def __str__(self):
        return self.v_name
class Adminlogin(models.Model):
    ad_name=models.CharField(max_length=255)
    ad_uname=models.CharField(max_length=255)
    ad_pwd=models.CharField(max_length=255)

    def __str__(self):
        return self.ad_name    
