from django.contrib import admin

from bibiateca.library.models import Author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'edition')


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
