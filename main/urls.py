from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='index'),
    path('myadmin/',views.myAdmin,name='myadmin'),
    path('search/',views.search,name='search'),
    path('<int:id>/<slug:slug>/',views.post_detail,name='post_detail')
]
