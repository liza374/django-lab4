from django.contrib import admin
from .models import Category, Tag, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page', 'category')
    list_filter = ('pub_date', 'main_page', 'category', 'tags')
    search_fields = ('title', 'description', 'slug')
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}
