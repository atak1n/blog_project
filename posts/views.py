# миксин для валидации логина
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    DeleteView,
    ListView,
    UpdateView
)
from django.urls import reverse_lazy

from .models import Post


class PostNewView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'posts/post_edit.html'
    fields = ('title', 'body')
    context_object_name = 'post'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    login_url = 'login'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'


class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts_list'
    # login_url = 'login'






