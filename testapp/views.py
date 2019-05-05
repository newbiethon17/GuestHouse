from django.shortcuts import get_object_or_404, render, redirect

from .models import Post
from .models import Member
from .forms import *

def index(request):
    
    # kw = request.POST['kw1']
    #kw = request.POST.get('kw1', '')
    #if kw=="":
    object_list = Post.objects.all()
    #else:
    #    object_list = Post.objects.all().filter(singer=kw)
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
        return redirect('index')
    '''
    member = Member.objects.all().filter(email=request.POST['email'])
    if len(member) == 1:
        if member[0].pwd == request.POST['pwd']:
            post = get_object_or_404(Post,id=pk)
            post.delete()
            Post.objects.
    return redirect('index')
    '''
    
def update(request, pk):
    post = get_object_or_404(Post,id=pk)
    if request.method == "GET":
        return render(request, 'post_form.html', {'post':post})
    else:
        form = PostForm(request.POST, instance=post)
        form.save()
        object_list = Post.objects.all()
        return redirect('index')
    
    
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
        return redirect('index')
    
def participate(request, pk):
    new_member = MemberForm(request.POST)
    post = get_object_or_404(Post,id=pk)
    
    if post.capacity > post.now_capacity:
        post.now_capacity = post.now_capacity+1
        post = post.save()   
        new_member = new_member.save()
        
        new_member.chosen_post = post  
        new_member.save()
        return redirect('index')
    else:
        
        return redirect('detail')
        
     
        
def unparticipate(request, pk):
    post = get_object_or_404(Post,id=pk)
    post.now_capacity = post.now_capacity -1
    post.save()
    '''
    member = Member.objects.filter(email=request.POST['email'])
    if member[0].pwd == request.POST['pwd']:
        post = get_object_or_404(Post,id=pk)
        post.now_capacity = post.now_capacity -1
        post.save()
        member[0].delete()
    '''
    return redirect('index')

def reserve(request):
    return render(request, 'reserve.html')
    
def reserve_house(request):
    return render(request, 'reserve_house.html')
    
def reserve_finish(request):
    return render(request, 'reserve_finish.html')
                   
                
    