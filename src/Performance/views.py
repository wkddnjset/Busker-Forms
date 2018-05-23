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

def SuccessView(request):
    return render(request, 'success.html', {})

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def mail_form(request):
    return render(request, 'contact.html', {})

def send_email(request):
    subject = request.POST.get('subject', '')          # Template에서 입력받은 제목
    message = request.POST.get('message', '')          # Template에서 입력받은 내용
    from_email = request.POST.get('from_email', '')    # Template에서 입력받은 이메일
    if subject and message and from_email:
        print(subject)
        try:
            send_mail(subject, message, from_email, ['aiden@tirrilee.io'])
            print("메일보내기 성공")
            return HttpResponseRedirect('/success')  # 메일 보내기에 성공했을시, 연결되는 링크
        except BadHeaderError:
            return HttpResponse('헤더 설정이 잘못 되었습니다.')
    else:
        # 실제로는 Form Class를 사용하고, 알아서 적절한 오류 메세지를 출력합니다.
        return HttpResponse('빈칸을 알맞게 채웠는지 확인하세요.')