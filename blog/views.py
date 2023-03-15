from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import Post
from .forms import EmailPostForm


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page_number is out of range deliver last page
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )
    return render(request, 'blog/post/detail.html',
                  {'post': post})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'blog/post/list.html'
    paginate_by = 3


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id,
                             status=Post.Status.PUBLISHED)
    sent = False
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailPostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                (post.get_absolute_url()))
            subject = f"{cd['name']} recommends you to read" \
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']} \'s comments: {cd['comments']}"
            send_mail(subject, message, cd['email'],
                      [cd['to']],
                      fail_silently=False,)
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'form': form,
                                                    'post': post,
                                                    'sent': sent})

