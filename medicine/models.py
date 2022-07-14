from datetime import datetime
from email.policy import default
from re import A
from zoneinfo import available_timezones
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db.models import Avg, Sum, Count, Max


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
		picture = CloudinaryField('image',null=True, blank=True)


		def __str__(self):
				return f"{self.name}-{str(self.id)}"
		class Meta:
				verbose_name_plural  =  "Diseases"     


		@classmethod
		def get_all_diseases(cls):
			table = Disease.objects.all()
			return table

		@classmethod
		def get_medicine_number(cls):
				num = list(Disease.objects.values('name').annotate(Count('medicine')))
				# num = count
				print(num)
				return num
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
		
		@classmethod
		def filter_by_disease(cls, id):
			result = cls.objects.filter(disease_id__id=id)
			return result

	
class  Purchasing(models.Model):
		units_sold  = models.IntegerField(null=True, blank=True)
		buyer = models.ForeignKey(User, on_delete=models.CASCADE)
		medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
		phone_number  = models.IntegerField(null=True, blank=True)
		email  = models.TextField(null=True, blank=True)
		delivery_location  = models.TextField(null=True, blank=True)

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
	disease_id  = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True, blank=True)
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



	@classmethod
	def get_test(cls):
		print("result")
		result  = (list(CalculationUnits.objects.values('medicine_id__disease__name').annotate(count=Count('medicine_id__id')))[0]).get('count')

		print(result)
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
			

	# @classmethod
	# def unit_sum(cls, id):
	# 		units = list(CalculationUnits.objects.filter(medicine_id=id).aggregate(Sum('units')).values())
	# 		test = all( i == None for i in units)
	# 		if (test) == True:
	# 				return 1
	# 		else:
	# 				units = int("".join(map(str,units)))
	# 				return units


	# @classmethod
	# def units_sold_sum(cls, id):

	# 		units = list(CalculationUnits.objects.filter(medicine_id=id).aggregate(Sum('units_sold')).values())
	# 		test = all( i == None for i in units)
	# 		if (test) == True:
	# 				return 1
	# 		else:
	# 				units = int("".join(map(str,units)))

	# 				return units

	# @classmethod
	# def set_price_latest(cls, id):
	# 		result = CalculationUnits.objects.all().last()
	# 		return result

	# @classmethod
	# def set_donations_sum(cls, id):
	# 		units = list(CalculationUnits.objects.filter(disease_id__medicine__id=id).aggregate(Sum('donation_amount')).values())
	# 		test = all( i == None for i in units)
	# 		if (test) == True:
	# 				return 1
	# 		else:
	# 				units = int("".join(map(str,units)))
	# 		result  = (list(CalculationUnits.objects.values('medicine_id__disease__name').annotate(count=Count('medicine_id__id')))[0]).get('count')

	# 		donations = units/result


			
	# 		return donations

	@classmethod
	def units_calculated(cls, id):
			units = list(CalculationUnits.objects.filter(medicine_id=id).aggregate(Sum('units')).values())
			test = all( i == None for i in units)
			if (test) == True:
					return 1
			else:
					units = int("".join(map(str,units)))

			units_sold = list(CalculationUnits.objects.filter(medicine_id=id).aggregate(Sum('units_sold')).values())
			test = all( i == None for i in units_sold)
			if (test) == True:
					return 1
			else:
					units_sold = int("".join(map(str,units_sold)))

			if (units-units_sold < 1):
					units_available = 0
			else:
					units_available = (units-units_sold)

			return (units_available)

			

	@classmethod
	def calculations(cls, id):
			units = list(CalculationUnits.objects.filter(medicine_id=id).aggregate(Sum('units')).values())
			test = all( i == None for i in units)
			if (test) == True:
					units = 1
			else:
					units = int("".join(map(str,units)))

			# sec_units = CalculationUnits.objects.filter(medicine_id=id).order_by('-id')[:1].aggregate(Sum('units')).values())


			units_sold = list(CalculationUnits.objects.filter(medicine_id=id).aggregate(Sum('units_sold')).values())
			test = all( i == None for i in units_sold)
			if (test) == True:
					units = 1
			else:
					units_sold = int("".join(map(str,units_sold)))


			set_price = CalculationUnits.objects.filter(medicine_id=id).order_by('-id')
			set_price = set_price[0].set_price


			donations = list(CalculationUnits.objects.filter(disease_id__medicine__id=id).aggregate(Sum('donation_amount')).values())
			test = all( i == None for i in donations)
			if (test) == True:
					units = 1
			else:
					donations1 = int("".join(map(str,donations)))
			# donations2  = (list(CalculationUnits.objects.filter(disease_id = 4).annotate(count=Count('units'))))
			donations2  = list(Disease.objects.values('medicine__disease__name').annotate(Count('medicine')))
			donations2 = donations2[2].get('medicine__count')
			# don = CalculationUnits.objects.filter(disease_id__disease_name=)

			# donations = donations1/donations2
			donations = 300000

