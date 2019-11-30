from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('Event_Title', 'Organised_By', 'pdf', 'cover')
