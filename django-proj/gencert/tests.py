import unittest
from django import test
from gencert.gcertificate import GCertificate


# Create your tests here.
class GenCertTest(unittest.TestCase):
    def test_gencert(self):
        certificate = GCertificate(format='A4')
        certificate.language = "English"  # Português
        certificate.title = "teste_en"
        certificate.type = "Certificate of Participation"  # Certificado de Participação
        certificate.logo = "static/img/favicon/favicon-192x192.png"
        certificate.company_name = "ArtesGC Inc"
        certificate.student_name = "Nurul Hosny Gaspar de Carvalho"
        certificate.description = "Congratulations,\nThank you!"  # Parabens,\nObrigado!
        return certificate.gencert()


class GenCertRootsTest(test.TestCase):
    pass
