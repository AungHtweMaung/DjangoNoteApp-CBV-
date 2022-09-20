from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control my-3"}),
            "text": forms.Textarea(attrs={"class": "form-control my-3"}),
        }
        labels = {
            "text": "Write your toughts" # text နေရာမှာ ပေးတဲ့စာသားပေါ်မှာ
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']

    #     if 'Django' not in title:
    #         raise forms.ValidationError("We only accept notes about Django.")
    #     return title 