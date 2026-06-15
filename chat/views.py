from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def users_list(request):

    users = User.objects.exclude(
        id=request.user.id
    )

    return render(
        request,
        "chat/users.html",
        {
            "users": users
        }
    )

from django.db.models import Q
from .models import Message


@login_required
def conversation(request, user_id):

    messages = Message.objects.filter(
        Q(
            sender=request.user,
            receiver_id=user_id
        )
        |
        Q(
            sender_id=user_id,
            receiver=request.user
        )
    )

    other_user = User.objects.get(
        id=user_id
    )

    return render(
        request,
        "chat/conversation.html",
        {
            "messages": messages,
            "other_user": other_user
        }
    )

from django.shortcuts import redirect


@login_required
def send_message(request, user_id):

    if request.method == "POST":

        Message.objects.create(
            sender=request.user,
            receiver_id=user_id,
            text=request.POST["message"]
        )

    return redirect(
        "conversation",
        user_id=user_id
    )