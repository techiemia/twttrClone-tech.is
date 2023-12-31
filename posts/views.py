from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/")

        else:
            return HttpResponseRedirect(form.errors.as_json)

    posts = Post.objects.all()[:20]

    return render(request, "post.html", {"posts": posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'edit.html', {'posts': post})

    if request.method == 'POST':
        editPosts = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=editPosts)
        
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/")
        else:
            return HttpResponse('Form is not valid')

def like(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes +1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')