from django.shortcuts import render, redirect, get_object_or_404
from gencert.forms import TcForm, CpForm
from gencert.gcertificate import GCertificate

certificate = GCertificate(format='A4')


# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')


def tc(request):
    if request.method == 'POST':
        form = TcForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            certificate.language = data['language']
            certificate.title = data['title']
            certificate.type = data['type']
            certificate.logo = data['logo']
            certificate.company_name = data['company_name']
            certificate.student_name = data['student_name']
            certificate.description = data['description']
            filename = certificate.gencert()
            redirect(to=f'preview/{filename}')
    else:
        form = TcForm()
    return render(request=request, template_name='training_certificate.html', context={'tc_form': form})


def cp(request):
    if request.method == 'POST':
        form = CpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            certificate.language = data['language']
            certificate.title = data['title']
            certificate.type = data['type']
            certificate.logo = data['logo']
            certificate.company_name = data['company_name']
            certificate.student_name = data['student_name']
            certificate.description = data['description']
            filename = certificate.gencert()
            redirect(to=f'preview/{filename}')
    else:
        form = CpForm()
    return render(request=request, template_name='certificate_participation.html', context={'cp_form': form})


def preview(request, _filename):
    if _filename.endswith('.pdf'):
        filename = f'/pdfs/{_filename}'
    else:
        return render(request=request, template_name='pnf.html')
    return render(request=request, template_name='pdf_preview.html', context={'filename': filename, 'title': 'Not Found'})
