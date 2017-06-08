from email.mime.text import MIMEText
from email.header import Header


from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib.auth.models import User
import smtplib
from .models import *

def open_server():
    server = smtplib.SMTP('smtp.gmail.com:587')
    mail_sender = 'settarov.a.i15@gmail.com'

    username = mail_sender
    password = 'Ctnnfhjdfhba1998'
    server.starttls()
    server.ehlo()
    server.login(username, password)
    return server
def message_mail(server,message,for_worker):
    message = MIMEText(message,'plain','utf-8')
    message['Subject'] = Header("Новый заказ для вас.", 'utf-8')
    server.sendmail("settarov.a.i15@gmail.com",str(for_worker),message.as_string())


def close_server(server):
    server.quit()
def send_for_workers(type,objects):
    server = open_server()
    workers = Workers.objects.all()
    for object in objects:
        for worker in workers:
            if type in worker.type:
                if object.city in worker.region:
                    for_worker= worker.email
                    message = object.message
                    message_mail(server,message,for_worker)
                    object.mailed = True
                    object.save()
    close_server(server)

def create_email(type,model):
    objects = model.objects.all()
    not_mailed= []
    for object in objects:
        if object.mailed == False:
            not_mailed.append(object)
    send_for_workers(type,not_mailed)


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
    if request.POST:
        ploshad = request.POST['ploshad']
        rooms = request.POST['rooms']
        potolki = request.POST['potolki']
        material_ot = request.POST['material_ot']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details)<=1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money+"р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Побелить покрасить\nПлощадь: %s кв.м. Комнат: %s Покраска потолков: %s\n" \
                  "Материал предоставляет: %s\nПодробности:%s\nБюджет:%s" \
                  "Место работы: %s %s"%(ploshad,rooms,potolki,material_ot,details,money,city,district)
        new_order = Pokraska(ploshad=ploshad,rooms=rooms, material_ot=material_ot,
                             details=details,money=money,city=city,district=district,
                             phone=phone,email=email, message=message)
        new_order.save()
        create_email("Побелить покрасить;", Pokraska)
    return redirect('/')

def uteplenie(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/obshivka.html', args)

def uteplenie_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        material = request.POST['material']
        otkosi = request.POST['otkosi']
        finish = request.POST['finish']
        if finish == "Нужно":
            finish_material = request.POST['finish_material']
        else:
            finish_material = "Без покрытия"
        material_ot = request.POST['material_ot']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details)<=1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money+"р."

        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Утепление\nПлощадь: %s кв.м.\nПредпочтительный материал:%s\n" \
                  "Откосы(в погонных метрах): %s\nФинишная отделка: %s, Матриал:%s\n" \
                  "Материал предоставляет: %s\nПодробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, material,otkosi,finish,finish_material, material_ot, details, money, city, district)
        new_order = Uteplenie(ploshad=ploshad,material=material,otkosi=otkosi,finish=finish,finish_material=finish_material,
                        material_ot=material_ot,
                        details=details, money=money, city=city, district=district,
                        phone=phone, email=email, message=message)
        new_order.save()
        create_email("Утепление фасадо;", Uteplenie)
    return redirect('/')


def design(request):
    args={}
    args.update(csrf(request))
    return render_to_response('Orders/remont/disign_interier.html',args)
def design_save(request):
    if request.POST:
        room_type = request.POST['room_type']
        try:
            design_interier = request.POST['disign_interier']
        except:
            design_interier =""
        try:
            design_project = request.POST['disign_project']
        except:
            design_project = ""

        what_do = design_interier+";"+design_project
        if what_do ==";":
            what_do = "не поределено."

        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money+"р."

        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Дизайн интерьер/проект\n" \
                  "Тип помещения: %s\n" \
                  "Объем работ: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (room_type, what_do,details, money, city, district)
        new_order = Design(room_type=room_type,what_do=what_do,details=details, money=money, city=city, district=district,
                              phone=phone, email=email, message=message)
        new_order.save()
        create_email("Дизайн интерьер/проект;", Design)
    return redirect('/')
def otoplenie(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/otoplenie.html', args)
def otoplenie_save(request):
    if request.POST:
        room_type = request.POST['room_type']
        ploshad = request.POST['ploshad']
        works = request.POST["works"]
        kotyol = request.POST["kotyol"]
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money+"р."
        if len(works)<=1:
            works = "Не определенно"
        if len(kotyol)<=1:
            kotyol = "Без котла"
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Отопление\nТип помещения: %s, Площадь: %s кв.м.\n" \
                  "Объем работ: %s\nТип котла: %s\n"\
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (room_type, ploshad, works,kotyol,details, money, city, district)

        new_order = Otoplenie(room_type=room_type,ploshad=ploshad,works=works,kotyol=kotyol,details=details,money=money,
                              city=city,district=district,phone=phone,email=email,message=message)
        new_order.save()
        create_email("Отопление;", Otoplenie)
    return redirect("/")



def osteklenie_balkonov(request):
    args={}
    args.update(csrf(request))
    return render_to_response("Orders/remont/osteklenie_balkonov.html",args)
def osteklenie_balkonov_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        glassing_type = request.POST['glassing_type']
        etazh = request.POST['etazh']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Остекление балконов\nПлощадь: %s кв.м.\n" \
                  "Вид остекления: %s\nЭтаж: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, glassing_type, etazh, details, money, city, district)
        new_order = Osteklenie_balkonov(ploshad=ploshad,glassing_type=glassing_type,etazh=etazh,
                                        details=details,money=money,city=city,district=district,
                                        phone=phone,email=email,message=message)
        new_order.save()
        create_email("Остекление балконов;", Osteklenie_balkonov)
        return redirect('/')

