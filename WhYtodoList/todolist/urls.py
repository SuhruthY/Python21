from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path("login/", CustomLogin.as_view(), name="login"),
    path("register/", CustomRegister.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),

    path("", TaskList.as_view(), name="tasks"),
    path("add-task/", TaskCreate.as_view(), name="add-task"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task"),
    path("del-task/<int:pk>/", TaskDelete.as_view(), name="del-task"),
]
