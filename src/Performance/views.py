from django.shortcuts import render
from .forms import Performs
from .models import Performance
from django.db.models import Q
import datetime
# Create your views here.

def PerFormView(request):

    qs = Performance.objects.all()
    # 시간 리스트 만들기
    time_list = []
    for i in range(0, 24):
        t = str(i).zfill(2) + ":00"
        time_list.append(t)

    get_date = request.GET.get('d', '')
    get_time = request.GET.get('t', '')
    get_place = request.GET.get('p', '')
    get_genre = request.GET.get('g', '')

    if get_date or get_genre or get_place or get_time:
        start_time = datetime.datetime.strptime(get_time, '%H:%M').time()
        end_time = datetime.datetime.strptime('23:59', '%H:%M').time()
        if get_date!='':
            perform_list = qs.filter(
                Q(date__gte=get_date),
                Q(end_time__range=[start_time, end_time])
            )
        else:
            perform_list = qs.filter(
                Q(end_time__range=[start_time, end_time])
            )
    print(get_date)
    print(get_time)
    return render(request, 'forms.html', {
        'form' : Performs,
        'objects' : qs,
        'time_list': time_list,
        'get_time' : get_time,
        'get_date' : get_date,
        'perform_list' : perform_list,
    })