def kosmetik_remont(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('Orders/remont/kosmetik_remont.html', args)

def kosmetik_remont_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        rooms = request.POST['rooms']
        works = request.POST['works']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        if len(works)<=1:
            works = "Не определено."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Косметический ремонт\nПлощадь: %s кв.м.\n" \
                  "Область ремонта: %s\nОбъем работ: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, rooms, works, details, money, city, district)
        new_order= Redecorating(ploshad=ploshad,rooms=rooms,works=works,details=details,money=money,city=city,
                                district=district,phone=phone,email=email,message=message)
        new_order.save()
        create_email("Косметический ремонт;", Redecorating)
    return redirect('/')

def plitka(request):
    args= {}
    args.update(csrf(request))
    return  render_to_response("Orders/remont/plitka.html",args)
def plitka_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        santehnika = request.POST['santehnika']
        material_ot = request.POST['material_ot']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Плитка\nПлощадь: %s кв.м.\n" \
                  "Установка сантехники: %s\n" \
                  "Материал предоставляет: %s\nПодробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, santehnika, material_ot, details, money, city, district)
        new_order = Plitka(ploshad=ploshad,santehnika=santehnika,material_ot=material_ot,details=details,
                           money=money,city=city,district=district,phone=phone,email=email,message=message)
        new_order.save()
        create_email("Плитка;", Plitka)
    return redirect("/")


def krovlya(request):
    args ={}
    args.update(csrf(request))
    return render_to_response("Orders/remont/krovlya.html",args)
