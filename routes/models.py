from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City
from trains.models import Train


# Create your models here

class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Route name")
    overall_travel_time = models.PositiveSmallIntegerField(verbose_name="Overall time in a trip")
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set')
    trains = models.ManyToManyField(Train, verbose_name="Trains list")

    def __str__(self):
        return f" Route №{self.name} from {self.from_city.name} to {self.to_city.name}"

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"
        ordering = ['overall_travel_time']


