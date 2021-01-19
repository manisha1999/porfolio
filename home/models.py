from django.db import models

# Create your models here.
class skills(models.Model):
    skill_id = models.AutoField
    skill_name = models.CharField(max_length = 50)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="home/images",default="")

    def __str__(self):
        return self.skill_name

class Project(models.Model):
    pro_id = models.AutoField
    name = models.CharField(max_length = 50)
    desc = models.CharField (max_length = 5000,default="")
    link = models.CharField(max_length=1000,default="")
    image = models.ImageField(upload_to="home/images", default="")
    def __str__(self):
        return self.name

class Contact(models.Model):
    msg_id =models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    msg = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.fname



