from django.contrib import admin
from core.models import Song, Track, Collaboration, Comment

# Register your models here.

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ['collaborator_role']

    def collaborator_role(self, obj):
        return f'{obj.collaborator.username} - {obj.role}'

    collaborator_role.short_description = 'Collaborator Role'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_head']

    def comment_head(self, obj):
        return f'{obj.user.username}: {obj.text[:20]}'

    comment_head.short_description = 'Comment Head'
