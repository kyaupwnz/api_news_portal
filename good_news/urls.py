from rest_framework.routers import DefaultRouter

from good_news.apps import GoodNewsConfig
from good_news.views import NewsPostViewSet, CommentsViewSet

app_name = GoodNewsConfig.name
router = DefaultRouter()
router.register(r'posts', NewsPostViewSet, basename='posts'),
router.register(r'comments', CommentsViewSet, basename='comments')

urlpatterns = [] + router.urls
