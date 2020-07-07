from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('userlist.urls')),
    path('api/', include('usercelebrate.urls'))
]
