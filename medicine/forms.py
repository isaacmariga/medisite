from django import forms
from .models import Prescription, Medicine


class PrescriptionForm(forms.ModelForm):
		class Meta:
			model = Prescription
			exclude = ['medicine'] 

class MedicineForm(forms.ModelForm):
		class Meta:
			model = Medicine
			exclude = [] 