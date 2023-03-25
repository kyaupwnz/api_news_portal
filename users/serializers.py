from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User
from users.validators import EmailValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        validators = [EmailValidator(field='email')]
        fields = ('email', 'birth_date', 'password')

    def validate_password(self, value):
        min_length = 8
        if len(value) < min_length:
            raise ValidationError(f'Пароль должен содержать минимум {min_length} знаков')
        if not any(x.isdigit() for x in value):
            raise ValidationError('Пароль должен включать цифры')
        if not any(x.isupper() for x in value):
            raise ValidationError('Пароль должен включать заглавные буквы')
        return value

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])

        user.is_active = True
        user.save()
        return user
