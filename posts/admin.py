from django.contrib import admin
from .models import Post, Comment


class CommentInLines(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLines]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
