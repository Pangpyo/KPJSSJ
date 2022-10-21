from pyexpat import model
from django import forms
from django import forms
from .models import Review, Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "댓글을 남겨보세요 💬",
        })
    )
    class Meta:
        model = Comment
        fields = ['content']