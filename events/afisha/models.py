from django.db import models
from django.utils import timezone
from datetime import timedelta


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=85)
    description = models.TextField()
    poster = models.ImageField(upload_to='events')
    #company = models.ForeignKey(Company, on_delete=models.CASCADE)
    event_date = models.DateField()
    time_from = models.TimeField(null=True, blank=True)
    time_to = models.TimeField(null=True, blank=True)
    price = models.IntegerField()

    CURRENCY = (
        ('USD', 'USD'),
        ('AMD', 'AMD'),
        ('RUR', 'RUR'),
    )

    currency = models.CharField(max_length=3, choices=CURRENCY, default='AMD')
    address = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    for_kids = models.BooleanField('Детский', default=False)

    def __str__(self):
        return self.name

   # @property
   # def is_today(self):
   #     return timezone.now().date() == self.event_date






