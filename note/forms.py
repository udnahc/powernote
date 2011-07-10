from django import forms 
from note.models import NoteCategory

def note_categories():
    return [ (category.get('id'),category.get('name')) for category in NoteCategory.objects.values('name','id') ]


class NotePropertyForm(forms.Form):
    note_description = forms.CharField(required=True, widget=forms.Textarea)
    note_status = forms.CharField(required=True, widget=forms.TextInput())
    note_category = forms.ChoiceField(required=False,choices = note_categories() ,label='Note Category')
    
    show_ticket  = forms.BooleanField(required=False)
    active = forms.BooleanField(required=False)
