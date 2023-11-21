from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Post Title'}),
            'author': forms.TextInput(attrs={'readonly': 'readonly'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Content of the Post'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
