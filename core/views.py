from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *

# Create your views here.
class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)

class CarListView(ListView):
    model = Car
    template_name = "car_list.html"

    def queryset(self):
        return Car.objects.filter(is_available=True)
        
class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"

@method_decorator(login_required, name='dispatch')
class BookingView(CreateView):
    template_name = "booking_form.html"
    model = Booking
    form_class = BookingForm

    def get_initial(self):
        car = None
        try:
            car = Car.objects.get(pk=self.kwargs.get('car_pk'))
        except:
            pass
        
        return {
            'car':car,
            'driver': self.request.user
        }

    def get_success_url(self):
        return "/booking/"+str(self.object.pk)+"/confirmation/"
    
    
@method_decorator(login_required, name='dispatch')
class BookingConfirmationView(DetailView):
    template_name = "booking_confirmation.html"
    model = Booking