from django.urls import path
from App1 import views

urlpatterns = [
    
    path('',views.home),
    path('create',views.userReg),
    path('adminhome',views.adminhome),
    path('userhome',views.userhome),
    path('loginp',views.loginp),
    path('adminDishes',views.adminDishes),
    path('adminTable',views.adminTable),
    path('viewUsers',views.viewUsers),
    path('adminlogOut',views.adminlogOut),
    path('viewUsers',views.viewUsers),
    path('editProfile',views.update),
    path('userviewDishes',views.userviewDishes),
    path('reserveTable',views.reserveTable)
]
