import sys

from settings.pro_settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CMS',
        'USER': 'root',
        'PASSWORD': '1277431229',
        'PORT': 3306,
        # 指定存储引擎
        'STORAGE_ENGINE': 'INNODB',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # 设置sql模式为严格模式，这种情况下，一些警告将会升级为错误
            'charset': 'utf8mb4'  # 指定使用的字符集
        }
    },
    'other': {
        'ENGINE':  'django.db.backends.mysql',
        'NAME': 'CMS_SPIDER',
        'USER': 'root',
        'PASSWORD': '1277431229',
        'PORT': 3306,
        'STORAGE_ENGINE': 'INNODB',
    }
}


# 日志系统 logger --> handler --> filter -->  formatter
LOGGING = {
    'version': 1,
    # 是否禁止默认配置的记录器
    'disable_existing_loggers': False,

    # 记录器,django.db.backends是Django数据库默认使用的日志名
    'loggers': {
        'django.db.backends': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False
        },

        # django请求日志，仅记录4XX和5XX的日志
        'django.request': {
            'handlers': ['request', ],
            'level': 'DEBUG',
            'propagate': False
        }
    },

    'handlers': {
        'request': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/Users/wangdong/Desktop/Learn/practice/CMS/request.log',
            'formatter': 'standard',
            'filters': ['request_info']
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG'
    },
    # 日志格式化
    'formatters': {
        'standard': {
            'format': '{"time": "%(asctime)s", "level": "%(levelname)s", "request_id": %(request_id)s, "user_id": %(user_id)s, "path": "%(path)s", "method": "%(method)s", "func": "%(module)s.%(funcName)s:%(lineno)d",  "message": "%(message)s", "status_code": %(status_code)s, "response": %(response)s, "spend_time": %(spend_time)ss}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },

    # 过滤器
    'filters': {
        'request_info': {'()': 'utils.log_filter.RequestLogFilter'},
    },
}
