from django.urls import path

from twitter.views import Tweets, TweetCreate

urlpatterns = [
    path('', Tweets.as_view(), name='tweets'),
    path('new/', TweetCreate.as_view(), name='tweet_create'),
]
