# importing forms and models for using dgango's in-build forms
from django import forms
from home.models import TODO

class TODOForm(forms.ModelForm):
  class Meta:
    model = TODO
    fields = ["title", "status", "priority"]