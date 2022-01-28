from django.shortcuts import render
from sistema.forms import cadastroform


# Create your views here.
def home(request):
    return render(request, 'index.html')


def form(request):
    data = {}
    data['form'] = cadastroform()
    return render(request, 'form.html', data)