# Second last calculations
			Second_last = CalculationUnits.objects.filter(medicine_id=id).order_by('-id')
			Sec_original_price = Second_last[1].set_price
			# Sec_original_price = Sec_original_price[1].set_price

			sec_units = list(CalculationUnits.objects.filter(medicine_id=id).order_by('-id')[1:].aggregate(Sum('units')).values())
			test = all( i == None for i in sec_units)
			if (test) == True:
					units = 1
			else:
					sec_units = int("".join(map(str,sec_units)))

			sec_units_sold = list(CalculationUnits.objects.filter(medicine_id=id).order_by('-id')[1:].aggregate(Sum('units_sold')).values())
			test = all( i == None for i in sec_units_sold)
			if (test) == True:
					units = 1
			else:
					sec_units_sold = int("".join(map(str,sec_units_sold)))

			sec_donations = list(CalculationUnits.objects.filter(disease_id__medicine__id=id).order_by('-id')[1:].aggregate(Sum('donation_amount')).values())
			test = all( i == None for i in sec_donations)
			if (test) == True:
					units = 1
			else:
					sec_donations = int("".join(map(str,sec_donations)))
			result  = (list(CalculationUnits.objects.values('medicine_id__disease__name').annotate(count=Count('medicine_id__id')))[0]).get('count')

			sec_donations = sec_donations/result

			sec_available_units = (sec_units-sec_units_sold)

			sec_total_original_cost = (Sec_original_price*sec_available_units)

			sec_after_discount_price = (sec_total_original_cost-sec_donations)

			sec_price_per_unit = (sec_after_discount_price/sec_available_units)

			sec_discount_per_unit = (Sec_original_price - sec_price_per_unit)

			total_spent_discount = (sec_discount_per_unit*sec_units_sold)


			if ((units-units_sold) < 1):
					available_units = 0
			else :
					available_units =(units-units_sold)


			total_original_price = set_price*available_units


			if ((donations-total_spent_discount) < 1):
					total_donations = 0
			else :
					total_donations = (donations-total_spent_discount)

			after_discount_price = total_original_price-total_donations

			if (total_original_price-total_donations < 1):
					price_per_unit = set_price
			else:
				price_per_unit = after_discount_price/available_units


			print(f"sec-donations - {sec_donations}")
			print(f"sec_available_units -{sec_available_units}")
			print(f"sec_total_original_cost - {sec_total_original_cost}")
			print(f"sec_after_discount_price - {sec_after_discount_price}")
			print(f"sec_price_per_unit - {sec_price_per_unit}")
			print(f"total_spent_discount - {total_spent_discount}")
			print(f"available_units- {available_units}")
			print(f"total_original_price - {total_original_price}")
			print(f"donations - {donations}")
			print(f"donations1 - {donations1}")
			print(f"donations2 - {donations2}")
			print(f"total_donations - {total_donations}")
			print(f"after_discount_price - {after_discount_price}")
			print(f"price_per_unit - {price_per_unit}")
			print(f"set_price - {set_price}")
			return(price_per_unit)



			




			
