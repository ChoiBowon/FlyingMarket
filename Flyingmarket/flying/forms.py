from django import forms
from .models import Flying
from django.utils import timezone

class FlyingUploadForm(forms.ModelForm):
    class Meta:
        model = Flying
        fields = '__all__'
        exclude = ['is_matched', 'user']
        widgets = {
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget(),
        }