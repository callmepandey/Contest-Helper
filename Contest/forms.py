from django import forms
from .models import MyContest
class ContestForm(forms.ModelForm):
    class Meta:
        model = MyContest
        fields = ['contestName','dateTime','platform','contestLink']
