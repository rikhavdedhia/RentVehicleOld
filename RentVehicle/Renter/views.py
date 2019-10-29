from django.shortcuts import render, redirect
from django.views import generic
from Vehicle import models
from Booking import models as bmodels
from . import forms
from django.http import Http404

# Create your views here.
class ListAvailableVehicles(generic.ListView):
    model = models.Vehicle
    template_name = 'Renter/AvailableVehicle_List.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context

    def get_queryset(self):
        self.form = forms.CreateFilter(User=self.request.user)
        print("Form created")
        #self.form.initiate(self.request.user)
        self.vehicles = models.Vehicle.objects.filter()
        try:
            #self.vehicle = super().get_queryset()

            self.filter = models.Filter.objects.get(user=self.request.user)
            if self.filter.zipcode:
                print('1')
                self.vehicles = self.vehicles.filter(
                    zipcode__zipcode = self.filter.zipcode
                )
            if self.filter.make:
                print('2')
                self.vehicles = self.vehicles.filter(
                    make__make = self.filter.make.make
                )
            if self.filter.color:
                print('3')
                self.vehicles = self.vehicles.filter(
                    color__color = self.filter.color
                )
            if self.filter.StartPrice and self.filter.EndPrice:
                print('4')
                print(self.filter.StartPrice)
                self.vehicles = self.vehicles.filter(
                    price__gte = self.filter.StartPrice

                ).filter(
                price__lte = self.filter.EndPrice
                )
            elif self.filter.EndPrice:
                print('5')
                self.vehicles = self.vehicles.filter(
                    price__lte = self.filter.EndPrice
                )
            elif self.filter.StartPrice:
                print('8')
                self.vehicles = self.vehicles.filter(
                    price__gte = self.filter.EndPrice
                )
            if self.filter.rating:
                print('6')
                self.vehicles = self.vehicles.filter(
                    rating__rating__gte = self.filter.rating.rating
                )
            if self.filter.style:
                print('7')
                self.vehicles = self.vehicles.filter(
                    style__style = self.filter.style
                )
            if self.filter.bookingDate:
                print('8')
                self.vehicles = self.vehicles.exclude(
                    pk = bmodels.Booking.objects.filter(bookingDate = self.filter.bookingDate).pk
                )
        except:
            return self.vehicles.all()
        else:
            return self.vehicles.all()

    def post(self, request, *args, **kwargs):
        filter_form = forms.CreateFilter(data = request.POST, User=self.request.user)
        if filter_form.is_valid():
            print("Form is valid")
            filterForm = filter_form.save(commit=False)
            try:
                filter = models.Filter.objects.get(user=self.request.user)
                print("Filter Found")
                filter.update(zipcode=filterForm.zipcode,
                              make = filterForm.make,
                              color=filterForm.color,
                              style=filterForm.style,
                              StartPrice=filterForm.StartPrice,
                              EndPrice=filterForm.EndPrice,
                              rating=filterForm.rating,
                              bookingDate=filterForm.bookingDate
                              )
            except:
                print(self.request.user)
                filter_form.user = self.request.user
                print("Filter saved")
                filterForm.save()
        else:
            print("Form not valid")
        return redirect('Renter:AvailableVehicles')

class VehicleDetails(generic.DetailView):
    model = models.Vehicle
    template_name = "Renter/RenterVehicle_Detail.html"
    context_object_name = "vehicle_detail"