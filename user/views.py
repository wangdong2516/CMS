from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class UserView(View):

    def post(self, request):
        return JsonResponse({'message': 'ok'})