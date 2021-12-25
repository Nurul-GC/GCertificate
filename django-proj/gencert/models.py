# ******************************************************************************
#  Copyright (c) 2021 Nurul-GC.                                                *
# ******************************************************************************

from django.db import models


# Create your models here.
class CP(models.Model):
    """certificate of perticipation model"""
    LANG = (
        ('English', 'English'),
        ('Português', 'Português')
    )
    TYPES = (
        ('Certificado de Participação', 'Certificado de Participação'),
        ('Certificate of Participation', 'Certificate of Participation')
    )
    logo = models.FileField(upload_to=f'media/logos/')
    language = models.CharField(choices=LANG, max_length=10, help_text='Escolha o idioma do certificado!')
    document_title = models.CharField(max_length=50, help_text='Digite um titulo para o documento!')
    document_subject = models.CharField(choices=TYPES, max_length=30, help_text='Escolha o tema do certificado!')
    company_name = models.CharField(max_length=50, help_text='Digite o nome da instituição emissora!')
    student_name = models.CharField(max_length=50, help_text='Digite o nome do estudante!')
    description = models.TextField(max_length=1000, help_text='Digite o conteudo descritivo e motivo desta certificação!')

    def __str__(self):
        return f"{self.student_name.name} certified by {self.company_name.name}"


class TC(models.Model):
    """training certificate model"""
    LANG = (
        ('English', 'English'),
        ('Português', 'Português')
    )
    TYPES = (
        ('Training Certificate', 'Training Certificate'),
        ('Certificado de Formação', 'Certificado de Formação'),
    )
    logo = models.FileField(upload_to=f'media/logos/')
    language = models.CharField(choices=LANG, max_length=10, help_text='Escolha o idioma do certificado!')
    document_title = models.CharField(max_length=50, help_text='Digite um titulo para o documento!')
    document_subject = models.CharField(choices=TYPES, max_length=30, help_text='Escolha o tema do certificado!')
    company_name = models.CharField(max_length=50, help_text='Digite o nome da instituição emissora!')
    student_name = models.CharField(max_length=50, help_text='Digite o nome do estudante!')
    course_name = models.CharField(max_length=50, help_text='Digite o nome do curso!')
    description = models.TextField(max_length=1000, help_text='Digite o conteudo descritivo e motivo desta certificação!')

    def __str__(self):
        return f"{self.student_name.name} certified by {self.company_name.name}"
