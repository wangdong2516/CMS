"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
from django.urls import include

# 每当Django遇到 include() 时，它将截断匹配的URL，并把剩余的字符串发往包含的URLconf作进一步处理。
# 一个被包含的URLconf接收任何来自parent URLconfs的被捕获的参数,变量将传递给被包含的 URLconf
# 这个被捕获的参数 总是 传递到被包含的URLconf中的 每一 行，不管那些行对应的视图是否需要这些参数

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('user/', include('user.urls', namespace='user'))
]
