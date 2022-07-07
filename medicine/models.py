from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.


# People models

class Profile(models.Model):
		user = models.ForeignKey(User, on_delete=models.CASCADE)
		password = models.CharField(max_length =300)
		email = models.EmailField()
		phone_number  = models.IntegerField()
		category = models.CharField(max_length =30, default="user")

		def __str__(self):
			return str(self.id)

		@classmethod
		def get_all_profiles(cls):
			table = Profile.objects.all()
			return table

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
				return self.name 
		class Meta:
				verbose_name_plural  =  "Diseases"     


		@classmethod
		def get_all_diseases(cls):
			table = Disease.objects.all()
			return table



class Medicine(models.Model):
		disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True, blank=True)
		name = models.CharField(max_length =30)
		price  = models.IntegerField(null=True, blank=True)
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
		medicine  = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True, blank=True)

		class Meta:
				verbose_name_plural  =  "Medicine Units"  
		def __str__(self):
					return str(self.id) 

		@classmethod
		def filter_by_medicine(MediUnits, id):
			result = MediUnits.objects.filter(medicine__id=id)
			return result	


class  Donating(models.Model):
		amount  = models.IntegerField(null=True, blank=True)
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
		units  = models.IntegerField(null=True, blank=True)
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