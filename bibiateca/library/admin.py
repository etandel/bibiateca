from django.core.urlresolvers import reverse
from django.contrib import admin

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

from bibiateca.library.models import Author, Publisher, Book, Series, Comics


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class BookAdmin(AjaxSelectAdmin):
    list_display = ('title', 'author_names', 'publisher_name', 'edition',)

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

    def publisher_name(self, obj):
        if obj.publisher:
            url = '<a href={url}>{label}</a>'.format(
                url=reverse('admin:library_obj.publisher_change',
                            args=(obj.publisher.id,)),
                label=obj.publisher.name
            )
        else:
            url = ''
        return url
    publisher_name.allow_tags = True
    publisher_name.short_description = 'publisher'


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ComicsAdmin(BookAdmin):
    list_display = ('title', 'series_name', 'publisher_name', 'author_names',)

    form = make_ajax_form(Comics, {'authors': 'authors'})

    def series_name(self, obj):
        if obj.series:
            url = '<a href={url}>{label}</a>'.format(
                url=reverse('admin:library_obj.series_change',
                            args=(obj.series.id,)),
                label=obj.series.name
            )
        else:
            url = ''
        return url
    series_name.allow_tags = True
    series_name.short_description = 'series'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Comics, ComicsAdmin)
