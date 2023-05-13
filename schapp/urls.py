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
    path('show',views.show,name='show'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editdb/<int:pk>',views.editdb,name='editdb'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('logout',views.logout,name='logout'),
    path('treg',views.treg,name='treg'),
    path('tregdb',views.tregdb,name='tregdb'),
    path('showt',views.showt,name='showt'),
    path('deletet/<int:pk>',views.deletet,name='deletet'),
    path('uhome',views.uhome,name='uhome'),
    path('seepr',views.seepr,name='seepr'),
    path('editt',views.editt,name='editt'),
]