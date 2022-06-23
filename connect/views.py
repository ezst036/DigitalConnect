from django.shortcuts import render, redirect
from .forms import ConnectForm
from django.contrib import messages

def connectview(request):
    if request.method == 'GET':
        #Pre-populate user information in the new form
        if request.user.is_authenticated:
            form = ConnectForm(initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name
            })
    if request.method == 'POST':
        #Receive filled out form from user
        form = ConnectForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Your message has been received.')
            form.save()
            return redirect('home')
    
    #Blank form for users who are not logged in
    if not request.user.is_authenticated:
        form = ConnectForm()
    
    return render(request, 'form.html', {'form': form})