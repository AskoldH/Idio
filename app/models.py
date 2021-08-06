from django.db import models


class Idiom(models.Model):
    title = models.CharField(max_length=250)
    meaning = models.TextField()

    def __str__(self):
        return self.title
