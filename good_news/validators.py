from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from users.models import User


class AgeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        author = value.get('author')
        obj = get_object_or_404(User, pk=author.pk)
        date_now = datetime.now().date()
        age = date_now.year - obj.birth_date.year
        if age < 18:
            raise serializers.ValidationError('Возрастное ограничение 18 лет')


class TitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if any(x in value.get('title').lower() for x in ('ерунда', 'глупость', 'чепуха')):
            raise serializers.ValidationError('В заголовке встречаются запрещенные слова')

