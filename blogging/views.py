from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm


def about(request):
        return render(request, 'about.html')


def contact(request):
        return render(request, 'contact.html')


def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST or None)
        if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect(request.path)
        return render(request, 'blog/post_detail.html', {'post': post, 'form': form})


@login_required
def post_new(request):
        if request.method == "POST":
                form = PostForm(request.POST)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.author = request.user
                        post.save()
                        return redirect('blogging.views.post_detail', pk=post.pk)
        else:
                form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
                form = PostForm(request.POST, instance=post)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.author = request.user
                        post.save()
                        return redirect('blogging.views.post_detail', pk=post.pk)
        else:
                form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
        posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
        return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.publish()
        return redirect('blogging.views.post_detail', pk=pk)


@login_required
def post_delete(request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('blogging.views.post_list')
