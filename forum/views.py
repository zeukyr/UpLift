from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import postForm, postComment


class ucalgaryView(ListView):
    model = Post
    template_name = "forum/Ucalgary.html"
    ordering = ['-post_date']


class ucalgaryDetailView(DetailView):
    model = Post
    template_name = "forum/Ucalgary_details.html"


class createPostView(CreateView):
    model = Post
    form_class = postForm
    template_name = "forum/create_post.html"

class createCommentView(CreateView):
    model = Comment
    form_class = postComment
    template_name = "forum/Create_comment.html"
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)