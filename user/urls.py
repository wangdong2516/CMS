from django.urls import re_path
from user import views

# 当include函数指定了namespace参数的时候，必须在子应用的urls.py中指定app_name，否则会报错
app_name = 'user'

urlpatterns = [
    re_path(r'register/$', views.UserRegirestView.as_view(), name='register'),
    re_path('login/', views.UserLoginView.as_view(), name='login'),
]