from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):

    data = "Versao 0.21 - apresentação"
    

    return render(request, 'index.html', 
        { 'dados' : data } 
    )

@login_required
def db1(request):

    data = "Versao 0.01 - Dashboard 1.1 (um) "

    # data = clima.objcts.all()

    return render(request, 'dashboard1.html', 
        { 'dados' : data } 
    )    

@login_required
def db2(request):

    data = "Versao 0.01 - Dashboard 2 (dois)"
    

    return render(request, 'dashboard2.html', 
        { 'dados' : data } 
    )        