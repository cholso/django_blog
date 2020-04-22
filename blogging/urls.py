from django.urls import path
# from blogging.views import stub_view
from blogging.views import list_view, detail_view, add_post
from blogging.feeds import LatestEntriesFeed 


urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    # path('posts/<int:post_id>/', stub_view, name="blog_detail"),
    path('posts/', add_post, name='add_post'),
    path('latest/feed/', LatestEntriesFeed()),
]
