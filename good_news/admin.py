from django.contrib import admin
from good_news.models import NewsPost
from django.urls import reverse

from django.utils.html import format_html



@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'link_to_author', 'creation_date', 'edition_date')
    search_fields = ('title', 'creation_date', 'edition_date', 'author')
    list_filter = ('creation_date',)
    readonly_fields = ('author',)

    def link_to_author(self, obj):
        link = reverse("admin:users_user_change", args=[obj.author.id])
        return format_html('<a href="{}"> {}</a>', link, obj.author.email)
    link_to_author.short_description = 'Автор'


