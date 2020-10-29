from rest_framework import serializers
from user.models import User


class UserRegisterSerializer(serializers.Serializer):

    UserTypeChoices = [
        (1, 'BASE'),  # 普通用户
        (2, 'VIP')  # VIP用户
    ]
    SOURCE_TYPE = [
        (1, 'qq'),
        (2, 'weixin'),
        (3, 'cms'),
        (4, 'other')
    ]

    # 用户名
    username = serializers.CharField(
        max_length=20, min_length=6, error_messages={'info': '用户名要求6-20位'},
        required=True
    )
    # 邮箱
    email = serializers.EmailField(error_messages={'info': '邮箱格式错误'}, required=True)
    # 密码
    password = serializers.CharField(
        max_length=30, min_length=6, error_messages={'info': '密码要求6-30位'},
        required=True, write_only=True
    )
    # 确认密码
    confirm_password = serializers.CharField(max_length=30, min_length=6, required=True, write_only=True)
    # 是否记住我
    is_remember = serializers.BooleanField(write_only=True)
    # 用户来源
    source_type = serializers.ChoiceField(choices=SOURCE_TYPE, default=4)
    # 用户类型
    user_type = serializers.ChoiceField(choices=UserTypeChoices, default=1)

    class Meta:
        # **在其中指定的字段必须在序列化器中定义，才会序列化返回。**
        read_only_fields = ['username', 'email', 'source_type', 'user_type']

    def validate(self, attrs):
        """数据验证方法"""
        password = attrs['password']
        confirm_password = attrs.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('两次密码输入不一致，请重新输入')
        return attrs

    def create(self, validated_data):
        """重写保存逻辑"""
        validated_data.pop('is_remember')
        return User.objects.create(**validated_data)
