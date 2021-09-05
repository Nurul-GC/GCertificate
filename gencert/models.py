from django.db import models


# Create your models here.
class Certificate(models.Model):
    TYPES = (('Certificado de Formação', 'Certificado de Formação'),
             ('Certificado de Participação', 'Certificado de Participação'))
    logo = models.ImageField()
    title = models.CharField(max_length=50)
    type = models.CharField(choices=TYPES)
    company = models.CharField(max_length=50)
    student = models.CharField(max_length=50)
