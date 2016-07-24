from django.shortcuts import render

def login_form(request):
    return render(request, 'account/login.html')
