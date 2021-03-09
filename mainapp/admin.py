from django.contrib import admin

from .models import News


# Видоизменяем админку
class NewsAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'title')
    # какие поля будут участвовать в поиске
    search_fields = ('title', 'content')


admin.site.register(News, NewsAdmin)
