from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from twitter.models import Tweet


class Tweets(LoginRequiredMixin, ListView):
    template_name = 'Tweet.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Tweet.objects.filter(deleted=False)


class TweetCreate(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = ['title', 'content']
    template_name = 'createTweet.html'

    def form_valid(self, form):
        post = Tweet()
        post.owner = self.request.user
        post.content = form.cleaned_data['content']
        post.title = "title"
        post.save()

        messages.success(self.request, 'Tweet was successfully created.')

        return redirect('tweet_create')
