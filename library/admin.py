from django.contrib import admin
from .models import PictureBook, Picture

class PictureInline(admin.TabularInline):
    model = Picture
    extra = 1

class PictureBookAdmin(admin.ModelAdmin):
    inlines = [PictureInline]

    list_display = ['title', 'author', 'tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(PictureBook, PictureBookAdmin)
