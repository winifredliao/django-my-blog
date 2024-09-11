from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "My-Dinner",
        "image": "swords.png",
        "author": "Winifred",
        "date": date(2024, 9, 11),
        "title": "My Dinner",
        "excerpt": "Curry is the best!",
        "content":"""
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem recusandae excepturi cumque deleniti odio quae. Sint sapiente, eaque velit explicabo nam libero fugit amet ullam repudiandae facere sed dolor perspiciatis.
        """
    },
    {
        "slug": "My-Work",
        "image": "cat.jpg",
        "author": "Winifred",
        "date": date(2024, 9, 11),
        "title": "My Work",
        "excerpt": "Curry is the best!",
        "content":"""
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem recusandae excepturi cumque deleniti odio quae. Sint sapiente, eaque velit explicabo nam libero fugit amet ullam repudiandae facere sed dolor perspiciatis.
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem recusandae excepturi cumque deleniti odio quae. Sint sapiente, eaque velit explicabo nam libero fugit amet ullam repudiandae facere sed dolor perspiciatis.
        """
    },
    {
        "slug": "My-Friend",
        "image": "house.jpg",
        "author": "Winifred",
        "date": date(2024, 9, 11),
        "title": "My Friend",
        "excerpt": "Curry is the best!",
        "content":"""
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem recusandae excepturi cumque deleniti odio quae. Sint sapiente, eaque velit explicabo nam libero fugit amet ullam repudiandae facere sed dolor perspiciatis.
        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "posts/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "posts/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "posts/post-detail.html", {
        "post": identified_post
    })