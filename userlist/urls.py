from django.urls import path
from userlist.views import *

urlpatterns = [
    path('children/create', ChildCreateView.as_view()),
    path('children/view', ChildListView.as_view())
]