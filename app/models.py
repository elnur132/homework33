from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    avatar = models.ImageField(upload_to='ava')

    def __str__(self):
        return self.name