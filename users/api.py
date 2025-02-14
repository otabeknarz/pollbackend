from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from .models import User


@api_view(["GET"])
def get_polls(request):
    return Response([label for choice, label in User.PollChoices.choices], status=200)


@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    return Response(serializers.UserSerializer(users, many=True).data, status=200)


@api_view(["GET"])
def get_user(request, id):
    user = User.objects.filter(id=id).first()
    if not user:
        return Response({"error": "User not found"}, status=404)

    return Response(serializers.UserSerializer(user).data, status=200)


@api_view(["POST"])
def create_user(request):
    request.data["choice"] = get_choice_from_label(request.data.get("choice"))
    user = serializers.UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data, status=201)
    else:
        return Response(user.errors, status=400)


def get_choice_from_label(label_or_choice, reverse=False):
    if reverse:
        for choice, choice_label in User.PollChoices.choices:
            if choice == label_or_choice:
                return choice_label
        return None

    for choice, choice_label in User.PollChoices.choices:
        if choice_label == label_or_choice:
            return choice
    return None


@api_view(["POST"])
def update_user_choice(request):
    user = User.objects.filter(id=request.data.get("id")).first()
    if not user:
        return Response({"error": "User not found"}, status=404)

    labels = [label for choice, label in User.PollChoices.choices]

    if user.choice and request.data.get("choice") is not None:
        return Response(
            {
                "error": "User already voted",
                "user": serializers.UserSerializer(user).data
            },
            status=400
        )

    else:
        if request.data.get("choice") is None:
            user.choice = None
        else:
            user.choice = (
                get_choice_from_label(request.data.get("choice", user.choice))
                if request.data.get("choice") in labels
                else user.choice
            )
        user.save()
        return Response(serializers.UserSerializer(user).data, status=200)


@api_view(["GET"])
def stats_view(request):
    users = User.objects.all()
    stats = {label: 0 for choice, label in User.PollChoices.choices}
    for user in users:
        if get_choice_from_label(user.choice, reverse=True) is not None:
            stats[get_choice_from_label(user.choice, reverse=True)] += 1

    return Response(stats, status=200)
