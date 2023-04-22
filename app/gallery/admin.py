from django.contrib import admin

from gallery.models.photo import Photo


# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "signature", "photo", "created_at")
    list_filter = ("id", "author", "signature", "photo", "favorites", "created_at")
    search_fields = ("id", "author", "signature", "photo", "favorites", "created_at")
    fields = ("author", "signature", "photo", "favorites")
    readonly_fields = ("id", "created_at")


admin.site.register(Photo, PhotoAdmin)
