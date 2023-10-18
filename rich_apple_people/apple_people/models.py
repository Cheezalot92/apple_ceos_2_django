from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    first_year_active = models.IntegerField()
    
    def __str__(self):
        return self.name