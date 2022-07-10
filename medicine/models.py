from datetime import datetime
from email.policy import default
from zoneinfo import available_timezones
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


# Create your models here.


# People models

class User(AbstractUser):
		username = models.CharField(max_length=255)
		password = models.CharField(max_length =300)
		email = models.EmailField(max_length=255, unique=True)

		USERNAME_FIELD = 'email'
		REQUIRED_FIELDS = [ 'username']

		def __str__(self):
			return str(self.id)


		@classmethod
		def get_by_id(cls, id):
			result = cls.objects.get(id=id)
			return result	


class Supplier(models.Model):
		name = models.CharField(max_length =30)
		password = models.CharField(max_length =30)
		location = models.CharField(max_length =30)
		bio = models.TextField(max_length =300)
		email = models.EmailField()
		phone_number  = models.IntegerField()
		profile_pic = models.ImageField(upload_to = 'articles/')
		category = models.CharField(max_length =30, default="supplier")

		def __str__(self):
				return self.name

		@classmethod
		def get_all_suppliers(cls):
			table = Supplier.objects.all()
			return table




# Products

class Disease(models.Model):
		name = models.CharField(max_length =30,null=True, blank=True)

		def __str__(self):
				return f"{self.name}-{str(self.id)}"
		class Meta:
				verbose_name_plural  =  "Diseases"     


		@classmethod
		def get_all_diseases(cls):
			table = Disease.objects.all()
			return table

		# @classmethod
		# def get_last(cls):
		# 	result = Disease.objects.all().order_by('-id')
		# 	result = result[1]
		# 	result = result.id
		# 	return result
		# @classmethod
		# def get_last(cls):
		# 	result = Disease.objects.all().last()
		# 	# result = result[1]
		# 	result = result.id
		# 	return result




class Medicine(models.Model):
		disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True, blank=True)
		name = models.CharField(max_length =30)
		description = models.TextField(max_length =300)
		picture = CloudinaryField('image',null=True, blank=True)

		def __str__(self):
				return f"{self.name}-{str(self.id)}"

		class Meta:
				verbose_name_plural  =  "Medicines"   

		@classmethod
		def get_all_medicines(cls):
			table = Medicine.objects.all()
			return table
		
		@classmethod
		def filter_by_disease(Medicine, disease):
			result = Medicine.objects.filter(disease__name=disease)
			return result	

		@classmethod
		def get_by_id(cls, id):
			result = cls.objects.get(id=id)
			return result	

# Actions models
class MediUnits(models.Model):
		units  = models.IntegerField(null=True, blank=True)
		set_price  = models.IntegerField(null=True, blank=True)
		medicine  = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True, blank=True)

		class Meta:
				verbose_name_plural  =  "Medicine Units"  
		def __str__(self):
					return str(self.id) 

		@classmethod
		def get_all_units(cls):
			table = MediUnits.objects.all()
			return table
			
		@classmethod
		def filter_by_medicine(MediUnits, id):
			result = MediUnits.objects.filter(medicine__id=id)
			return result	


class  Donating(models.Model):
		donation_amount  = models.IntegerField(null=True, blank=True)
		phone_number  = models.IntegerField(null=True, blank=True)
		email  = models.TextField(null=True, blank=True)
		donor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
		disease = models.ForeignKey(Disease, on_delete=models.CASCADE ,null=True, blank=True)

		def __str__(self):
			return str(self.id)

		class Meta:
				verbose_name_plural  =  "Donations"   


		@classmethod
		def get_all_donations(cls):
			table = Donating.objects.all()
			return table

		@classmethod
		def filter_by_donor(cls, donor):
			result = cls.objects.filter(donor=donor)
			return result	

	
class  Purchasing(models.Model):
		units_sold  = models.IntegerField(null=True, blank=True)
		buyer = models.ForeignKey(User, on_delete=models.CASCADE)
		medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

		def __str__(self):
			return str(self.id)

		class Meta:
				verbose_name_plural  =  "Purchases"   

		@classmethod
		def get_all_purchases(cls):
			table = Purchasing.objects.all()
			return table

class  Prescription(models.Model):
		picture =  CloudinaryField('image',null=True, blank=True)
		buyer = models.ForeignKey(User, on_delete=models.CASCADE)
		medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

		def __str__(self):
			return str(self.id)
		class Meta:
				verbose_name_plural  =  "Prescriptions"   
				
		@classmethod
		def get_all_prescriptions(cls):
			table = Prescription.objects.all()
			return table

		@classmethod
		def filter_by_medicine(cls, id):
			result = cls.objects.filter(medicine__id=id)
			return result	

class CalculationUnits(models.Model):
	medicine_id  = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True, blank=True)
	units = models.IntegerField( null=True, blank=True)
	units_sold = models.IntegerField(null=True, blank=True)
	set_price = models.IntegerField(null=True, blank=True)
	donation_amount = models.IntegerField(null=True, blank=True)

	def __str__(self):
			return str(self.id)
	
	@classmethod
	def get_all(cls):
		result = CalculationUnits.objects.all()
		return result

	@classmethod
	def get_latest(cls):
		result = CalculationUnits.objects.all().last()
		return result

	@classmethod
	def get_second_last(cls):
			result = CalculationUnits.objects.all().order_by('-id')
			result = result[1]
			return result





	# @classmethod
	# def discounted_price(cls):
	# 		calculation_units = CalculationUnits.objects.all().last()
	# 		units = calculation_units.units
	# 		units_sold = calculation_units.units_sold
	# 		set_price = calculation_units.set_price
	# 		donation_amount = calculation_units.donation_amount

	# 		available_units =(units-units_sold)

	# 		total_original_price = set_price*available_units

	# 		price_per_unit = total_original_price-
			



			




			
