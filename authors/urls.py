from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.log_out, name='logout'),
]




# from django.urls import path
# from . import views

# urlpatterns = [

#     path('signup/', views.SignupPage, name='signup'),
#     path('login/', views.LoginPage, name='login'),
#     path('logout/',views.LogoutPage,name='logout'),
    
# ]