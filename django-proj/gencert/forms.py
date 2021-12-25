# ******************************************************************************
#  Copyright (c) 2021 Nurul-GC.                                                *
# ******************************************************************************

from django import forms
from gencert.models import CP, TC


class CpForm(forms.ModelForm):
    class Meta:
        model = CP
        fields = ['logo', 'language', 'document_title', 'document_subject',
                  'company_name', 'student_name', 'description']


class TcForm(forms.ModelForm):
    class Meta:
        model = TC
        fields = ['logo', 'language', 'document_title', 'document_subject',
                  'company_name', 'student_name', 'course_name', 'description']
