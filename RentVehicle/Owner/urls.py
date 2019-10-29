from django.urls import path
from . import views

app_name = 'Owner'

urlpatterns = [
    path("OwnerVehicles/", views.ListOwnerVehicles.as_view(), name="OwnerVehicles"),
    path("AddVehicle/",views.CreateVehicle.as_view(),name = 'CreateVehicle'),
    path("VehicleDetails/<VehicleRegistrationNumber>/<int:pk>",views.VehicleDetails.as_view(), name = "VehicleDetails"),
    path("requests/", views.RequestList.as_view(), name = "RequestList"),
    path('requests/<int:pk>', views.RequestDetails.as_view(), name='RequestDetails'),
]
