from django.contrib import admin
from django.urls import path
from home import views

# Django admin customization
admin.site.site_header = "TODOs Administration"
admin.site.index_title = "Welcome to TODOs Dashboard"
admin.site.site_title = "Welcome to TODOs Portal"

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("add-todo/", views.add_todo, name="add_todo"),
    path("logout/", views.signout, name="signout"),
    path("delete-todo/<int:id>", views.delete_todo, name="delete_todo"),
    path("change-status/<int:id>/<str:status>", views.change_todo, name="change_todo"),
]
