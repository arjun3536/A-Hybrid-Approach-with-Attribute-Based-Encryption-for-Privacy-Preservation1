from django.urls import path
from HYBRIDAPPROACHAPP import views

urlpatterns = [
    path('', views.loginpage, name="login"),  # Root URL serves login page
    path('admincourtcasedisplay/', views.admincourtcasedisplay),
    path('operatorregister/', views.operatorregistercode),
    path('operatordisplay/', views.operatordisplay),
    path('advocateregister/', views.advocateregistercode),
    path('adminadvocatedisplay/', views.adminadvocatedisplay),
    path('adminhome/', views.adminhome),
    path('operatorhome/', views.operatorhome),
    path('operatorcourtcasecode/', views.operatorcourtcasecode),
    path('operatoradvocatedisplay/', views.operatoradvocatedisplay),
    path('operatorcourtcasedisplay/', views.operatorcourtcasedisplay),
    path('operatorviewdata/', views.operatorviewdata),
    path('decryptdata/', views.decryptdata, name="decryptdata"),
    path('adddata/', views.adddata),
    path('viewdata/', views.viewdata),
    path('advocatehome/', views.advocatehome),
    path('advocatecourtcasedisplay/', views.advocatecourtcasedisplay),
]
