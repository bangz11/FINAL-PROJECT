from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html"
    ), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),

    path("add-book/", views.add_book, name="add_book"),
    path("delete-book/<int:book_id>/", views.delete_book, name="delete_book"),
    path("edit-book/<int:book_id>/", views.edit_book, name="edit_book"),
]
