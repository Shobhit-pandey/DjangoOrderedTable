from django import forms
import django_tables2 as tables

from orderedtable.models import Project

CHOICE = (
    ('distance', 'distance'),
    ('rate', 'rate'),
    ('project_size', 'project_size'),
    ('completion_date', 'completion_date'),
)


class ImportJson(forms.Form):
    json = forms.FileField(required=True)


class ProjectTable(tables.Table):
    class Meta:
        model = Project


class Choice(forms.Form):
    ch1 = forms.ChoiceField(choices=CHOICE,required=True)
    ch2 = forms.ChoiceField(choices=CHOICE, required=True)
    ch3 = forms.ChoiceField(choices=CHOICE, required=True)
    ch4 = forms.ChoiceField(choices=CHOICE, required=True)