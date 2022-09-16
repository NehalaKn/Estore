from django.db import models

# Create your models here.

class  Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=150)
    price=models.PositiveIntegerField()
    publisher=models.CharField(max_length=200)
    quantity=models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name