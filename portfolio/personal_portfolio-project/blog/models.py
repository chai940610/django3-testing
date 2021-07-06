from django.db import models

class Blogger(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    date= models.DateTimeField()
    description= models.TextField()

    def __str__(self):
        return self.title
    