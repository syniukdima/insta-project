from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from chats.views import ChatPage, BaseChat


urlpatterns = [
    # адмін панель
    path('admin/', admin.site.urls),

    # сторінка початкового чату
    path('', BaseChat.as_view(), name='home'),

    # сторінка з можливістю зараєструватися, вийти з акаунту або стоворити його
    path('profile/', include('django.contrib.auth.urls')),

    path('profile/', include('users.urls')),

    # сторінка з всіма постами
    path('post/', include('our_post.urls')),

    # сторінка чату з користувачем
    path('<username>/', ChatPage.as_view(), name='chat'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # значення для завантаження медіа файлів(картинок до посту)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
