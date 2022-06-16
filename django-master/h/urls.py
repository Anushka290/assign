from django.contrib import admin
from django.urls import path,include
from . import index
from demo import views
from userAdmin import views as userAdminViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo.urls')),
    path('',include('userAdmin.urls')),
   

 
]
