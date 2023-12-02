from django.urls import path

from . import views

urlpatterns = [
    #  сторінка реєстрації
    path("signup/", views.SignUp.as_view(), name="signup"),

    path("search/", views.Search.as_view(), name="search"),

    path('edit/<str:username>/', views.EditProfile.as_view(), name="edit_profile"),

    path("followToggle/<str:username>/",
         views.FollowUser.as_view(), name="followToggle"),

    path("<str:username>/", views.Profile.as_view(), name="profile"),
]