def krovlya_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        postavka_materiala = request.POST['postavka_materiala']
        dop = request.POST['dop']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(dop)<=1:
            dop = "Отсутствуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Кровля\nПлощадь: %s кв.м.\n" \
                  "Поставка материла: %s\n" \
                  "Дополнительные элементы: %s\nПодробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, postavka_materiala, dop, details, money, city, district)
        new_order = Krovlya(ploshad=ploshad, postavka_materiala=postavka_materiala, dop=dop, details=details,
                           money=money, city=city, district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Кровля;", Krovlya)
    return redirect("/")

def poli(request):
    args={}
    args.update(csrf(request))
    return  render_to_response("Orders/remont/poli.html",args)
def poli_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        type_pokr = request.POST['type_pokr']
        works = request.POST['works']
        material_ot = request.POST['material_ot']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(works) <= 1:
            works = "Не определено"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Полы\nПлощадь: %s кв.м., Тип покрытия: %s\n" \
                  "Объем работ: %s\n" \
                  "Материал предоставляет: %s\nПодробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, type_pokr, works,material_ot, details, money, city, district)
        new_order = Poli(ploshad=ploshad,type_pokr=type_pokr,works=works,material_ot=material_ot,details=details,money=money, city=city,
                         district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Полы;", Poli)
    return redirect("/")

def pod_kluch(request):
    args = {}
    args.update(csrf(request))
    return render_to_response("Orders/remont/pod_kluch.html",args)
def pod_kluch_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        room_type = request.POST['room_type']
        works = request.POST['works']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(works) <= 1:
            works = "Не определено"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Работы под ключ\nПлощадь: %s кв.м., Тип помещения: %s\n" \
                  "Объем работ: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, room_type, works,details, money, city, district)
        new_order = Raboti_pod_kluch(ploshad=ploshad,room_type=room_type,works=works,details=details,money=money, city=city,
                         district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Работы под ключ;", Raboti_pod_kluch)
    return redirect("/")

def santehnika(request):
    args={}
    args.update(csrf(request))
    return render_to_response("Orders/remont/santehnika.html",args)
def santehnika_save(request):
    if request.POST:
        work_type = request.POST['work_type']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Сантехника\n" \
                  "Вид работы: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (work_type, details, money, city, district)
        new_order = Santehnika(work_type=work_type,details=details,money=money, city=city,
                         district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Сантехника;", Santehnika)
    return redirect("/")
def potolki(request):
    args = {}
    args.update(csrf(request))
    return render_to_response("Orders/remont/potolki.html",args)
def potolki_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        material = request.POST['material']
        isol = request.POST['isol']
        svet = request.POST['svet']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(isol)<=1:
            isol = "Не нужна"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Потолки\nПлощадь: %s кв.м.\nМатериал: %s\nИзоляция: %s\nМонтаж светотехники: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad,material,isol,svet, details, money, city, district)
        new_order = Potolki(ploshad=ploshad,material=material,isol=isol, svet=svet,details=details,money=money, city=city,
                         district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Потолки;", Potolki)
    return redirect("/")


def gipsokarton_peregorodki(request):
    args={}
    args.update(csrf(request))
    return render_to_response("Orders/remont/gipsokarton_peregorodki.html",args)

def gipsokarton_peregorodki_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        finish = request.POST['finish']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Гипсокартонные перегородки\nПлощадь: %s кв.м.\nФинишная отделка: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, finish, details, money, city, district)
        new_order = Gipsokarton_peregorodki(ploshad=ploshad, finish=finish, details=details, money=money,
                            city=city,
                            district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Гипсокартонные перегородки;", Gipsokarton_peregorodki)
    return redirect("/")

def remont_vannoy(request):
    args = {}
    args.update(csrf(request))
    return render_to_response("Orders/remont/remont_vannoy.html",args)
def remont_vannoy_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        plitka = request.POST['plitka']
        santehnika = request.POST['santehnika']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Ремонт ванной\nПлощадь: %s кв.м.\nКладка плитки: %s\nУстановка сантехники: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, plitka,santehnika, details, money, city, district)
        new_order = Remont_vannoy(ploshad=ploshad, plitka=plitka,santehika=santehnika, details=details, money=money,
                                            city=city,
                                            district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Ремонт ванной;", Remont_vannoy)
    return redirect("/")


def reshetki(request):
    args={}
    args.update(csrf(request))
    return render_to_response("Orders/remont/reshetki.html",args)
def reshetki_save(request):
    if request.POST:
        count = request.POST['count']
        type = request.POST['type']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Решетки на окна и двери.\nКоличество: %s шт.\nТип решеток: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (count, type, details, money, city, district)
        new_order = Reshetki(count=count, type=type, details=details, money=money,
                                  city=city,
                                  district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Решетки на окна;", Reshetki)
    return redirect("/")

def oboi(request):
    args={}
    args.update(csrf(request))
    return render_to_response("Orders/remont/oboi.html",args)
def oboi_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Поклейка обоев.\nПлощадь: %s кв.м.\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, details, money, city, district)
        new_order = Oboi(ploshad=ploshad, details=details, money=money,
                             city=city,
                             district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Поклейка обоев;", Oboi)
    return redirect("/")

def beton(request):
    args={}
    args.update(csrf(request))
    return render_to_response("Orders/remont/beton.html",args)
def beton_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Бетонные работы.\nПлощадь: %s кв.м.\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, details, money, city, district)
        new_order = Beton(ploshad=ploshad, details=details, money=money,
                             city=city,
                             district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Бетонные работы;", Beton)
    return redirect("/")

def natyazhnoi_potolok(request):
    args={}
    args.update(csrf(request))
    return render_to_response("Orders/remont/natyazhnoi_potolok.html",args)
def natyazhnoi_potolok_save(request):
    if request.POST:
        ploshad = request.POST['ploshad']
        svet = request.POST['svet']
        details = request.POST['details']
        money = request.POST['money']
        city = request.POST['city']
        district = request.POST['district']
        phone = request.POST['phone']
        email = request.POST['email']
        if len(details) <= 1:
            details = "Отсутсвуют"
        if len(money) == 0:
            money = "По договоренности"
        else:
            money = money + "р."
        message = "Здравствуйте!\nМы нашли новый заказ для вас.\nДанные по заказу:\n" \
                  "Тип заказа: Натяжной потолок.\nПлощадь: %s кв.м.\n Монтаж светотежники: %s\n" \
                  "Подробности:%s\nБюджет:%s\n" \
                  "Место работы: %s %s" % (ploshad, svet,details, money, city, district)
        new_order = Natyazhnoi_potolok(ploshad=ploshad,svet=svet, details=details, money=money,
                             city=city,
                             district=district, phone=phone, email=email, message=message)
        new_order.save()
        create_email("Натяжной потолок;", Natyazhnoi_potolok)
    return redirect("/")
def login(request):
    args={}
    args.update(csrf(request))
    return render_to_response('login.html', args)
def register(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('register.html', args)

def register_create_user(request):
    if request.POST:
        surname = request.POST["surname"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        snils = request.POST["snils"]
        password = request.POST["password"]
        works = request.POST["works"]
        region = request.POST["city"]
        new_user = User(username=email,password=password)
        new_worker = Workers(surname=surname,name=name,email=email,telephone=phone,SNILS=snils,password=password,
                             type=works,region=region)
        new_user.save()
        new_worker.save()


    return redirect('/login/')

