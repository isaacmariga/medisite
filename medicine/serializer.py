from rest_framework import serializers
from .models import Profile, Supplier, Medicine, Donating, Purchasing, Prescription, Disease


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
      model = Profile
      fields = ('password', 'email', 'user', 'phone_number','category')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
      model = Supplier
      fields = ('name', 'email', 'location', 'phone_number','category','profile_pic','bio','password')

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
      model = Medicine
      fields = ('id','name', 'disease', 'price', 'units','description', 'picture')

class DonatingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Donating
      fields = ('amount', 'phone_number','email' 'donor','disease')

class PurchasingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Purchasing
      fields = ('units', 'buyer', 'medicine')

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
      model = Prescription
      fields = ('picture', 'buyer', 'medicine')
class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
      model = Disease
      fields = ('name',)
