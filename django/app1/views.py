from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):

    data = "Apresentação"
    

    return render(request, 'index.html', 
        { 'dados' : data } 
    )

@login_required
def db1(request):

    data = "DashBoard Data Base "


    return render(request, 'dashboard1.html', 
        { 'dados' : data } 
    )    

def db3(request):

    data = "DashBoard Previsão "


    return render(request, 'dashboard3.html', 
        { 'dados' : data } 
    )    