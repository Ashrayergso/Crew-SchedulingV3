from django.contrib import admin
from django.urls import path
from .views import (
    home,
    crewmember_list,
    crewmember_detail,
    cert_list,
    cert_detail,
    qualification_list,
    qualification_detail,
    ship_list,
    ship_detail,
    positions_list,
    positions_detail,
    assignment_list,
    assignment_detail,
    shipcrewallowance_list,
    shipcrewallowance_detail,
    crewmember_edit,
    crewmember_delete,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # Root path
    path('home', home, name='home_alias'), # Optional alias for the home path
    path('crewmember_list/', crewmember_list, name='crewmember_list'),
    path('crewmember_detail/<int:pk>/', crewmember_detail, name='crewmember_detail'),
    path('cert_list/', cert_list, name='cert_list'),
    path('cert_detail/<int:pk>/', cert_detail, name='cert_detail'),
    path('qualification_list/', qualification_list, name='qualification_list'),
    path('qualification_detail/<int:pk>/', qualification_detail, name='qualification_detail'),
    path('ship_list/', ship_list, name='ship_list'),
    path('ship_detail/<int:pk>/', ship_detail, name='ship_detail'),
    path('positions_list/', positions_list, name='positions_list'),
    path('positions_detail/<int:pk>/', positions_detail, name='positions_detail'),
    path('assignment_list/', assignment_list, name='assignment_list'),
    path('assignment_detail/<int:pk>/', assignment_detail, name='assignment_detail'),
    path('shipcrewallowance_list/', shipcrewallowance_list, name='shipcrewallowance_list'),
    path('shipcrewallowance_detail/<int:pk>/', shipcrewallowance_detail, name='shipcrewallowance_detail'),
    path('crewmember_edit/<int:pk>/', crewmember_edit, name='crewmember_edit'),
    path('crewmember_delete/<int:pk>/', crewmember_delete, name='crewmember_delete'),
]