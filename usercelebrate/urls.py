from django.urls import path
from usercelebrate.views import *

urlpatterns = [
    path('celebrate/create', CelebrateCreateView.as_view()),
    path('celebrate/view', CelebrateListView.as_view())
]