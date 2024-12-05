import markdown
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Post
from .forms import CommentForm

class StartingPageView(ListView):
    template_name = "posts/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = "posts/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class SinglePostView(DetailView):
    template_name = "posts/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        identified_post = context["post"]
        context["post_content_html"] = markdown.markdown(
            identified_post.content, extensions=["fenced_code", "codehilite"]
        )
        context["post_tags"] = identified_post.tags.all()
        context["comment_form"] = CommentForm()
        return context