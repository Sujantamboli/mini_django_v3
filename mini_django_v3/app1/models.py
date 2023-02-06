from django.db import models

# Create your models here.


class Mymodel(models.Model):

    field1 = models.CharField(max_length=250)
    field2 = models.CharField(max_length=250)


class Portal(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name + " " + self.description





