from django import template
from django.contrib.auth import get_user_model

from our_post.models import UserPost, PostComment

register = template.Library()

User = get_user_model()


@register.simple_tag()
def getPostUser(id):
    return UserPost.objects.filter(userId=id).order_by("-id").prefetch_related(
        'likes', 'content', 'comments').select_related('userId')


@register.simple_tag()
def getCountPostUser(id):
    return UserPost.objects.filter(userId=id).count()


@register.simple_tag()
def getUser(id):
    return User.objects.filter(id=id).select_related('avatar').first()


@register.simple_tag()
def getAllComments():
    return PostComment.objects.all().select_related('userId')
