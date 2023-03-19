from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Post
import markdown
from django.template.defaultfilters import truncatechars_html


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog'

    def items(self):
        return Post.published.all()[0:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatechars_html(markdown.markdown(item.body), 300)

    def item_pubdate(self, item):
        return item.publish

