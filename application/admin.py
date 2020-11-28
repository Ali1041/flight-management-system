from django.contrib import admin
from .models import *


class airplane_admin(admin.ModelAdmin):
    list_display = ['name', 'model', 'seats', 'airline', 'added_date']
    list_editable = ['seats']
    search_fields = ['referenceNumber']
    ordering = ['-id']

class airport_admin(admin.ModelAdmin):
    list_display = ['name', 'city']
    search_fields = ['name', 'city']
    ordering = ['-id']

class flight_admin(admin.ModelAdmin):
    list_display = [
        'airline',
        'flight_num',
        'departure_airport',
        'arrival_airport',
        'departure_time',
        'arrival_time',
        'price',
        'status',
        'airplane'
    ]

    search_fields = ['flight_num', 'airline']
    ordering = ['-id']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        return qs.filter(airline =  airline_staff.objects.get(user = request.user).airline)


# Register your models here.
admin.site.register(airline)
admin.site.register(airline_staff)
admin.site.register(airplane, airplane_admin)
admin.site.register(airport, airport_admin)
admin.site.register(flight, flight_admin)