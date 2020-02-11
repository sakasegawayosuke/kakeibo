from django.contrib import admin

# Register your models here.

#models.pyからCategoryクラスとKakeiboクラスをインポート
from .models import Category, Kakeibo

#家計簿テーブルのカラム名を指定
class KakeiboAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'money', 'memo')

#読み込んだCategoryクラスとKakeiboクラスをadminサイトに表示
admin.site.register(Category)
admin.site.register(Kakeibo, KakeiboAdmin)
