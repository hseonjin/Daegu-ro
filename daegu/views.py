from django.shortcuts import render

def index(request):
    datas = 'daeguro'
    return render(request, 'index.html', {'datas' : datas})


def dashboard(request):
    datas = 'daeguro'
    return render(request, 'dashboard.html', {'datas' : datas})

