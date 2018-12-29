from rest_framework import serializers

from twitter.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tweet
        fields = ('title', 'content', 'owner')
