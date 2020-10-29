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
    }
}


# 数据库日志打印
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
            'level': 'DEBUG',
        },
    }
}