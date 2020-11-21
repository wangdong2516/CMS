"""自定义项目日志过滤器"""
import logging
from utils.middleware import local


class RequestLogFilter(logging.Filter):
    """
    日志过滤器
    """

    def filter(self, record):
        record.request_id = getattr(local, 'request_id', 'none')
        record.body = getattr(local, 'body', 'none')
        record.path = getattr(local, 'path', 'none')
        record.method = getattr(local, 'method', 'none')
        record.user_id = getattr(local, 'user_id', 'none')
        record.status_code = getattr(local, 'status_code', 'none')
        record.response = getattr(local, 'response', 'none')
        record.spend_time = getattr(local, 'spend_time', 'none')

        return True