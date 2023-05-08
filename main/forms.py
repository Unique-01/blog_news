from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post, Comment,Category


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'category', 'title', 'content', 'status']
        widgets = {
            'content': CKEditorWidget(),
        }

class PostUpdateForm(PostForm):
    content = forms.CharField(widget=CKEditorWidget(attrs={'id':'content_update'}))
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].label = ""
        self.fields['name'].label = ""
        self.fields['email'].label = ""

    class Meta:
        model = Comment
        fields = ['comment', 'name', 'email']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': "Your Comment"}),
            'name': forms.TextInput(attrs={'placeholder': "Name"}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'})
        }