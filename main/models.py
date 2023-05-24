from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.shortcuts import reverse

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = RichTextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='postImg/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    status = models.IntegerField(choices = STATUS,default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.id,"slug":self.slug})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comment')
    comment = models.TextField()
    name = models.CharField(max_length=500)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}-{self.comment[:10]}'

class PastQuestion(models.Model):
    description = models.CharField(max_length=200)
    document = models.FileField(upload_to="past_questions")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
    
    





