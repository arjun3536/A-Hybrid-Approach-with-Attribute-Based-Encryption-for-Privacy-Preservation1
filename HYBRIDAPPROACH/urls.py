from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abe/', include("HYBRIDAPPROACHAPP.urls")),
    path('', lambda request: redirect('/abe/')),  # Redirect root URL to /abe/
]
