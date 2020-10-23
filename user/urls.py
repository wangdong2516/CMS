from django.urls import path
from user.views import UserView


urlpatterns = [
    path('index/', UserView.as_view(), name='index'),
]