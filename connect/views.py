from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConnectForm

# Create your views here.

def connectview(request):
    if request.method == 'POST':

        form = ConnectForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = ConnectForm()
    return render(request, 'form.html', {'form': form})