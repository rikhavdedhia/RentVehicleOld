from . import models
from django import forms

class CreateBooking(forms.ModelForm):
    class Meta:
        fields = ('bookingDate','additionalDriverName','additionalDriverLicense')
        model = models.Booking

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['additionalDriverName'].required = False
        self.fields['additionalDriverLicense'].required = False

class CreateCardPayment(forms.ModelForm):
    class Meta:
        exclude = ['booking']
        model = models.PaymentDetailsCard

class CreateCheckPayment(forms.ModelForm):
    class Meta:
        exclude = ['booking']
        model = models.PaymentDetailsCheck
