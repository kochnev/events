from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    poster = models.ImageField(upload_to='events', blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    price = models.IntegerField()

    CURRENCY = (
        ('USD', 'USD'),
        ('AMD', 'AMD'),
        ('RUR', 'RUR'),
    )

    currency = models.CharField(max_length=3, choices=CURRENCY, default='AMD')
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name




