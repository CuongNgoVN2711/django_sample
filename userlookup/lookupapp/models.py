from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    birdthday = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=50)
    image = models.URLField(max_length=200, default='')

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)