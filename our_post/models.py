from datetime import datetime
from django.db import models
from django.conf import settings
from django.urls import reverse


class UserPost(models.Model):
    """Class describing a model with a post"""

    userId = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    createdAt = models.DateTimeField(default=datetime.now())
    content = models.ManyToManyField("Photo")
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="collected_votes")
    comments = models.ManyToManyField("PostComment", blank=True,)

    class Meta:
        db_table = "user_post"

    def get_absolute_url(self):
        return reverse('comments', kwargs={'post_id': self.pk})

    def get_pk_for_like(self):
        return reverse('like_post', kwargs={'id': self.pk})

    def get_pk_for_delete(self):
        return reverse('delete', kwargs={'id_post': self.pk})


class Photo(models.Model):
    """Class describing the model with a photo for posts"""

    photo = models.FileField(upload_to='uploads/')


class PostComment(models.Model):
    """Class describing the model with comments on posts"""

    userId = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commentText = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "post_comment"

    def get_pk_for_delete(self):
        return reverse('delete_comment', kwargs={'id_comment': self.pk})
