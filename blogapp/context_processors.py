from main.models import Category,Post
from main.forms import PostForm,CategoryForm

def custom_processor(request):
    categories = Category.objects.all()
    post_form = PostForm()
    categoryform = CategoryForm()
    general_post = Post.objects.all()
    return {'categories': categories,'post_form':post_form,'categoryform':categoryform}

