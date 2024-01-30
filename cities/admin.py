from django.contrib import admin

from .models import City


# Register your models here.

class CityAdmin(admin.ModelAdmin):
    class Meta:
        model = City

    list_display = ('pk', 'name',)


admin.site.register(City, CityAdmin)
