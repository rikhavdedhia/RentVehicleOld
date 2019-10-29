from django.shortcuts import render, redirect
from django.views import generic
from . import models
from . import forms
from django.http import Http404
from Vehicle import models as vmodels
from dropdowndb import models as dmodels
from Booking import models as bmodels
from django.core.mail import send_mail
from django.conf import settings

class CreateBooking(generic.CreateView):
    form_class = forms.CreateBooking
    model = models.Booking
    template_name = "Booking/booking_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["VRnum"] = self.kwargs.get('VehicleRegistrationNumber')
        print(self.kwargs.get('VehicleRegistrationNumber'))
        context["VRid"] = self.kwargs.get("pk")
        context['vehicle'] = vmodels.Vehicle.objects.get(VehicleRegistrationNumber=self.kwargs.get('VehicleRegistrationNumber'))
        return context

    def form_valid(self, form):
        print("in form_valid")
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        vehicle = vmodels.Vehicle.objects.get(VehicleRegistrationNumber=self.kwargs.get('VehicleRegistrationNumber'))
        self.object.vehicle = vehicle
        self.object.price = vehicle.price + vehicle.securityDeposit
        self.object.requestStatus = dmodels.RequestStatus.objects.get(statusId = 1)
        self.object.bookingStatus = dmodels.BookingStatus.objects.get(statusId = 1)
        self.object.save()
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     book_form = forms.CreateBooking(data = request.POST)
    #     if book_form.is_valid():
    #         self.object = book_form.save(commit=False)
    #         self.object.user = self.request.user
    #         vehicle = vmodels.Vehicle.objects.get(VehicleRegistrationNumber=self.kwargs.get('VehicleRegistrationNumber'))
    #         self.object.vehicle = vehicle
    #         self.object.price = vehicle.price + vehicle.securityDeposit
    #         self.object.requestStatus = dmodels.RequestStatus.objects.get(statusId = 1)
    #         self.object.bookingStatus = dmodels.BookingStatus.objects.get(statusId = 1)
    #         self.object.save()
    #     return redirect('Booking:BookingList')

class RenterBookingList(generic.ListView):
    model = models.Booking
    template_name = 'Booking/RenterBooking_List.html'

    def get_queryset(self):
        try:
            self.bookings = bmodels.Booking.objects.filter(
                user = self.request.user
            )
        except Exception as e:
            print (type(e))
            return ""
        else:
            return self.bookings.all()

class OwnerBookingList(generic.ListView):
    model = models.Booking
    template_name = 'Booking/OwnerBooking_List.html'

    def get_queryset(self):
        try:
            self.bookings = bmodels.Booking.objects.filter(
                vehicle__user = self.request.user
            )
            self.bookings = self.bookings.filter(
                bookingStatus = dmodels.BookingStatus.objects.get(pk=3)
            )
        except Exception as e:
            print (type(e))
            return ""
        else:
            return self.bookings.all()

class RenterBookingDetails(generic.DetailView):
    model = models.Booking
    template_name = "Booking/renterBooking_Detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking = models.Booking.objects.get(pk=self.kwargs.get('pk'))
        if booking.requestStatus == dmodels.RequestStatus.objects.get(pk=3):
            context["accepted"] = True
        if booking.bookingStatus == dmodels.BookingStatus.objects.get(pk=3):

            context["booked"] = True
        return context

class SelectPayment(generic.DetailView):
    template_name = 'Booking/SelectPayment.html'
    model = models.Booking

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking = models.Booking.objects.get(pk=self.kwargs.get('pk'))
        context["pk"] = booking.pk
        return context

class CardPayment(generic.CreateView):
    form_class = forms.CreateCardPayment
    model = models.PaymentDetailsCard
    template_name = "Booking/Card_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        curr_booking = models.Booking.objects.get(pk=self.kwargs.get('pk'))
        curr_booking.bookingStatus = dmodels.BookingStatus.objects.get(statusId=3)
        curr_booking.save()
        self.object.booking = curr_booking
        self.object.save()
        subject = 'Booking Confirmation'
        message = 'Your booking has been confirmed'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rikhavdedhia.2016@gmail.com']#,'d.parikh511@gmail.com','mit.sheth00796@gmail.com','vrajshah180@gmail.com']
        #send_mail( subject, message, email_from, recipient_list)
        return super().form_valid(form)


class CheckPayment(generic.CreateView):
    form_class = forms.CreateCheckPayment
    model = models.PaymentDetailsCheck
    template_name = "Booking/Check_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        curr_booking = models.Booking.objects.get(pk=self.kwargs.get('pk'))
        curr_booking.bookingStatus = dmodels.BookingStatus.objects.get(statusId=3)
        curr_booking.save()
        self.object.booking = curr_booking
        self.object.save()
        return super().form_valid(form)
