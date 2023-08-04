from django import forms
from .models import CrewMember

class CrewMemberForm(forms.ModelForm):
    class Meta:
        model = CrewMember
        fields = ['name', 'gender', 'contact', 'position', 'availability']
