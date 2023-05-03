from main.models import Category
from main.forms import PostForm
def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

def post_form_processor(request):
    post_form = PostForm()
    return {'post_form':post_form}
