from django.shortcuts import render
from blog.models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView)
from blog.forms import PostForm, CommentForm
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


class PostlistView(ListView):
    model = Post 

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUbdateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post