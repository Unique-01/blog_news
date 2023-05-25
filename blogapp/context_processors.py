from main.models import Category,Post
from main.forms import PostForm,CategoryForm,PastQuestionForm

def custom_processor(request):
    categories = Category.objects.all()
    post_form = PostForm()
    categoryform = CategoryForm()
    general_post = Post.objects.all()
    past_question_form = PastQuestionForm()

    return {'categories': categories,'post_form':post_form,'categoryform':categoryform,'general_post':general_post,'past_question_form':past_question_form}

