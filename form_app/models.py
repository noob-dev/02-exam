from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    question = models.TextField()

    def __str__(self):
        return self.name
