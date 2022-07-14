from django.urls import path, include
from . import views, api_view, reg_api_view



urlpatterns = [
  path('', views.welcome,name = 'test'),
  path('home/<disease>', views.home,name = 'home'),
  path('play/', views.play,name = 'play'),
  path('details/<id>', views.details,name = 'details'),
  path('prescription/<id>', views.prescription,name = 'prescription'),
  path('donor/<donor>', views.donor,name = 'donor'),
  path('celebration', views.celebration,name = 'celebration'),
  path('medicine_upload', views.medicine_upload,name = 'medicine_upload'),

  # path('api/profile/', api_view.ProfileList.as_view(), name = 'profile'),
  path('api/supplier/', api_view.SupplierList.as_view()),
  path('api/medicines/', api_view.MedicineList.as_view()),
  path('api/medicine/<disease>', api_view.MedicineByDisease.as_view()),
  path('api/medicine-id/<id>', api_view.MedicineById.as_view()),
  path('api/mediunits/<id>', api_view.UnitsByMedicine.as_view()),
  path('api/mediunits/', api_view.MediUnitsList.as_view()),
  path('api/donations/<id>', api_view.DonatingByDisease.as_view()),
  path('api/donation/', api_view.DonatingList.as_view()),
  path('api/purchase/', api_view.PurchasingList.as_view()),
  path('api/prescription/', api_view.PrescriptionList.as_view()),
  path('api/disease/', api_view.DiseaseList.as_view()),
  path('api/calculation_units/', api_view.CalculationUnitsList.as_view()),
  path('api/calculation_units_latest/', api_view.CalculationUnitsLatest.as_view()),
  path('api/discounted_price/<id>', api_view.DiscountedPrice.as_view()),
  path('api/units_remaining/<id>', api_view.UnitsRemaining.as_view()),
  path('api/latest_units_medicine/<id>', api_view.LatestPriceByMedicine.as_view()),



  path('api/register', reg_api_view.RegisterView.as_view()),
  path('api/login', reg_api_view.LoginView.as_view()),
  path('api/user', reg_api_view.UserView.as_view()),
  path('api/logout', reg_api_view.LogoutView.as_view()),
]

