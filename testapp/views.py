from django.shortcuts import get_object_or_404, render, redirect

from .models import Post
from .models import Member
from .forms import *
from django.urls import reverse_lazy
from .starter import startpost
'''
def start(request):
    startpost()
    return redirect('home')

class PostList(ListView):
    model = Post
    template_name = 'home.html'
class PostCreate(CreateView):
    model = Post
    fields =  '__all__'
    template_name = 'post_form.html'
    success_url = reverse_lazy('home')
    
    
class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
  '''  
def index(request):
    object_list = Post.objects.all()
    return render(request, 'home.html', {'object_list':object_list})

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
        form.save()
        object_list = Post.objects.all()
        return render(request, 'home.html', {'object_list':object_list})