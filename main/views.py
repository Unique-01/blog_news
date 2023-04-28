from django.shortcuts import render, redirect,get_object_or_404
from django.views import generic
from .models import *
from .forms import *
from django.db.models import Q


class HomePage(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-updated')
    template_name = 'index.html'
    paginate_by = 5

    # def get_queryset(self):
    #     query=self.request.GET.get('q')
    #     if query:
    #         queryset = Post.objects.filter(Q(status=1) & (Q(title__icontains=query) | Q(content__icontains = query) | Q(category__icontains=query))).order_by('-updated')
    #     else:
    #         queryset = Post.objects.filter(status=1).order_by('-updated')


def post_detail(request,id,slug):
    post = get_object_or_404(Post,id=id,slug=slug)
    next_post = Post.objects.get(id=post.id+1)
    prev_post = Post.objects.get(id=post.id-1)

    context = {
        'post':post,
        'next_post':next_post,
        'prev_post':prev_post,
    }
    return render(request,'post-detail.html',context)

def search(request):
    query = request.GET.get('q')
    search_result = None
    if query:
        search_result= Post.objects.filter(Q(status=1) & (Q(title__icontains=query) | Q(content__icontains = query))).order_by('-updated')
    return render(request,'search.html',{'search_result':search_result})


    

def myAdmin(request):
    posts = Post.objects.all().order_by('-updated')
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            return redirect('myadmin')
    context = {'posts': posts, 'form': form}
    return render(request, 'myadmin.html', context)
