from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    user = models.OneToOneField(User, max_length=150, null=False, blank=False, unique=True,
                                on_delete=models.CASCADE, related_name='donor')
    location = models.CharField(max_length=200,null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False, unique=True)
    password = models.CharField(max_length=30, null=False, blank=False)
    donations = ArrayField(models.CharField(max_length=100))

    def __str__(self):
        self.name

class Institute(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    user = models.OneToOneField(User, max_length=150, null=False, blank=False, unique=True,
                                on_delete=models.CASCADE, related_name='institute')
    location = location = models.CharField(max_length=200,null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False, unique=True)
    password = models.CharField(max_length=30, null=False, blank=False)
    cnpj = models.CharField(max_length=18, null=False, blank=False, unique=True)

    def __str__(self):
        self.name

class Donation(models.Model):
    FOOD_CHOICES = (
        ('FRESH', 'Alimentos Frescos'),
        ('CANNED', 'Enlatados'),
        ('CHILLED', 'Embutidos'),
        ('GRAIN', 'Grãos')
    ) 
    food = models.CharField(max_length=100, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    type_food = models.CharField(null=False, max_length=150, choices=FOOD_CHOICES)
    reciver = models.CharField(Institute, blank=False, null=False, max_length=150)

    def __str__(self):
        self.food