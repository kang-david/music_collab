from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title

class Track(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='tracks')
    name = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='tracks/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Collaboration(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='collaborations')
    collaborator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collaborations')
    role = models.CharField(max_length=100)  # 'Guitarist', 'Drummer', etc.
    invited_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.collaborator.username} - {self.role}'

class Comment(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.text[:20]}'
