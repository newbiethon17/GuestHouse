from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Post
from django.urls import reverse_lazy
from .starter import startpost

def start(request):
    startpost()
    return redirect('home')

class PostList(ListView):
    model = Post
    template_name = 'home.html'
class PostCreate(CreateView):
    model = Post
    fields =  '__all__'
    template_name = 'Post_form.html'
    success_url = reverse_lazy('home')
class PostDetail(DetailView):
    model = Post
    template_name = 'Post_detail.html'
class PostUpdate(UpdateView):
    model = Post
    fields =  '__all__'
    template_name = 'Post_form.html'
    success_url = reverse_lazy('home')
class PostDelete(DeleteView):
    model = Post
    template_name = 'Post_delete.html'
    success_url = reverse_lazy('home')