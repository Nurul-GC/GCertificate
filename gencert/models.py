from django.db import models


# Create your models here.
class Certificate(models.Model):
    LANG = (
        ('English', 'English'),
        ('Português', 'Português')
    )
    TYPES = (
        ('Training Certificate', 'Training Certificate'),
        ('Certificado de Formação', 'Certificado de Formação'),
        ('Certificado de Participação', 'Certificado de Participação'),
        ('Certificate of Participation', 'Certificate of Participation')
    )
    logo = models.ImageField()
    language = models.CharField(choices=LANG)
    document_title = models.CharField(max_length=50)
    document_type = models.CharField(choices=TYPES)
    company_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.student_name} certified by {self.company_name}"
