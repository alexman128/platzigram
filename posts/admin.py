
# Django
from django.contrib import admin

from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts Admin"""

    list_display = ('pk', 'user', 'title', 'photo', 'created', 'modified')
    list_display_links = ('pk', 'user')
    list_editable = ('photo',)
    list_flter = (
        'created',
        'modified'
    )
class PostInline(admin.StackedInline):
    """Post in-line """
    model = Post
    can_delete = False
    verbose_name_plural = 'posts'
