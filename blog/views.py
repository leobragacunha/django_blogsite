from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = blog_models.Comment
    fields = ['comment']
    template_name = "blog/comment_form.html"

    def get_context_data(self, **kwargs: Any):
        context = super(CommentCreateView,self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(blog_models.Post, pk = self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        form.instance.comment_blogger = self.request.user
        form.instance.post = get_object_or_404(blog_models.Post, pk = self.kwargs['pk'])
        form.save()
        return super(CommentCreateView,self).form_valid(form)
    

class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = blog_models.Comment
    fields = ["comment"]
    template_name = "blog/comment_form.html"

    def get_context_data(self, **kwargs):
        context = super(CommentUpdateView,self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(blog_models.Post, pk = self.kwargs['postpk'])
        context['comment'] = self.get_object()
        return context


class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = blog_models.Comment
    template_name = 'blog/comment_confirm_delete.html'

    def form_valid(self, form):
        self.object = self.get_object()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'pk':self.object.post.id})


class PostPerUserView(LoginRequiredMixin, generic.ListView):
    model = blog_models.Post 
    template_name = "blog/post_per_user.html"

    def get_queryset(self):
        return blog_models.Post.objects.filter(blogger = self.request.user).order_by('-updated_date')