from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post 

class LatestEntriesFeed(Feed):
    title = "My Cool Blog"
    link = "/latest/feed/"
    description = "My innermost thoughts, published."



    def items(self):
        return Post.objects.order_by('published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description 

    # only needed if Post has no get_absolute_url method
    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk]
