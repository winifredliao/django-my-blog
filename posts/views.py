from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "posts/index.html")

def posts(request):
    pass

def post_detail(request):
    pass