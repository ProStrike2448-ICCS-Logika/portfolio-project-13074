from django.forms import BaseModelForm
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get(self, request: HttpRequest, *args, **kwargs):
        super().get(request)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX
            return render(request, 'blog/post_list.html', context=self.get_context_data())
        return render(request, self.template_name, context=self.get_context_data())


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form: BaseModelForm):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/post_update_form.html'


class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
