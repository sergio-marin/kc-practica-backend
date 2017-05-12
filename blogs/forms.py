from django import forms

from blogs.models import Post


class NewPostForm(forms.ModelForm):

    class Meta:
            model = Post
            fields = ["title", "introduction", "body", "media_url", "categories"]