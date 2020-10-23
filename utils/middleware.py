"""
    自定义Django中间件
    MAINTAINER wang10272516@163.com
"""
import json
from django.utils.deprecation import MiddlewareMixin
from django.http.response import JsonResponse


class PostRequestMiddleware(MiddlewareMixin):
    """
        实现将POST请求类型为非文件类型的时候，将key-value数据转换为字段
    """

    def process_request(self, request):
        """
            在请求传入视图函数之前调用
        """
        if request.method == 'POST':
            if request.META['CONTENT_TYPE'] == 'application/json':
                try:
                    data = json.loads(request.body)
                except json.JSONDecodeError as e:
                    return JsonResponse({
                        'data': None,
                        'info': '请求数据的格式错误',
                        'success': 0
                    })
            else:
                data = dict(request.POST)
        request.data = data
