from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import *
from django.views.generic import ListView, DetailView

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

class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"