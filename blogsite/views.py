from django.shortcuts import render

from accounts.models import User
from blog.models import Post, Comment

def home(request):
    num_users = User.objects.count()
    num_posts = Post.objects.count()
    
    context = {
        'num_users':num_users,
        'num_posts':num_posts,
    }

    return render(request, 'home.html', context=context)