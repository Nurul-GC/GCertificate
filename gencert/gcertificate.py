from fpdf import FPDF, HTMLMixin
from datetime import date


class GCertificate(FPDF, HTMLMixin):
    title = "Certificado de Participacao"
    logo = "favicon-192x192.png"
    company = "ArtesGC Inc."
    student = "Nurul GC"
    today = date.today()
    content = ("Lorem ipsum dolor sit amet consectetur adipiscing elit iaculis, egestas sollicitudin suscipit sed est arcu vel rutrum torquent,\n"
               "consequat a sociosqu felis class nibh mi. Erat porttitor accumsan neque sodales massa euismod ultricies eleifend vestibulum, nam porta pellentesque platea ultrices nec nibh congue,\n"
               "vel sociosqu venenatis enim faucibus morbi vitae nullam. Arcu hac felis porta suscipit senectus orci nisl condimentum, dis risus morbi luctus laoreet tristique aptent nibh, ligula eros pellentesque\n"
               "eget sagittis non lacus. Dis tellus cras hendrerit semper consequat, tempor parturient laoreet purus neque pretium, metus varius diam tortor. Tortor erat feugiat morbi vehicula metus eros rutrum\n"
               "dignissim velit, himenaeos nullam maecenas laoreet at penatibus ante cras, sociosqu augue class aenean leo pharetra fusce euismod. Magnis id felis praesent pharetra porttitor molestie venenatis\n"
               "parturient, potenti at neque cum justo laoreet facilisis tempus, vitae pretium placerat in egestas luctus sollicitudin.<br><br>\n")

    def html(self):
        return f"""
<center>
<img src="{self.logo}" width="50", height="50">
<h1><i>{self.title}</i></h1>
</center>
<br><br>
{'-'*390}

<p>
E com bastante honra que a <b>{self.company}</b> certifica e agradece a colaboracao do carissimo <b>{self.student}</b>
na elaboracao deste projecto.<br><br>

{self.content}

Certificado emitido em: <b>{self.today}</b><br>
</p>

{'-'*390}
<br><br>
<p align="right"><b>Assinatura do Responsavel{' '*20}</b><br><br>
_____________________________________________</p>
</div>
"""

    def gencert(self):
        texto = self.html()
        self.add_page(orientation='L')
        self.write_html(text=texto)


if __name__ == '__main__':
    certificate = GCertificate(format='A4')
    certificate.gencert()
    certificate.output(name='static/pdf/teste.pdf', dest='F')
