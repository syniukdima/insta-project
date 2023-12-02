from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from users.forms import CustomUserCreationForm
from chats.models import ChatModel
from .forms import UserProfileForm, AvatarUserForm, BackgroundForm

User = get_user_model()


class SignUp(CreateView):
    """Class to represent the registration page"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class Profile(DetailView):
    """Class to represent the profile page"""

    pk_url_kwarg = 'username'

    def get(self, request, *args, **kwargs):
        userProfile = User.objects.filter(
            username=self.kwargs.get("username")).select_related('avatar')[0]
        form = UserProfileForm()
        form_avatar = AvatarUserForm()
        form_background = BackgroundForm()
        data = {
            "author": userProfile,
            "form": form,
            "form_avatar": form_avatar,
            "form_background": form_background,
            'following': userProfile.following.select_related('avatar'),
            'followers': userProfile.followers.select_related('avatar'),
        }
        return render(request, "users/profile.html", data)


class FollowUser(DetailView):
    """Class to represent the page of the users you are following"""
    
    pk_url_kwarg = 'username'

    def get(self, request, *args, **kwargs):
        authorObj = User.objects.get(username=self.kwargs.get("username"))
        currentUserObj = User.objects.get(username=request.user.username)
        following = authorObj.following.all()
        if self.kwargs.get("username") != currentUserObj.username:
            if currentUserObj in following:
                authorObj.following.remove(currentUserObj.id)
            else:
                authorObj.following.add(currentUserObj.id)
        return HttpResponseRedirect(reverse('profile', args=[authorObj.username]))


class EditProfile(DetailView):
    """Class to represent the profile edit page"""

    pk_url_kwarg = 'username'

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST)
        form_avatar = AvatarUserForm(request.POST, request.FILES)
        form_background = BackgroundForm(request.POST, request.FILES)
        new_username = self.kwargs.get("username")

        if form.is_valid():
            new_username = form.cleaned_data['username']
            if new_username == self.kwargs.get("username") or not new_username:
                User.objects.filter(username=self.kwargs.get(
                    "username")).update(username='')
                User.objects.filter(username='').update(
                    username=self.kwargs.get("username"))
                new_username = self.kwargs.get("username")
            else:
                User.objects.filter(username=self.kwargs.get(
                    "username")).update(username=new_username)
                ChatModel.objects.filter(sender=self.kwargs.get(
                    "username")).update(sender=new_username)

        if form_avatar.is_valid() and form_background.is_valid():
            if form_avatar.cleaned_data['avatar']:
                avatar = form_avatar.save()
                User.objects.filter(
                    username=new_username).update(avatar=avatar)
            if form_background.cleaned_data['background']:
                background = form_background.save()
                User.objects.filter(username=new_username).update(
                    background=background)
        return HttpResponseRedirect(reverse('profile', args=[new_username]))


class Search(ListView):
    """Class to represent the search page"""
    
    template_name = "partials/search.html"

    def post(self, request, *args, **kwargs):
        query = self.request.POST.get('q')
        object_list = User.objects.filter(
            Q(username__icontains=query)
        ).select_related('avatar')
        return render(request, self.template_name, {'search_users': object_list})
