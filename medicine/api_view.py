from django.shortcuts import render, redirect
from .models import Profile, Supplier, Medicine, Donating, Purchasing, Prescription
from .serializer import ProfileSerializer, SupplierSerializer, MedicineSerializer, DonatingSerializer, PurchasingSerializer, PrescriptionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfileList(APIView):
		def get(self, request, format=None):
				profile = Profile.get_all_profiles()
				serializers = ProfileSerializer(profile, many=True)
				return Response(serializers.data)
        
class SupplierList(APIView):
		def get(self, request, format=None):
				suppliers = Supplier.get_all_suppliers()
				serializers = SupplierSerializer(suppliers, many=True)
				return Response(serializers.data)
        
class MedicineList(APIView):
		def get(self, request, format=None):
				medicines = Medicine.get_all_medicines()
				serializers = MedicineSerializer(medicines, many=True)
				return Response(serializers.data)
        
class DonatingList(APIView):
		def get(self, request, format=None):
				donations = Donating.get_all_donations()
				serializers = DonatingSerializer(donations, many=True)
				return Response(serializers.data)
        
class PurchasingList(APIView):
		def get(self, request, format=None):
				purchase = Purchasing.get_all_purchases()
				serializers = ProfileSerializer(purchase, many=True)
				return Response(serializers.data)
        
class PrescriptionList(APIView):
		def get(self, request, format=None):
				prescription = Prescription.get_all_prescriptions()
				serializers = PrescriptionSerializer(prescription, many=True)
				return Response(serializers.data)
        
