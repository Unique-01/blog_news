from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='index'),
    path('myadmin/',views.myAdmin,name='myadmin'),
    path('search/',views.search,name='search'),
    path('pagination/',views.PostPagination.as_view(),name='postpagination'),
    path('category/<str:name>/',views.get_category_post,name='categorypost'),
    path('<int:id>/<slug:slug>/',views.post_detail,name='post_detail'),
]
