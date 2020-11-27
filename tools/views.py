from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.
from utils.word_cloud import WorldCloud


class WordCloudView(View):
    """制作词云"""
    FILE_NAME = 'word_cloud.txt'

    def post(self, request):
        file = request.FILES.getlist('file', None)
        with open(self.FILE_NAME, 'wb+')  as f:
            for file_obj in file:
                for chunk in file_obj.chunks():  # 分块写入文件
                    f.write(chunk)
        wcloud = WorldCloud()
        wcloud.make_word_cloud()
        return JsonResponse({'message': 'ok'})
