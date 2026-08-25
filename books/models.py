from django.db import models
from django.contrib.auth.models import User

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
    author= models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    categories = models.ManyToManyField(Category)
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="books",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title} by {self.author}"


