from django.forms import ModelForm
from .models import *


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']
