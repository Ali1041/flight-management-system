from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth
# Create your models here.

class airline(models.Model):
    name = models.CharField(max_length = 150)
    country = models.CharField(max_length = 150)
    isActive = models.BooleanField(default = True)
    added_date = models.DateTimeField(default = datetime.now(), editable = False)

    def __str__(self):
        return f'{self.name} - ({self.country})'


class airline_staff(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    airline = models.ForeignKey(airline, on_delete = models.CASCADE)


class airplane(models.Model):
    name = models.CharField(max_length = 150)
    model_year = models.CharField(max_length = 150)
    seats = models.IntegerField(default = 30)
    airline = models.ForeignKey(airline, on_delete = models.CASCADE)
    added_date = models.DateTimeField(default = datetime.now(), editable = False)

    def __str__(self):
        return f'{self.name} ({self.model_year})'

class airport(models.Model):
    name = models.CharField(max_length = 150)
    city = models.CharField(max_length = 150)
    
    def __str__(self):
        return f'{self.name} ({self.city})'

class flight(models.Model):
    airline = models.ForeignKey(airline, on_delete = models.CASCADE, null = True)
    flight_num = models.IntegerField()
    departure_airport = models.ForeignKey(airport, on_delete = models.CASCADE, related_name = "Departure")
    arrival_airport = models.ForeignKey(airport, on_delete = models.CASCADE, related_name = "Arrival")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.FloatField()
    status = models.CharField(max_length = 150, choices = [('upcoming', 'upcoming'), ('in progress', 'in progress'), ('delayed', 'delayed')], default = 'upcoming')
    airplane = models.ForeignKey(airplane, on_delete = models.CASCADE)


# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver