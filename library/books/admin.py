from django.contrib import admin


from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', )
    list_filter = ('title', 'phone',)
    fieldsets = (
        ('Авторы', {
            'fields': ('title', 'phone', ),
        }),
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title', )
    fieldsets = (
        ('Жанры', {
            'fields': ('title', ),
        }),
    )


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title', 'author', 'genre',)
    fieldsets = (
        ('Жанры', {
            'fields': ('title', 'author', 'genre',),
        }),
    )