from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"

    def get_absolute_url(self):
        return reverse('platepick-detail', kwargs={'pk': self.pk})

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price_option = [
        ('option1', '$'),
        ('option2', '$$'),
        ('option3', '$$$'),
        ('option4', '$$$$'),
        ('option5', '$$$$$')
    ]
    visit_option = [
        ('option1', 'Want to Try'),
        ('option2', 'Visited')
    ]
    price = models.CharField(max_length=15, choices=price_option, default='option1')
    visit = models.CharField(max_length=15, choices=visit_option, default='option1')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, default=1, related_name="restaurants")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.cuisine}" # might not need this
