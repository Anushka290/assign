from unicodedata import name
from django.urls import URLPattern, path
from userAdmin import views as user_views
from django.contrib.auth import views as auth_views
from demo import admin
from . import views
urlpatterns =[
    
    

   



    path('table',views.table,name='table'),
    path('create',views.createe,name='create'),
    path('update_order/<int:pk>', views.updateOrder, name='updateOrder'),
    path('delete_order/<int:pk>/', views.deleteOrder, name="delete_order"),
    

]
app_name ='demo'