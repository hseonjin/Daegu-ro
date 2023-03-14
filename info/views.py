from django.shortcuts import redirect, render
from pytz import common_timezones
from .models import Info
from django.core.paginator import Paginator
# from .forms import TodoForm

# Create your views here.


# info 리스트 조회
def profile(request):
    profile_member = Info.objects.all()
    return render(request, 'info/profile.html', {'profile_member': profile_member})


# # info 세부내용 조회
# def info_detail(request, pk):
#     inform = Info.objects.get(id=pk)
#     return render(request, 'info/info_detail.html', {'inform': inform})
