from datetime import date

from django.shortcuts import render, get_object_or_404

from .models import Post


def get_date(post):
    return post["date"]


# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"posts": all_posts})


def post_detail(request, slug):
    # post = next(post for post in all_posts if post["slug"] == slug)
    post = get_object_or_404(Post, slug=slug)
    post_tags = post.tags.all()
    return render(request, "blog/post-detail.html", {"post": post, "post_tags": post_tags})
