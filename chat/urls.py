from django.urls import path
from . import views

urlpatterns = [

    path(
        "users/",
        views.users_list,
        name="users_list"
    ),

    path(
        "chat/<int:user_id>/",
        views.conversation,
        name="conversation"
    ),

    path(
        "send/<int:user_id>/",
        views.send_message,
        name="send_message"
    ),
]