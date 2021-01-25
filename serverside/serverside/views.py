from django.views import View
from django.shortcuts import render, redirect
from .forms import QueryForm
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
# def index(request):
#     return render(request, "index.html")

def index(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            details = form.cleaned_data['detail']
            
            rec = "ankurkumar93@protonmail.com"
            send_mail(subject,details,'parvaiziqra@gmail.com',['ankurkumar93@protonmail.com'], fail_silently=False)
            
            messages.success(request, "Thanks for your mail")
            
            return render(request, 'index.html', {'form': form})
            
            
    else:
        form = QueryForm()
    
    return render(request, 'index.html', {'form': form})
