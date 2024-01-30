from django.db import models
from django.urls import reverse


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('cities:city_detail', kwargs={'pk': self.pk})
