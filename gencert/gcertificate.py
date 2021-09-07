import os.path

from fpdf import FPDF, HTMLMixin
from datetime import date


class GCertificate(FPDF, HTMLMixin):
    type = None
    logo = None
    title = None
    language = None
    description = None
    course_name = None
    company_name = None
    student_name = None
    today = date.today()

    def _description(self):
        return self.description.replace("\n", "<br>")

    def html(self):
        if self.language == "English":
            if self.type == "Training Certificate":
                return self.tc()
            elif self.type == "Certificate of Participation":
                return self.cp()
        elif self.language == "Português":
            if self.type == "Certificado de Formação":
                return self.tc()
            elif self.type == "Certificado de Participação":
                return self.cp()

    def cp(self):
        """
        - certificate of participation content
        - conteudo do certificado de participacao
        """
        if self.language == "English":
            return f"""<center>
<img src="{self.logo}" width="50" height="50">
<h1><i>{self.type}</i></h1>
</center>
<br><br>
{'-' * 390}

<p>
It is with great honor that <b>{self.company_name}</b> certifies the collaboration and appreciates the presence of <b>{self.student_name}</b> on this event.<br>
</p>

<p>
{self._description()}
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
<img src="{self.logo}" width="50" height="50">
<h1><i>{self.type}</i></h1>
</center>
<br><br>
{'-'*390}

<p>
E com bastante honra que a <b>{self.company_name}</b> certifica a colaboração e agradece a presença do carissimo <b>{self.student_name}</b>
neste evento.<br>
</p>

<p>
{self._description()}
<br><br>
Certificado emitido em: <b>{self.today}</b><br>
</p>

{'-'*390}
<br><br>
<p align="right"><b>Assinatura do Responsavel{' '*20}</b><br><br>
_____________________________________________</p>
</div>
"""

    def tc(self):
        """
        - training certificate content
        - conteudo do certificado de formacao
        """
        if self.language == "English":
            return f"""..."""
        elif self.language == "Português":
            return f"""..."""

    def gencert(self):
        try:
            texto = self.html()
            self.add_page(orientation='L')
            self.set_author(author=self.company_name)
            self.set_title(title=self.title)
            self.write_html(text=texto)
            os.makedirs(name='static/pdfs/', exist_ok=True)
            self.output(name=f'static/pdfs/{self.title}.pdf', dest='F')
            return f'{self.title}.pdf'
        except Exception as error:
            raise error
