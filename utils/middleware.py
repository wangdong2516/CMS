"""
    自定义Django中间件
    MAINTAINER wang10272516@163.com
"""
import time
import threading
import json
import logging

from django.template.response import TemplateResponse
from django.utils.deprecation import MiddlewareMixin

local = threading.local()


class RequestMixinMiddleware(MiddlewareMixin):
    """扩展Django request"""

    def process_request(self, request):
        request.body_ = json.dumps(request.GET if request.method == 'GET' else request.POST)


class LoggerMiddleware(MiddlewareMixin):
    """
        实现logger日志打印
    """

    def __call__(self, request):
        """记录request请求信息"""
        start_time = time.time()
        local.request_id = request.correlation_id
        local.path = request.path
        local.user_id = request.user.id
        local.method = request.method
        params = json.dumps(request.GET if request.method == 'GET' else request.POST)
        local.params = params
        response = None
        response = response or self.get_response(request)
        end_time = time.time()
        local.spend_time = '%.2f' % (end_time - start_time)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        local.status_code = response.status_code
        # 这里需要对状态码进行判断，因为django.request只会记录状态码为4xx和5xx开头的请求
        # 这里需要手动记录日志
        if response.status_code == 200 and not isinstance(response, TemplateResponse):
            request_log = logging.getLogger('django.request')
            local.response = json.dumps(json.loads(response.content.decode()))
            request_log.debug(msg=response.reason_phrase)
        try:
            local.response = json.dumps(response.content)
        except Exception as e:
            local.response = json.dumps({})
        return response
