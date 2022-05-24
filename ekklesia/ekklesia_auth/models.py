from django.db import models

# Create your models here.

class CustomUser(models.Model):
    insert_date = models.DateTimeField()