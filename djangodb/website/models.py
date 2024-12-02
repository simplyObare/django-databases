from django.db import models


# Create your models here.
class Members(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"Name: {self.fname} {self.lname} Age: {self.age}"
