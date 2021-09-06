from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')


def tc(request):
    return render(request=request, template_name='training_certificate.html')


def cp(request):
    return render(request=request, template_name='certificate_participation.html')
