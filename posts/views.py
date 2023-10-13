from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.urls import reverse

# Create your views here.
def viwe_posts(request):
    objects = Post.objects.all()
    return render(request, 'posts/posts.html',{'posts':objects})

def view_detail(request,id):
    single_post = Post.objects.get(id=id)
    return render(request, 'posts/post_detail.html',{'post':single_post})

def view_form(request):
    if request.method == 'POST' :
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.auther = request.user
            myForm.save()
            return redirect(reverse('blog:view_posts'))
    else:
        form = PostForm()
    return render(request, 'posts/form.html',{'form':form})

def edit_post(request,id):
    single_post = Post.objects.get(id=id)
    if request.method == 'POST' :
        form = PostForm(request.POST, request.FILES, instance=single_post) 
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=single_post)
    return render(request, 'posts/edit.html',{'form':form})  

def delete_post(request,id):
    single_post = Post.objects.get(id=id)
    single_post.delete()
    return redirect(reverse('blog:view_posts'))
    
