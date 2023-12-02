from django.contrib import admin

from users.models import User, AvatarUser, BackgroundUser


class UserAdmin(admin.ModelAdmin):
    """Class describing the representation of the user model in the admin panel"""

    list_display = ('id', 'username')


admin.site.register(User, UserAdmin)
admin.site.register(AvatarUser)
admin.site.register(BackgroundUser)
