from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from user.serializers import UserRegisterSerializer
from django.views import View
# Create your views here.


class UserView(View):

    def post(self, request):
        return JsonResponse({'message': 'ok'})


class UserRegirestView(CreateAPIView):
    """用户注册视图"""

    serializer_class = UserRegisterSerializer


class UserLoginView(APIView):
    """用户登录视图"""
