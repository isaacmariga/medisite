from django.contrib import admin
from .models import Disease, User, Supplier, Medicine, Donating, Purchasing, Prescription, MediUnits
# Register your models here.

class  MedicineAdmin(admin.ModelAdmin):
    list_display=('id','name', 'disease', 'price', 'units','description', 'picture')

admin.site.register(User)
admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(Donating)
admin.site.register(Purchasing)
admin.site.register(Prescription)
admin.site.register(Disease)
admin.site.register(MediUnits)