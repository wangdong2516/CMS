import jwt
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import User
from django.conf import settings


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
    # jwt-token，用来保持状态信息
    access_token = serializers.CharField(read_only=True, max_length=255)

    # 刷新token
    refresh_token = serializers.CharField(read_only=True, max_length=255)

    class Meta:
        # **在其中指定的字段必须在序列化器中定义，才会序列化返回。**
        read_only_fields = [
            'username', 'email', 'source_type',
            'user_type', 'access_token', 'refresh_token'
        ]

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
        user = User.objects.create(**validated_data)
        # 手动创建token
        # payload = {
        #     "user_id": user.id,
        #     "user_name": user.username
        # }

        # token = jwt.encode(payload, key=settings.SECRET_KEY)
        user.refresh_token = str(RefreshToken.for_user(user))
        user.access_token = str(RefreshToken.for_user(user).access_token)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    """用户登录的序列化器"""

    username = serializers.CharField(
        max_length=150, min_length=8, required=True, allow_null=False,

    )
    password = serializers.CharField(max_length=128, min_length=8, required=True, allow_null=False)

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'username': {
                'min_length': 8,
                'max_length': 150,
                'error_messages': {
                    'max_length': '长度超过150',
                    'min_length': '长度少于8'
                }
            },
            'password': {
                'error_messages': {
                    'required': '缺少参数',
                    'max_length': '长度超过150',
                    'min_length': '长度少于8'
                }
            }
        }