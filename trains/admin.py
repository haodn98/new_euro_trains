from django.contrib import admin
from trains.models import Train


# Register your models here.

class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train

    list_display = [field.name for field in Train._meta.fields if field.name != 'id']
    list_editable = ('travel_time',)


admin.site.register(Train, TrainAdmin)
