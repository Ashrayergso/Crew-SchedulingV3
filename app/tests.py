```python
from django.test import TestCase
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance

class CrewMemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CrewMember.objects.create(name='John', gender='M', contact='1234567890', position='Captain', availability=True)

    def test_name_label(self):
        crewmember = CrewMember.objects.get(id=1)
        field_label = crewmember._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

# Repeat similar tests for other models and their fields

class AssignCrewToShipsTest(TestCase):
    def setUp(self):
        # Create some test data for the function to work with

    def test_assign_crew_to_ships(self):
        # Call the function and assert the expected results

class ViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Repeat similar tests for other views

class MessageTest(TestCase):
    def test_crew_fetch_success_message(self):
        # Trigger the condition that should result in the message being displayed
        # Assert that the message is in the response

    # Repeat similar tests for other messages
```