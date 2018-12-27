from django.views import generic

from twitter.models import Post


class all_posts(generic.ListView):
    template_name = 'allPosts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.filter(deleted=False)

