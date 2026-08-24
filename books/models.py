from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField(blank=True, null=True)
    created_at=models.DateField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


