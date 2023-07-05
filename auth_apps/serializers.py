from django.conf import settings
from rest_framework import serializers, exceptions, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User, Doctor
from utils.messages.hundle_messages import successResponse
from utils.messages.response_SMS import SendSms


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer, TokenObtainPairSerializer):
    # doctor = DoctorSerializer(many=True)
    confirm_psd = serializers.CharField(write_only=True, style={input: 'password'}, )

    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'age', 'is_doctor', 'gender', 'password', 'confirm_psd']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        """
                overrides the parent serializer class validate method
                :param attrs:
                :return:
                """
        if User.objects.filter(phone=attrs['phone']).exists():
            raise exceptions.AuthenticationFailed('The user with the Phone number exist', "user_exists", )
        else:
            password = attrs['password']
            password2 = attrs['confirm_psd']
            attrs.pop('confirm_psd')
            if password != password2:
                raise exceptions.AuthenticationFailed('Passwords must match.', "password_mismatch", )

            user = User.objects.create_user(
                **attrs
            )

            token = super().validate(attrs)
            SendSms("thank you for joining us", user.phone)
            details = {
                "phone": user.phone,
                "name": user.name,
                "gender": user.gender
            }
            data = {
                "details": details,
                "token": token,
                "expires_in": settings.SIMPLE_JWT.get('ACCESS_TOKEN_LIFETIME')
            }
            response_data = successResponse(status_code=status.HTTP_200_OK, message_code="authentication",
                                            message=data)

            return response_data
