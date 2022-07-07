
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicine.urls')),
    path('api-token-auth/', obtain_auth_token)
  
]


admin.site.site_header  =  "Medistore bookstore admin"  
admin.site.site_title  =  "Medistore bookstore admin site"
admin.site.index_title  =  "Medistore Bookstore Admin"