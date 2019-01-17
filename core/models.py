# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    reg_number = models.CharField(max_length=15, blank=True, null=True)
    vin = models.CharField(max_length=17, blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    car_model = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.reg_number + " " + self.make + " " + self.car_model

class Booking(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name="car_bookings")
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver_bookings")

    def __str__(self):
        return "Reg: "+self.car.reg_number + " Time: " + self.start_time.strftime("%Y-%m-%d %H:%M") + " - " + self.end_time.strftime("%Y-%m-%d %H:%M")