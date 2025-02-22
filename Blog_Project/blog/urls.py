from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/',views.about,name='about'),
    path('login/',views.user_login,name='user_login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.user_logout,name='user_logout'),
    path('dashboard/',views.about,name='dashboard'),




]