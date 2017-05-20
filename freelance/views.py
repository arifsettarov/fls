from email.mime.text import MIMEText
from email.header import Header


from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib.auth.models import User
import smtplib
from .forms import *
from .models import Workers,Link_Section

def mail_order(orders):
    server = smtplib.SMTP('smtp.gmail.com:587')
    mail_sender = 'settarov.a.i15@gmail.com'

    username = mail_sender
    password = 'Ctnnfhjdfhba1998'
    server.starttls()
    server.ehlo()
    server.login(username, password)
    workers = Workers.objects.all()
    for order in orders:
        for worker in workers:
            if order.type in worker.type.all():
                if order.region in worker.region.all():
                    message_text = u"Уважаемый %s.Мы нашли подходящий для вас заказ.\n"\
                                   "Данные по заказу: %s\n"\
                                   "Описание: %s\n"\
                                   "Стоимость: от %s до %s\n"\
                                   "Вы можете связться с заказчиком по телефону: %s %s"\
                                   %(worker.surname+" "+worker.name,str(order.type)+", "+str(order.region),str(order.description),
                                     str(order.price_start),str(order.price_end),str(order.telephone),str(order.name))
                    message = MIMEText(message_text,'plain','utf-8')
                    message['Subject'] = Header("Новый заказ для вас.", 'utf-8')
                    server.sendmail(mail_sender,str(worker.email),message.as_string())
                    order.mailed=True
                    order.save()
    server.quit()
def check_mail_order():
    orders = Orders.objects.all()
    not_mailed_orders = []
    for order in orders:
        if order.mailed==False:
            not_mailed_orders.append(order)

    mail_order(not_mailed_orders)
# Create your views here.
def index(request):
    objects = Link_Section.objects.all()
    args = {}
    args['objects']= objects
    return render_to_response('mainpage.html', args)

def pokraska(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/pokraska_sten.html', args)
def pokraska_save(request):
    pass

def obshivka(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/obshivka.html', args)

def obshivka_save(request):
    pass

def gas_systems(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/gas_systems.html', args)
def remont_pomesheniy(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/remont_pomesheniy.html', args)
def plitochnie_raboti(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/plitochnie_raboti.html', args)
def remont_krishi(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/remont_krishi.html', args)
def parket(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/parket.html', args)
def vodoprovod(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/vodoprovod.html', args)















def create_order(request):
    form = Create_Order_form
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_order.html',args)

def save_order(request):
    if request.POST:
        form = Create_Order_form(request.POST)
        if form.is_valid():
            form.save()
    check_mail_order()
    return redirect('/')


def login(request):
    form = Login_Form
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('login.html',args)
def login_check(request):
    if request.POST:
        form = Login_Form(request.POST)
        if form.is_valid():
            data =form.data
            email = data.get('email')



    return redirect('/')


def register(request):
    form = Register_Form
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('register.html', args)

def register_create_user(request):
    if request.POST:
        form = Register_Form(request.POST)
        form.save()

        username = form.data.get('email')
        password = form.data.get('password')
        new_user = User(username=username,password=password)
        new_user.save()


    return redirect('/login/')

