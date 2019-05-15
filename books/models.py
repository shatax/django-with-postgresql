from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField('Book Title', max_length=100)
    date_added = models.DateTimeField('Date Added')
    location = models.CharField('Location of the book in the store',max_length=100)
    added_by = models.CharField('Who added?',max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
