from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /song/
    url(r'^song$', views.song_list, name='song_list'),
    # ex: /song/5/
    url(r'^song/(?P<song_id>[0-9]+)/$', views.song_detail, name='song_detail'),
    url(r'^song/(?P<song_id>[0-9]+)/add_review/$', views.add_review, name='add_review')
]
