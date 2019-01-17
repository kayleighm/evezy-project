from django.forms import ModelForm, ValidationError, SplitDateTimeField
from django.db.models import Q
from .models import Booking
from datetime import datetime, timedelta
from django.contrib.admin.widgets import AdminSplitDateTime
from django.conf import settings

class BookingForm(ModelForm):
    start_time = SplitDateTimeField(widget=AdminSplitDateTime(), input_date_formats=settings.DATE_INPUT_FORMATS, input_time_formats=settings.TIME_INPUT_FORMATS)
    end_time = SplitDateTimeField(widget=AdminSplitDateTime(), input_date_formats=settings.DATE_INPUT_FORMATS, input_time_formats=settings.TIME_INPUT_FORMATS)
    
    class Meta:
        model = Booking
        fields = "__all__"

    def clean(self):
        cleaned_data = super(BookingForm, self).clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        car = cleaned_data.get("car")
        driver = cleaned_data.get("driver")
        
        if not start_time or not end_time:
            return

        #CHECK FOR OVERLAPPING BOOKINGS on Car or Driver
        overlapping_bookings = Booking.objects.filter(Q(car__pk=car.pk) | Q(driver__pk=driver.pk) ).filter( Q(start_time__gte=start_time, start_time__lt=end_time) | Q(end_time__gt=start_time, end_time__lte=end_time))
        if overlapping_bookings.count() > 0:
            raise ValidationError(
                    "This car is unavailable for this date/time or you already have another car booked for this slot."
                )

        #CHECK FOR PADDING TIME
        start_time_minus_2hrs = start_time - timedelta(hours=2)
        invalid_bookings = Booking.objects.filter(car__pk=car.pk).filter(Q(end_time__gt=start_time_minus_2hrs) & Q(start_time__lt=start_time_minus_2hrs))
        if invalid_bookings.count() > 0:
            raise ValidationError(
                    "This car is unavailable for this start time."
                )

        end_time_plus_2hrs = end_time + timedelta(hours=2)
        invalid_bookings = Booking.objects.filter(car__pk=car.pk).filter(Q(start_time__lt=end_time_plus_2hrs) & Q(end_time__gt=end_time_plus_2hrs))
        if invalid_bookings.count() > 0:
            raise ValidationError(
                    "This booking must be ended at an earlier time."
                )
        