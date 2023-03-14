from django.shortcuts import render
from .models import List

# Create your views here.

def list(request):
    list_data = List.objects.all()
    healing = List.objects.filter(thema__contains='힐링')
    history = List.objects.filter(thema__contains='역사')
    food = List.objects.filter(thema__contains='식도락')
    hotplace = List.objects.filter(thema__contains='핫플')
    experience = List.objects.filter(thema__contains='체험')
    activity = List.objects.filter(thema__contains='액티비티')
    shoping = List.objects.filter(thema__contains='쇼핑')
    culture = List.objects.filter(thema__contains='문화')
    night = List.objects.filter(thema__contains='야경')
    child = List.objects.filter(thema__contains='아이동반')

    return render(request, 'list/list_map.html', {'list_data': list_data, 'healing':healing, 'history':history, 'food':food, 'hotplace':hotplace, 'experience':experience, 'activity':activity, 'shoping':shoping, 'culture':culture, 'night':night, 'child':child})
    # 이건 나중에 해보기
    # thema_list = List.objects.order_by().values_list('thema').distinct()
    # print(thema_list)
    # return render(request, 'list/list_map.html', {'list_data': thema_list})


def list_healing(request):
    list_datas = List.objects.all()
    healing = List.objects.filter(thema__contains='힐링')  

    return render(request, 'list/list_healing.html', {'list_datas': list_datas, 'healing':healing})

def list_history(request):
    list_datas = List.objects.all()
    history = List.objects.filter(thema__contains='역사')  

    return render(request, 'list/list_history.html', {'list_datas': list_datas, 'history':history})

def list_food(request):
    list_datas = List.objects.all()
    food = List.objects.filter(thema__contains='식도락')  

    return render(request, 'list/list_food.html', {'list_datas': list_datas, 'food':food})

def list_hotplace(request):
    list_datas = List.objects.all()
    hotplace = List.objects.filter(thema__contains='핫플')  

    return render(request, 'list/list_hotplace.html', {'list_datas': list_datas, 'hotplace':hotplace})

def list_experience(request):
    list_datas = List.objects.all()
    experience = List.objects.filter(thema__contains='체험')  

    return render(request, 'list/list_experience.html', {'list_datas': list_datas, 'experience':experience})

def list_activity(request):
    list_datas = List.objects.all()
    activity = List.objects.filter(thema__contains='액티비티')  

    return render(request, 'list/list_activity.html', {'list_datas': list_datas, 'activity':activity})

def list_shoping(request):
    list_datas = List.objects.all()
    shoping = List.objects.filter(thema__contains='쇼핑')  

    return render(request, 'list/list_shoping.html', {'list_datas': list_datas, 'shoping':shoping})

def list_culture(request):
    list_datas = List.objects.all()
    culture = List.objects.filter(thema__contains='문화')  

    return render(request, 'list/list_culture.html', {'list_datas': list_datas, 'culture':culture})

def list_night(request):
    list_datas = List.objects.all()
    night = List.objects.filter(thema__contains='야경')  

    return render(request, 'list/list_night.html', {'list_datas': list_datas, 'night':night})

def list_child(request):
    list_datas = List.objects.all()
    child = List.objects.filter(thema__contains='아이동반')  

    return render(request, 'list/list_child.html', {'list_datas': list_datas, 'child':child})
