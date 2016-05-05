from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /song/
    url(r'^songs$', views.song_list, name='song_list'),
    # ex: /song/5/
    url(r'^song/(?P<song_id>[0-9]+)/$', views.song_detail, name='song_detail'),
    url(r'^song/(?P<song_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    # ex: /review/user - get reviews for the logged user
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
    # ex: /recommendation - get song recommendation for logged user
    url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),
]
