from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from user.serializers import UserRegisterSerializer
# Create your views here.
from django.views import View


class UserView(View):

    def post(self, request):
        return JsonResponse({'message': 'ok'})


class UserRegirestView(CreateAPIView):
    """用户注册视图"""

    serializer_class = UserRegisterSerializer