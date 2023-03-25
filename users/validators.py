from rest_framework import serializers


class EmailValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not any(x in value.get('email') for x in ('mail.ru', 'yandex.ru')):
            raise serializers.ValidationError('Разрешены домены: mail.ru, yandex.ru')
