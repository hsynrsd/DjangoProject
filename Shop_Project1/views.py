from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save() # save the user
        return redirect('/shop')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def hello(request):
    return HttpResponse("Hello World")