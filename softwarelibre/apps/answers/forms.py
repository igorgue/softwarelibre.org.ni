from django import forms
from apps.tagging.forms import TagField

class QuestionForm(forms.Form):
    title = forms.CharField()
    question = forms.CharField(widget = forms.Textarea)
    tags = TagField()

class AnswerForm(forms.Form):
    answer = forms.CharField(widget = forms.Textarea)

