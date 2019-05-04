from django.shortcuts import get_object_or_404, render, redirect

from .models import Post
from .models import Member
from .forms import *

def index(request):
    object_list = Post.objects.all()
    return render(request, 'home.html', {'object_list':object_list})

def detail(request, pk):
    post = get_object_or_404(Post,id=pk)
    return render(request, 'post_detail.html', {'post':post})

def delete(request, pk):
    post = get_object_or_404(Post,id=pk)
    if request.method == "GET": 
        return render(request, 'post_delete.html', {'post':post})
    else:
        post.delete()
        object_list = Post.objects.all()
        return render(request, 'home.html', {'object_list':object_list})
    
def update(request, pk):
    post = get_object_or_404(Post,id=pk)
    if request.method == "GET":
        return render(request, 'post_form.html', {'post':post})
    else:
        form = PostForm(request.POST, instance=post)
        form.save()
        object_list = Post.objects.all()
        return render(request, 'home.html', {'object_list':object_list})
    
    
def create(request):
    if request.method == "GET":
        return render(request, 'post_create.html')
    else:
        form = PostForm(request.POST)
        form_pk = form.save()
        
        new_member = Member()
        new_member.email = request.POST['owner_email']
        new_member.number = request.POST['owner_number']
        new_member.pwd = request.POST['owner_pwd']
        new_member.chosen_post = form_pk
        new_member.save()
        
        object_list = Post.objects.all()
        return render(request, 'home.html', {'object_list':object_list})