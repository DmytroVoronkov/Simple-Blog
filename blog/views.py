from datetime import date

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
