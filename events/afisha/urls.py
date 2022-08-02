from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("events/<event_id>/", views.event_detail, name='event_detail'),

]