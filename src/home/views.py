import pathlib
from django.shortcuts import render
from django.http import HttpResponse

current_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    html_template = "home.html"
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }

    return render(request, html_template, my_context)