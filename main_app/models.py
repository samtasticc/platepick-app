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

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = [
        ('option1', '$'),
        ('option2', '$$'),
        ('option3', '$$$'),
        ('option4', '$$$$'),
        ('option5', '$$$$$')
    ]
    visit = [
        ('option1', 'Want to Try'),
        ('option2', 'Visited')
    ]

    def __str__(self):
        return f"{self.get_name_display()} on {self.date}"
