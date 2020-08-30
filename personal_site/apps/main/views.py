from django.shortcuts import render

from .models import IPRipper
from .forms import IPForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = IPForm(request.POST)
        if form.is_valid():
            new_ip = IPRipper(
                ip=form.cleaned_data["ip"]
                )
            new_ip.save()
    else:
        form = IPForm()
    return render(request, 'about.html', context={"form": form})