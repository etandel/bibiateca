from django.core.urlresolvers import reverse
from django.contrib import admin

from bibiateca.library.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'edition')

    search_fields = ('title', 'author__name')

    def author_name(self, obj):
        return '<a href={url}>{label}</a>'.format(
            url=reverse('admin:library_author_change', args=(obj.author_id,)),
            label=obj.author.name
        )
    author_name.allow_tags = True
    author_name.short_description = 'author'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
