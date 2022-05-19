from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from cloudinary.forms import cl_init_js_callbacks

from django.views.generic import (
    ListView
)
from .models import Post
from.forms import PostForm, CommentForm


class LandingView(ListView):
    queryset = Post.objects
    context_object_name = "landing"
    template_name = "index.html"


class PostListView(ListView):
    queryset = Post.objects.order_by('-created_on')
    context_object_name = "posts"
    template_name = 'list_view.html'

    def comment_view(self,request, slug):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST or None)
            if comment_form.is_valid():
                content = request.POST.get('content')
                comment.objects.create(post=post, user=request.user, content=content)
                comment.save()
                return HttpResponseRedirect('plants: list_view')
                    
        else:
            comment_form = CommentForm()
        return render(request, 'plants: list_view', {
            'comments': comments,
        })


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
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
        if request.method == 'POST':
            post_form = PostForm(request.POST, request.FILES)

            if post_form.is_valid():
                post_form.instance.author = request.user
                postform = post_form.save(commit=False)
                postform.save()

            return HttpResponseRedirect(reverse('plants:list_view'))
