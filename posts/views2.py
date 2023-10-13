from .models import Post
from django.views import generic

class Postlist(generic.ListView):
    model = Post

class PostDetail(generic.DetailView):
    model = Post

class AddPost(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url = '/blog/'

class EditPost(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/blog/'
    template_name = 'posts/edit.html'

class DeletePost(generic.DeleteView):
    model = Post
    success_url = '/blog/'
    