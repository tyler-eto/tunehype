from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review, Song
import datetime


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list': latest_review_list, 'username': username}
    return render(request, 'reviews/user_review_list.html', context)


def song_list(request):
    song_list = Song.objects.order_by('-name')
    context = {'song_list': song_list}
    return render(request, 'reviews/song_list.html', context)


def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    form = ReviewForm()
    return render(request, 'reviews/song_detail.html', {'song': song, 'form': form})


@login_required
def add_review(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = request.user.username
        tags = form.cleaned_data['tags']
        review = Review()
        review.tags = tags
        review.song = song
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect(reverse('reviews:song_detail', args=(song.id,)))

    return render(request, 'reviews/song_detail.html', {'song': song, 'form': form})
