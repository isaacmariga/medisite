from django.urls import path, include
from . import views, api_view



urlpatterns = [
  path('', views.welcome,name = 'test'),
  path('home/<disease>', views.home,name = 'home'),
  path('details/<id>', views.details,name = 'details'),
  path('profile/<id>', views.profile,name = 'profile'),
  path('donor/<donor>', views.donor,name = 'donor'),

  path('api/profile/', api_view.ProfileList.as_view(), name = 'profile'),
  path('api/supplier/', api_view.SupplierList.as_view()),
  path('api/medicine/', api_view.MedicineList.as_view()),
  path('api/donation/', api_view.DonatingList.as_view()),
  path('api/purchase/', api_view.PurchasingList.as_view()),
  path('api/prescription/', api_view.PrescriptionList.as_view()),

]
