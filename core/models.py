from django.db import models

# Create your models here.
class Photoportfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Printportfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='prints/')
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class TutoringSession(models.Model):
    title = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title