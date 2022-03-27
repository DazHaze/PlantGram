from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, DetailView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView
)
from .models import Post
from.forms import PostForm


class PostListView(ListView):
    template_name = "index.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = 'index.html'


class PostDetail(DetailView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        profile = request.user.profile
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "liked": liked,
                "profile": profile
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "commented": True,
                "liked": liked,
            },
        )

class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('plants:post_detail', args=[slug]))

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def post(self, request, *args, **kwargs):

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.author = request.user
            postform = post_form.save(commit=False)
            postform.save()
        else:
            post_form = PostForm()

        return render(
                request,
                "add_post.html",
                {
                    "post_form": PostForm()
                },
            )



