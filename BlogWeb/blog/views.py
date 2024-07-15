from typing import Any
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.urls import reverse


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin

def about(request):
    return render(request, 'blog/about.html',{"title":"Blog-About"})
    
def LikeView(request,pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    
    return HttpResponseRedirect(reverse( 'blog-detail',args=[str(pk)]))

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name='blog/home.html'
    
    context_object_name='posts'
    ordering = ["date_posted"]   #this code orders posts by time posted from top to down(recent top )

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post

    def get_context_data(self, *args, **kwargs):
        context=super(PostDetailView,self).get_context_data()
        stuff=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["total_likes"]= total_likes
        context["liked"] = liked
        return context
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

