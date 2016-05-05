from django.contrib import admin

from models import Song, Review, Cluster


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('song', 'rating', 'user_name', 'comment', 'tags', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment', 'tags']


class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    list_display = ['name', 'get_members']

admin.site.register(Song)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cluster, ClusterAdmin)
