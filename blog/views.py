from datetime import date

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

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


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"posts": all_posts})


def post_detail(request, slug):
    # post = next(post for post in all_posts if post["slug"] == slug)
    post = get_object_or_404(Post, slug=slug)
    post_tags = post.tags.all()
    return render(
        request, "blog/post-detail.html", {"post": post, "post_tags": post_tags}
    )
