from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import CommentForm
# Create your views here.


def index(request):
    return render(request, "articles/index.html")

def comment_create(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.save()
    return redirect('articles:index')


def comment_delete(request, review_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('articles:index')
    