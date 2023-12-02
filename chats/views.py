from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from chats.models import ChatModel
from .services import set_name_group

User = get_user_model()


class BaseChat(LoginRequiredMixin, ListView):
    """Class for displaying a page with user selection for chat"""

    model = User
    template_name = r'chat\index.html'
    context_object_name = 'users'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return User.objects.exclude(
            username=self.request.user.username).select_related('avatar').only(
            'avatar__avatar', 'is_online', 'username', 'is_superuser', 'last_time_online')


class ChatPage(LoginRequiredMixin, DetailView):
    """Class for displaying a chat page"""

    model = User
    template_name = r'chat\chat.html'
    pk_url_kwarg = 'username'
    context_object_name = 'users'
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return User.objects.exclude(username=self.request.user.username).select_related('avatar')\
            .only('avatar__avatar', 'is_online', 'username', 'is_superuser', 'last_time_online')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_obj = User.objects.filter(
            username=self.kwargs.get("username")).select_related('avatar').only(
            'avatar__avatar', 'is_online', 'username', 'is_superuser', 'last_time_online').first()
        context['user'] = user_obj
        context['messages'] = ChatModel.objects.filter(
            thread_name=set_name_group(
            self.request, user_obj)).only(
            'sender', 'new_day', 'timestamp', 'base64', 'message')
        return context
