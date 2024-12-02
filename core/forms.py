from django import forms
from .models import File, DataItem

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file_name', 'file']

class DataItemForm(forms.ModelForm):
    class Meta:
        model = DataItem
        fields = ['title', 'description', 'user'] 

