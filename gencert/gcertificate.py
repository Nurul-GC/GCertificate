import os.path

from fpdf import FPDF, HTMLMixin
from datetime import date


class GCertificate(FPDF, HTMLMixin):
    type = ""
    title = ""
    logo = ""
    language = ""
    company_name = ""
    student_name = ""
    today = date.today()
    description = ""

    def html(self):
        if self.language == "English":
            if self.type == "Training Certificate":
                pass
            elif self.type == "Certificate of Participation":
                pass
        elif self.language == "Português":
            if self.type == "Certificado de Formação":
                pass
            elif self.type == "Certificado de Participação":
                pass

    def cp(self):
        """certificate of participation content"""
        if self.language == "English":
            return f"""<center>
<img src="{self.logo}" width="50", height="50">
<h1><i>{self.type}</i></h1>
</center>
<br><br>
{'-' * 390}

<p>
It is with great honor that <b>{self.company}<b> certifies and appreciates the collaboration and presence of <b>{self.student}<b> on this event.<br>
</p>

<p>
{self.description}
<br><br>
Certificate issued in: <b>{self.today}</b><br>
</p>

{'-' * 390}
<br><br>
<p align="right"><b>Signature of the Responsible{' ' * 20}</b><br><br>
_____________________________________________</p>
</div>
"""
        elif self.language == "Português":
            return f"""
<center>
<img src="{self.logo}" width="50", height="50">
<h1><i>{self.type}</i></h1>
</center>
<br><br>
{'-'*390}

<p>
E com bastante honra que a <b>{self.company_name}</b> certifica e agradece a colaboração e presença do carissimo <b>{self.student_name}</b>
neste evento.<br><br>

{self.description}

Certificado emitido em: <b>{self.today}</b><br>
</p>

{'-'*390}
<br><br>
<p align="right"><b>Assinatura do Responsavel{' '*20}</b><br><br>
_____________________________________________</p>
</div>
"""

    def tc(self):
        """training certificate content"""
        if self.language == "English":
            pass
        elif self.language == "Português":
            pass

    def gencert(self):
        texto = self.html()
        self.add_page(orientation='L')
        self.set_author(author=self.company_name)
        self.set_title(title=self.title)
        self.write_html(text=texto)
        self.output(name=f'{self.title}.pdf', dest='F')
        return os.path.abspath(f'./{self.title}.pdf')


if __name__ == '__main__':
    certificate = GCertificate(format='A4')
    certificate.language = "English"
    certificate.title = "teste"
    certificate.type = "Certificate of Participation"
    certificate.gencert()
