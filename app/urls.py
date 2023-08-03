from django.contrib import admin
from django.urls import path, include
from .views import crewmember_list, crewmember_detail, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('crewmember_list/', crewmember_list, name='crewmember_list'),
    path('crewmember_detail/<int:pk>/', crewmember_detail, name='crewmember_detail'),
]

