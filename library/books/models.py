from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.title} - {self.author}'

