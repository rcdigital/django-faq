from django.contrib import admin
from imagekit.admin import AdminThumbnail
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'show_on_home', 'updated_date',)
    exclude = ('slug', )

admin.site.register(News, NewsAdmin)
