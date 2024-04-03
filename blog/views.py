from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts import models as acc_models
from . import models as blog_models

# Create your views here.

class BloggersListView(generic.ListView):
    model = acc_models.User
    template_name = 'blog/blogger_list.html'
    context_object_name = 'blogger_list'
    paginate_by = 10
    

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(BloggersListView, self).get_context_data(**kwargs)
        context["num_bloggers"] = acc_models.User.objects.all().count()
        # NICE TO HAVE: NUMBER OF POSTS PER USER

        return context


class BloggerDetailView(generic.DetailView):
    model = acc_models.User
    template_name = 'blog/blogger_detail.html'
    context_object_name = 'blogger'


class PostListView(generic.ListView):
    model = blog_models.Post

    def get_queryset(self):
        return blog_models.Post.objects.order_by('-created_date')


class PostDetailView(generic.DetailView):
    model = blog_models.Post


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = blog_models.Post
    fields = ['title', 'content']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.blogger = self.request.user
        post.save()
        return redirect('blog:posts')    


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = blog_models.Post
    fields = ['title', 'content']


class PostDeleteView(LoginRequiredMixin ,generic.DeleteView):
    model = blog_models.Post
    success_url = reverse_lazy('blog:posts')


class CommentCreateView(generic.CreateView):
    pass


class CommentUpdateView(generic.UpdateView):
    pass


class CommentDeleteView(generic.DeleteView):
    pass