from Vehicle import models
from django import forms
from dropdowndb.models import ZipCode
import datetime

class CreateFilter(forms.ModelForm):
    class Meta:
        model = models.Filter
        fields = ['zipcode', 'make', 'color', 'StartPrice', 'EndPrice', 'rating','style','bookingDate']

    # def initiate(self, User):
    #

    def __init__(self, User, *args,**kwargs):
        super(CreateFilter, self).__init__(*args, **kwargs)
        try:
            filter = models.Filter.objects.get(user=User)
            print("Here")
            self.fields['zipcode'].initial = filter.zipcode
            self.fields['make'].initial = filter.make
            self.fields['color'].initial = filter.color
            self.fields['StartPrice'].initial = filter.StartPrice
            self.fields['EndPrice'].initial = filter.EndPrice
            self.fields['rating'].initial = filter.rating
            self.fields['style'].initial = filter.style
            self.fields['bookingDate'].initial = filter.bookingDate
        except:
            print("rik")
        self.fields['zipcode'].required = False
        self.fields['make'].required = False
        self.fields['color'].required = False
        self.fields['StartPrice'].required = False
        self.fields['EndPrice'].required = False
        self.fields['rating'].required = False
        self.fields['style'].required = False
        self.fields['bookingDate'].required = False
        print("After rik")
        # filter = models.Filter.objects.get(user=None)
        # print("Here")
        # self.fields['zipcode'].initial = filter.zipcode
        # self.fields['make'].initial = filter.make
        # self.fields['color'].initial = filter.color
        # self.fields['StartPrice'].initial = filter.StartPrice
        # self.fields['EndPrice'].initial = filter.EndPrice
        # self.fields['rating'].initial = filter.rating
        # self.fields['style'].initial = filter.style
        # self.fields['bookingDate'].initial = filter.bookingDate
        # self.fields['zipcode'].required = False
        # self.fields['make'].required = False
        # self.fields['color'].required = False
        # self.fields['StartPrice'].required = False
        # self.fields['EndPrice'].required = False
        # self.fields['rating'].required = False
        # self.fields['style'].required = False
        # self.fields['bookingDate'].required = False

    def clean_bookingDate(self):
        bookingdate = self.cleaned_data.get('bookingDate')
        if(bookingdate < datetime.date.today()):
            raise forms.ValidationError("Booking date has to be future date")
        return bookingdate
