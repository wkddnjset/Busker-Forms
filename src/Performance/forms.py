from django import forms
from .models import *

class Performs(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Performs, self).__init__(*args, **kwargs)
        self.fields['start_time'].label = "시작시간"
        self.fields['end_time'].label = "종료시간"
        self.fields['place'].label = "장소"

    class Meta:
        model = Performance
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
            }),
            'start_time': forms.TimeInput(format='%H:%M', attrs={
                'class': 'form-control',
            }),
            'end_time': forms.TimeInput(format='%H:%M', attrs={
                'class': 'form-control',
            })
        }