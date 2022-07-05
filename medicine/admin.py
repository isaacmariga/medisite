from django.contrib import admin
from .models import Disease, Profile, Supplier, Medicine, Donating, Purchasing, Prescription
# Register your models here.


admin.site.register(Profile)
admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(Donating)
admin.site.register(Purchasing)
admin.site.register(Prescription)
admin.site.register(Disease)