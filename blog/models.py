from django.db import models
from django.db.models.fields import CharField, DateField, TextField

# Create your models here.

class Blog(models.Model):
    title = CharField(max_length=200)
    date = DateField()
    description = TextField()

    def __str__(self):
        return self.title