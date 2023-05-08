from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Category
from django.contrib import messages


class HomePage(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-updated')
    template_name = 'index.html'
    paginate_by = 10


class PostPagination(HomePage):
    template_name = 'postpagination.html'

def get_category_post(request,name):
    category = Category.objects.get(name=name)
    posts = Post.objects.filter(category=category)
    return render(request,'categorypost.html',{'posts':posts})

def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    comment = post.comment.all()
    try:
        next_post = Post.objects.get(id=post.id + 1)
    except:
        next_post = None

    try:
        prev_post = Post.objects.get(id=post.id - 1)
    except:
        prev_post = None
    comment_form = CommentForm()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

        return redirect('post_detail',id=id,slug=slug)

    context = {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
        'comment_form': comment_form,
        'new_comment': new_comment,
        'comment':comment
    }
    return render(request, 'post-detail.html', context)


def search(request):
    query = request.GET.get('q')
    if query:
        queryset = Post.objects.filter(
            Q(status=1) & (Q(title__icontains=query)
                           | Q(content__icontains=query))).order_by('-updated')
    else:
        queryset = Post.objects.filter(status=1).order_by('-updated')
    context = {'queryset': queryset}
    return render(request, 'search.html', context)


@login_required()
def myAdmin(request):
    posts = Post.objects.all().order_by('-updated')
    form = PostForm()
    categoryform = CategoryForm()
    category = Category.objects.all()
    if request.method == 'POST':
        categoryform = CategoryForm(request.POST)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            messages.success(request, "Post has been added successfully")
            return redirect('myadmin')

        if categoryform.is_valid():
            categoryform.save()
            messages.success(request, "category has been added successfully")
            return redirect('myadmin')

    context = {'posts': posts, 'form': form,'categoryform':categoryform,'category':category}
    return render(request, 'myadmin.html', context)


class PostUpdate(generic.UpdateView):
    model = Post
    template_name = "post_update.html"
    form_class = PostUpdateForm
    

class PostDelete(generic.DeleteView):
    model =Post
    template_name = 'post_delete.html'