from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view()),
    url(r'^signup/$', views.SignUpView.as_view()),
    url(r'^$', views.CarListView.as_view(), name='index'),
    url(r'^cars/$', views.CarListView.as_view(), name="cars"),
    url(r'^cars/(?P<pk>[-\d]+)/$', views.CarDetailView.as_view(), name='car-detail'),
    url(r'^cars/(?P<car_pk>[-\d]+)/book/$', views.BookingView.as_view()),
    url(r'^booking/(?P<pk>[-\d]+)/confirmation/$', views.BookingConfirmationView.as_view()),
]