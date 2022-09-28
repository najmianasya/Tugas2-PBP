from django import forms

class NewTaskForm(forms.Form):
    title = forms.CharField(label='Judul Task:', widget=forms.TextInput(attrs={'placeholder': 'Judul Task Baru'}))
    description = forms.CharField(label="Deskripsi Task:", widget=forms.Textarea(attrs={'placeholder': 'Deskripsi Task Baru'}))
