from django import forms
from social_app.models import post

class post_upload_form(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title','photo1','photo2','photo3','body']