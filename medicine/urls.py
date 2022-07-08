from django.urls import path, include
from . import views, api_view, reg_api_view



urlpatterns = [
  path('', views.welcome,name = 'test'),
  path('home/<disease>', views.home,name = 'home'),
  path('details/<id>', views.details,name = 'details'),
  # path('profile/<id>', views.profile,name = 'profile'),
  path('donor/<donor>', views.donor,name = 'donor'),

  # path('api/profile/', api_view.ProfileList.as_view(), name = 'profile'),
  path('api/supplier/', api_view.SupplierList.as_view()),
  path('api/medicines/', api_view.MedicineList.as_view()),
  path('api/medicine/<disease>', api_view.MedicineByDisease.as_view()),
  path('api/medicine-id/<id>', api_view.MedicineById.as_view()),
  path('api/mediunits/<id>', api_view.MediUnitsList.as_view()),
  path('api/donation/', api_view.DonatingList.as_view()),
  path('api/purchase/', api_view.PurchasingList.as_view()),
  path('api/prescription/', api_view.PrescriptionList.as_view()),
  path('api/disease/', api_view.DiseaseList.as_view()),


  path('register', reg_api_view.RegisterView.as_view()),
  path('login', reg_api_view.LoginView.as_view()),
  path('user', reg_api_view.UserView.as_view()),
  path('logout', reg_api_view.LogoutView.as_view()),
]

