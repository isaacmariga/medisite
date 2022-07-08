from django.shortcuts import render, redirect
from .models import User, Supplier, Medicine, Donating, Purchasing, Prescription


# Create your views here.



def welcome(request):

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

