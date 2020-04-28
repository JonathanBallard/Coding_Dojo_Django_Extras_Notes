
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    # content = forms.CharField(max_length=1000)
    class Meta:
        model = Note
        fields = '__all__'








