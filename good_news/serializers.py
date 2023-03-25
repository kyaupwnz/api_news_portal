from rest_framework import serializers

from good_news.models import NewsPost, Comments
from good_news.validators import AgeValidator, TitleValidator


class NewsPostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = NewsPost
        validators = [AgeValidator(field='birth_date'),
                      TitleValidator(field='title')]
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comments
        fields = '__all__'
