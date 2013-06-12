from django.core.urlresolvers import reverse
from django.contrib import admin

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

from bibiateca.library.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class BookAdmin(AjaxSelectAdmin):
    list_display = ('title', 'author_names', 'edition',)

    search_fields = ('title', 'author__name')

    form = make_ajax_form(Book, {'authors': 'authors'})

    def author_names(self, obj):
        names = []
        for author in obj.authors.all():
            url = '<a href={url}>{label}</a>'.format(
                url=reverse('admin:library_author_change', args=(author.id,)),
                label=author.name
            )
            names.append(url)
        return ', '.join(names)
    author_names.allow_tags = True
    author_names.short_description = 'authors'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
