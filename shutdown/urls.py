#path('shutdown/it', shutdownIT)
from django.urls import path
from shutdown.views import *

urlpatterns = [
    path('shutdown/it', shutdown_it),
    path('shutdown/it/<int:pc>', shutdown_detail_it),
    path('shutdown/hitech', shutdown_hitech),
]