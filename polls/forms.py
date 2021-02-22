from django.db import models
from django import forms
from .models import Thought
from django.forms import ModelForm


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = '__all__'

