from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from user.serializers import UserRegisterSerializer
from user.serializers import UserLoginSerializer
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

    def post(self, request):
        ser = UserLoginSerializer(data=request.data)
        if ser.is_valid():
            return JsonResponse({'message': "登录成功"})
        return JsonResponse({'message': ser.errors})

    def get(self, request):
        return JsonResponse({'message': 'ook'})