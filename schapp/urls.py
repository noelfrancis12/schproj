from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('admpage',views.admpage,name='admpage'),
    path('addc',views.addc,name='addc'),
    path('addcdb',views.addcdb,name='addcdb'),
    path('adds',views.adds,name='adds'),
    path('addsdb',views.addsdb,name='addsdb'),
    path('login1',views.login1,name='login1'),
]