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
from.forms import PostForm

class LandingView(ListView):
    queryset = Post.objects
    context_object_name = "landing"
    template_name = "index.html"

class PostListView(ListView):
    queryset = Post.objects.order_by('-created_on')
    context_object_name = "posts"
    template_name = 'list_view.html'


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
        if request.method == 'POST':
            post_form = PostForm(request.POST, request.FILES)

            if post_form.is_valid():
                post_form.instance.author = request.user
                postform = post_form.save(commit=False)
                postform.save()

            return HttpResponseRedirect(reverse('plants:list_view'))



