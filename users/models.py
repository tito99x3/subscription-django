from django.db import models

# Create your models here.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1478619033.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)