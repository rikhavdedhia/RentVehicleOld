from django.db import models
from dropdowndb import models as dmodels

# Create your models here.
class AcceptRejectBooking(models.Model):
    value = models.ForeignKey(dmodels.AcceptRejectBooking, on_delete=models.CASCADE)
