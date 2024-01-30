from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


# Create your models here

class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Train number")
    travel_time = models.PositiveSmallIntegerField(verbose_name="TIme in a trip")
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='to_city_set')

    def __str__(self):
        return f" Train {self.name} from {self.from_city.name} to {self.to_city.name}"

    def __repr__(self):
        return f" Train {self.name} from {self.from_city.name} to {self.to_city.name}"


    class Meta:
        verbose_name = "Train"
        verbose_name_plural = "Trains"
        ordering = ['travel_time']

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError("Change department or arrival city")
        qs = Train.objects.filter(from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time).exclude(
            pk=self.pk)
        if qs.exists():
            raise ValidationError('Change time in a trip')


