from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerPage, name='register'),
    path('predict/',views.predict_chances, name='submit_prediction'),
    
]