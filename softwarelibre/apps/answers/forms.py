from django import forms
from apps.tagging.forms import TagField

class QuestionForm(forms.Form):
    title = forms.CharField(max_lenght = 100)
    question = forms.CharField(widget = forms.Textarea)
    tags = TagField()

class AnswerForm(forms.Form):
    answer = forms.CharField(widget = forms.Textarea)

