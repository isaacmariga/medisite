from django.shortcuts import render, redirect
from django.core.mail import send_mail

import medicine
from .models import User, Supplier, Medicine, Donating, Purchasing, Prescription
from .forms import PrescriptionForm


# Create your views here.



def welcome(request):
	# medicine = Medicine.get_by_id(id)

	return render(request, 'test.html')


def home(request, disease):
	medicines = Medicine.filter_by_disease(disease) 
	
	return render(request, 'home.html',{'medicines':medicines})

def details(request, id):
	medicine = Medicine.get_by_id(id) 
	
	return render(request, 'details.html',{'medicine':medicine})

# def profile(request, id):
# 	profile = Profile.get_by_i
# 	return render(request, 'profile.html',{'profile':profile})d(id) 
	

def donor(request, donor):
	donations = Donating.filter_by_donor(donor) 
	
	return render(request, 'userdonations.html',{'donations':donations})

# @login_required(login_url='/accounts/login/')
def prescription(request, id):
	medicine = Medicine.get_by_id(id)
	if request.method == 'POST':
		form = PrescriptionForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.save(commit=False)
			name.medicine = medicine
			name.save()
		send_mail(
    	'Subject here',
    	'Here is the message.',
    	'aizakmariga@gmail.com',
   		['inmariga@gmail.com'],
   		fail_silently=False,)

		return redirect( prescription,  medicine.id)
	else:
		form = PrescriptionForm()
			
	return render(request ,'form_pages/prescription.html', {'form': form , 'medicine': medicine})
