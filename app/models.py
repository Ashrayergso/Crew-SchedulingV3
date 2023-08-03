```python
from django.db import models

class Positions(models.Model):
    position_name = models.CharField(max_length=200)
    position_code = models.CharField(max_length=200)
    contract_length = models.IntegerField()
    vacation_length = models.IntegerField()

    def __str__(self):
        return self.position_name

class CrewMember(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=200)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Cert(models.Model):
    name = models.CharField(max_length=200)
    validity = models.IntegerField()
    expiry = models.DateField()

    def __str__(self):
        return self.name

class Qualification(models.Model):
    crewmember = models.ForeignKey(CrewMember, on_delete=models.CASCADE)
    cert = models.ForeignKey(Cert, on_delete=models.CASCADE)
    expiry = models.DateField()
    date_issued = models.DateField()

    def __str__(self):
        return f"{self.crewmember.name} - {self.cert.name}"

class Ship(models.Model):
    ship_name = models.CharField(max_length=200)
    ship_code = models.CharField(max_length=200)
    ship_brand = models.CharField(max_length=200)

    def __str__(self):
        return self.ship_name

class Assignment(models.Model):
    crewmember = models.ForeignKey(CrewMember, on_delete=models.CASCADE)
    ship_code = models.ForeignKey(Ship, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.crewmember.name} - {self.ship_code.ship_name}"

class ShipCrewAllowance(models.Model):
    ship_code = models.ForeignKey(Ship, on_delete=models.CASCADE)
    quantity_allocated = models.IntegerField()
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ship_code.ship_name} - {self.position.position_name}"
```