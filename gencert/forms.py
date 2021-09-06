from django import forms
from gencert.models import CP, TC


class CpForm(forms.ModelForm):
    class Meta:
        model = CP
        fields = ['logo', 'language', 'documente_title', 'description',
                  'document_subject', 'company_name', 'student_name']


class TcForm(forms.ModelForm):
    class Meta:
        model = TC
        fields = ['logo', 'language', 'documente_title', 'description',
                  'document_subject', 'company_name', 'student_name']
