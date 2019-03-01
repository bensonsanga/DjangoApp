from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'community/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'community/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


class UserPostListView(ListView):
    model = Post
    template_name = 'community/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/community/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'community/about.html', {'title': 'about'})


def entourage(request):
    return render(request, 'community/entourage.html', {'title': 'entourage'})


def tutorials(request):
    return render(request, 'community/tutorials.html', {'title': 'tutorials'})


def dwg(request):
    return render(request, 'community/dwg.html', {'title': 'dwg'})


def scripts(request):
    return render(request, 'community/scripts.html', {'title': 'scripts'})


def models(request):
    return render(request, 'community/models.html', {'title': 'models'})


def icons(request):
    return render(request, 'community/icons.html', {'title': 'icons'})


def maps(request):
    return render(request, 'community/maps.html', {'title': 'maps'})
