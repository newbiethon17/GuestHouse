from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('owner_email', 'owner_number', 'concert_name', 'singer','concert_date', 'post_date',     'owner_pwd', 'now_capacity', 'capacity', 'description')