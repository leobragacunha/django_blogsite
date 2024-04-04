from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # LIST AND DETAIL VIEWS
    path("posts/", views.PostListView.as_view(), name='posts'),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name='post-detail'),
    path("bloggers/", views.BloggersListView.as_view(), name='bloggers'),
    path("blogger/<int:pk>", views.BloggerDetailView.as_view(), name='blogger-detail'),
    path("blogger/<int:pk>/posts/", views.PostPerUserView.as_view(), name='blogger-posts'),
    # CRUD VIEWS
    path("post/new/", views.PostCreateView.as_view(), name='post-new'),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post-delete'),
]
