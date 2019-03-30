from django import forms
from app import models


class articleForm(forms.ModelForm):
    class Meta:
        model = models.article
        fields="__all__"

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     for name,field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
    #         field.widget.attrs['placeholder'] = field.label