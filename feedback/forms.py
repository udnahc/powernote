from django import forms

class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':200}),
                        initial="Replace with your feedback")

