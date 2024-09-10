from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "posts/index.html")

def posts(request):
    return render(request, "posts/all-posts.html")

def post_detail(request):
    pass