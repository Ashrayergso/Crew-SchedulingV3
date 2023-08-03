```python
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance

def home(request):
    return render(request, 'app/home.html')

def crewmember_list(request):
    crewmembers = CrewMember.objects.all()
    messages.success(request, "CREW_FETCH_SUCCESS")
    return render(request, 'app/crewmember_list.html', {'crewmembers': crewmembers})

def crewmember_detail(request, pk):
    crewmember = get_object_or_404(CrewMember, pk=pk)
    return render(request, 'app/crewmember_detail.html', {'crewmember': crewmember})

def cert_list(request):
    certs = Cert.objects.all()
    return render(request, 'app/cert_list.html', {'certs': certs})

def cert_detail(request, pk):
    cert = get_object_or_404(Cert, pk=pk)
    return render(request, 'app/cert_detail.html', {'cert': cert})

def qualification_list(request):
    qualifications = Qualification.objects.all()
    return render(request, 'app/qualification_list.html', {'qualifications': qualifications})

def qualification_detail(request, pk):
    qualification = get_object_or_404(Qualification, pk=pk)
    return render(request, 'app/qualification_detail.html', {'qualification': qualification})

def ship_list(request):
    ships = Ship.objects.all()
    messages.success(request, "SHIP_FETCH_SUCCESS")
    return render(request, 'app/ship_list.html', {'ships': ships})

def ship_detail(request, pk):
    ship = get_object_or_404(Ship, pk=pk)
    return render(request, 'app/ship_detail.html', {'ship': ship})

def positions_list(request):
    positions = Positions.objects.all()
    return render(request, 'app/positions_list.html', {'positions': positions})

def positions_detail(request, pk):
    position = get_object_or_404(Positions, pk=pk)
    return render(request, 'app/positions_detail.html', {'position': position})

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'app/assignment_list.html', {'assignments': assignments})

def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    return render(request, 'app/assignment_detail.html', {'assignment': assignment})

def shipcrewallowance_list(request):
    allowances = ShipCrewAllowance.objects.all()
    return render(request, 'app/shipcrewallowance_list.html', {'allowances': allowances})

def shipcrewallowance_detail(request, pk):
    allowance = get_object_or_404(ShipCrewAllowance, pk=pk)
    return render(request, 'app/shipcrewallowance_detail.html', {'allowance': allowance})

def assignCrewToShips(request):
    # TODO: Implement the logic for automatic crew-to-ship assignment
    # This is a placeholder for the core feature of the application
    pass
```