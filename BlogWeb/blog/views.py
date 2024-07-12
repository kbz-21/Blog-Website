from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin



# Create your views here.
# def home(request):
#     context = {
#         'posts':Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)  

def about(request):
    return render(request, 'blog/about.html',{"title":"Blog-About"})

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name='blog/home.html'
    
    context_object_name='posts'
    ordering = ["date_posted"]   #this code orders posts by time posted from top to down(recent top )

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_fun(self):
        post = self.get_object()
        if self.request.user==post.author:
            return True
        return False    

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_fun(self):
        post = self.get_object()
        if self.request.user==post.author:
            return True
        return False
class PostDeleteView(DeleteView):
    model=Post
    success_url = '/'
    def test_fun(self):
        post = self.get_object()
        if self.request.user==post.author:
            return True
        return False
    

    
    


        


