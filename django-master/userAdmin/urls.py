from django.urls import  path
from userAdmin import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns =[

 
 path('', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
 path('register/', user_views.register, name = 'register'),
path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    

]
app_name ='userAdmin'