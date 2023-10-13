from django.urls import path
from posts.views import viwe_posts, view_detail, view_form ,edit_post, delete_post
from posts.views2 import Postlist, PostDetail, AddPost, EditPost, DeletePost

app_name='posts'

urlpatterns = [
    path('', Postlist.as_view() ,name='view_posts'),
    path('<int:pk>', PostDetail.as_view(), name='details'),
    path('form', AddPost.as_view(), name='new_post'),
    path('<int:pk>/edit', EditPost.as_view(), name='edit'),
    path('<int:pk>/delete', DeletePost.as_view(), name='delete'),
]


