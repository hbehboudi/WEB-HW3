from django.urls import path

from twitter.views import all_posts

urlpatterns = [
    path('', all_posts.as_view(), name='get_all_posts'),
]
