from django.contrib import admin
from .models import Post,Category,PastQuestion
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PastQuestion)
