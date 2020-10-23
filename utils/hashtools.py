"""
    基于hashids库封装数据库主键加密
"""
import hashids
from django.conf.global_settings import SECRET_KEY


class HashToolKit(object):

    def __init__(self, min_length: int, alphabet='abcdefghijklmnopqrstuvwxyz') -> str:
        """
        :param min_length: 生成hash值字符串的最小长度
        """
        self.min_length = min_length
        # 盐值,使用项目的SECRET_KEY作为盐
        self.salt = SECRET_KEY
        self.alphabet = alphabet
        self._hashids = hashids.Hashids(
            salt=self.salt, alphabet=self.alphabet,
            min_length=self.min_length
        )

    def wrap_id(self, data):
        """
            加密id
        :param data: QuerySet集合
        :return:
        """
        for i in data:
            i.id = self._hashids.encode(i.id)

    def unwrap_id(self, ids: list) -> list:
        """
            解密id
        :return: 解密之后的id
        """
        result = []
        for i in ids:
            result.append(self._hashids.decode(i)[0])
        return result
