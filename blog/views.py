from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm
def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'index.html',context=my_dict)

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    
