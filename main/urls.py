from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='index'),
    path('myadmin/',views.myAdmin,name='myadmin'),
    path('search/',views.search,name='search'),
    path('past_questions/',views.PastQuestionList.as_view(),name='past_question_list'),
    path('pagination/',views.PostPagination.as_view(),name='postpagination'),
    path('category/<str:name>/',views.get_category_post,name='categorypost'),
    path('update_post/<slug:slug>/',views.PostUpdate.as_view(),name='post_update'),
    path('delete_post/<slug:slug>/',views.PostDelete.as_view(),name='post_delete'),
    path('<slug:slug>/<int:id>/',views.post_detail,name='post_detail'),
    
    
    # path('', include('social_share.urls')),
]
