from django.shortcuts import render
from .models import Recommend
# Create your views here.

def recommend(request):
    healing = Recommend.objects.filter(thema__contains='힐링')
    history = Recommend.objects.filter(thema__contains='역사')
    food = Recommend.objects.filter(thema__contains='식도락')
    hot = Recommend.objects.filter(thema__contains='핫플')
    ex = Recommend.objects.filter(thema__contains='체험')
    activity = Recommend.objects.filter(thema__contains='액티비티')
    shoping = Recommend.objects.filter(thema__contains='쇼핑')
    culture = Recommend.objects.filter(thema__contains='문화')
    night = Recommend.objects.filter(thema__contains='야경')
    child = Recommend.objects.filter(thema__contains='아이동반')

    context = {'healing' : healing, 'history' : history, 'food' : history, 'food' : food, 'hot' : hot, 'ex' : ex, 'activity' : activity, 'shoping' : shoping, 'culture' : culture, 'night' : night, 'child' : child} 
    
    return render(request, 'recommend/recommend.html', context)