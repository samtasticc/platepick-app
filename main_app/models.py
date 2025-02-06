from django.db import models
from django.urls import reverse

# Create your models here.
class Destination(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('platepick-detail', kwargs={'platepick_id': self.id})