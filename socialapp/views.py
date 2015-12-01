from django.shortcuts import render, redirect
from django.http import HttpResponse

from socialapp.models import UserPost, UserPostComment
from socialapp.forms import UserPostForm, CommentPostForm


def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.order_by('-date_added')
        form = UserPostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = UserPost(text=text)
            user_post.save()
        return redirect('index')


def post_details(request, pk):
    
    post = UserPost.objects.get(pk=pk)
    if request.method == 'GET':
        form = CommentPostForm()
        comments=UserPostComment.objects.filter(post=post).order_by('-date_added')

        context = {
            'post': post,
            'form':form,
            'comments':comments,
        }
        
        #return HttpResponse(UserPostComment.objects.get(post=post)) #
        return render(request, 'post_details.html', context)

    elif request.method == 'POST':
        form = CommentPostForm(request.POST)

        
        if form.is_valid():
            text = form.cleaned_data['text']
            user_comment = UserPostComment(text=text, post=post)
            user_comment.save()
        return redirect('/post/'+str(post.pk))
