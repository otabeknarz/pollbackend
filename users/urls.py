from django.urls import path
from . import api

app_name = "users"

urlpatterns = [
    path("get-polls/", api.get_polls),
    path("get-users/", api.get_users),
    path("get-user/<str:id>/", api.get_user),
    path("create-user/", api.create_user),
    path("update-user-choice/", api.update_user_choice),
    path("stats/", api.stats_view),
]
