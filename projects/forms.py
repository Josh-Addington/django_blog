from django.forms import ModelForm, Textarea
from .models import Project

class ProjectForm(ModelForm):

        class Meta:
                model = Project
                fields = ('title', 'content', 'preview', 'code', 'js')
                widgets = {
                        'js': Textarea(attrs={'cols': 40, 'rows': 5}),
                }
