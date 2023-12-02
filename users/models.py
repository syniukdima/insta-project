from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class BackgroundUser(models.Model):
    """Class for describing a model with a background"""

    background = models.FileField(upload_to='uploads/background/')
    default = models.BooleanField(default=False)

    @staticmethod
    def defaultImg():
        if BackgroundUser.objects.filter(default=True).exists():
            return BackgroundUser.objects.get(default=True).pk
        defaultBackground = BackgroundUser(
            background='static/default/background/background.png', default=True)
        defaultBackground.save()
        return defaultBackground.pk


class AvatarUser(models.Model):
    """Class for describing a model with a avatar"""

    avatar = models.FileField(upload_to='uploads/avatar/')
    default = models.BooleanField(default=False)

    @staticmethod
    def defaultImg():
        if AvatarUser.objects.filter(default=True).exists():
            return AvatarUser.objects.get(default=True).pk
        defaultAvatar = AvatarUser(
            avatar='static/default/avatar/dp.png', default=True)
        defaultAvatar.save()
        return defaultAvatar.pk


class User(AbstractUser):
    """Class for describing a model with a user"""

    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False)
    avatar = models.ForeignKey(
        AvatarUser, on_delete=models.CASCADE, default=AvatarUser.defaultImg)
    background = models.ForeignKey(
        BackgroundUser, on_delete=models.CASCADE, default=BackgroundUser.defaultImg)
    is_online = models.BooleanField(default=False)
    last_time_online = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.username}"

    def getExcludeObjects(self):
        return reverse('chat', kwargs={'username': self.username})

    def getPkFollowToggle(self):
        return reverse('followToggle', kwargs={'username': self.username})

    def getUsernameProfile(self):
        return reverse('profile', kwargs={'username': self.username})

    def getSearchPage(self):
        return reverse('search')
