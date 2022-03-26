from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView
)
from .models import Post
from .forms import PhotoForm


class PostListView(ListView):
    template_name = "index.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = 'index.html'


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        profile = request.user.get_profile()
        # comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                # "comments": comments,
                "commented": False,
                "liked": liked,
                # "comment_form": CommentForm()
                "photo_form": PhotoForm(),
                "profile": profile
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        # comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # comment_form = CommentForm(data=request.POST)

        # if comment_form.is_valid():
        #     comment_form.instance.email = request.user.email
        #     comment_form.instance.name = request.user.username
        #     comment = comment_form.save(commit=False)
        #     messages.add_message( request, messages.SUCCESS, 'You comment has been posted!' )
        #     comment.post = post
        #     comment.save()
        # else:
        #     comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                # "comments": comments,
                "commented": True,
                "liked": liked,
                # "comment_form": CommentForm()
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

class AddPostView(View):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'