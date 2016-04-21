from django.forms import ModelForm, Textarea
from reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment', 'tags']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
            'tags': Textarea(attrs={'cols': 40, 'rows': 1})
        }
