from datetime import datetime

from django.shortcuts import render
import requests

from mainapp.models import Question, Feedback, Applicant


# Create your views here.

def index_set(request):
    if request.method == 'POST':
        name = request.POST['name']
        telegram = request.POST['telegram']
        phone = request.POST['phone']
        message = request.POST['message']
        text = f"""Новый сообщение от {name}
Имя : {name}
Телеграм : {telegram}
Номер телефона : {phone}
Сообщение : {message}
Дата : {datetime.today()}"""
        base_url = f'https://api.telegram.org/bot5503829283:AAFSA7ItBst8xhf-Lg_9cqa8iPOPGe4HA2s/sendMessage?chat_id=-851393242&text={text}'
        requests.get(base_url)
        Feedback.objects.create(
            first_name=name, telegram=telegram, phone_number=phone, message=message
        )
    return render(request, "index.html")


def sat_set(request):
    if request.method == 'POST':
        name = request.POST['name']
        telegram = request.POST['telegram']
        phone = request.POST['phone']
        text = f"""Новая заявка
Имя : {name}
Телеграм : {telegram}
Номер телефона : {phone}
Курс : SAT
Дата : {datetime.today()}"""
        base_url = f'https://api.telegram.org/bot5503829283:AAFSA7ItBst8xhf-Lg_9cqa8iPOPGe4HA2s/sendMessage?chat_id=-851393242&text={text}'
        requests.get(base_url)
        Applicant.objects.create(
            first_name=name, telegram=telegram, phone_number=phone, course='sat'
        )
    context = {
        'questions': Question.objects.all()[:6]
    }
    return render(request, "index-3.html", context)


def ielts_set(request):
    if request.method == 'POST':
        name = request.POST['name']
        telegram = request.POST['telegram']
        phone = request.POST['phone']
        text = f"""Новая заявка
Имя : {name}
Телеграм : {telegram}
Номер телефона : {phone}
Курс : IELTS
Дата : {datetime.today()}"""
        base_url = f'https://api.telegram.org/bot5503829283:AAFSA7ItBst8xhf-Lg_9cqa8iPOPGe4HA2s/sendMessage?chat_id=-851393242&text={text}'
        requests.get(base_url)
        Applicant.objects.create(
            first_name=name, telegram=telegram, phone_number=phone, course='ielts'
        )
    context = {
        'questions': Question.objects.all()[:6]
    }
    return render(request, "index-2.html", context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        telegram = request.POST['telegram']
        phone = request.POST['phone']
        message = request.POST['message']
        text = f"""Новый сообщение от {name}
Имя : {name}
Телеграм : {telegram}
Номер телефона : {phone}
Сообщение : {message}
Дата : {datetime.today()}"""
        base_url = f'https://api.telegram.org/bot5503829283:AAFSA7ItBst8xhf-Lg_9cqa8iPOPGe4HA2s/sendMessage?chat_id=-851393242&text={text}'
        requests.get(base_url)
        Feedback.objects.create(
            first_name=name, telegram=telegram, phone_number=phone, message=message
        )
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
