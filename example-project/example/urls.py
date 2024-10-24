from django.contrib import admin
from django.shortcuts import render
from django.urls import path


def index_view(request):
    return render(
        request,
        "index.html",
        {
            "view_context": "I'm from view context",
        },
    )


urlpatterns = [
    path("", index_view),
]
