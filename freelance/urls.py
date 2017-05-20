from django.conf.urls import url
from freelance import views
urlpatterns=[
    url(r'^$', views.index, name="Главная"),
    url(r'^create_order/$', views.create_order, name="Оформление заказа"),
    url(r'^pokraska-sten/$',views.pokraska),
    url(r'^pokraska_save_order/$',views.pokraska_save),

    url(r'^obshivka/$',views.obshivka),
    url(r'^obshivka_save_order/$',views.obshivka_save),

    url(r'^gazovie-sistemi/$',views.gas_systems),
    url(r'^gazovie-sistemi_save_order/$',views.gas_systems),

    url(r'^plitochnie-raboti/$',views.plitochnie_raboti),
    url(r'^plitochnie-raboti_save_order/$',views.plitochnie_raboti),

    url(r'^remont-pomesheniy/$',views.remont_pomesheniy),
    url(r'^remont-pomesheniy_save_order/$',views.remont_pomesheniy),

    url(r'^remont-pomesheniy/$',views.plitochnie_raboti),
    url(r'^remont-pomesheniy_save_order/$',views.plitochnie_raboti),

    url(r'^remont-krishi/$',views.remont_krishi),
    url(r'^remont-krishi_save_order/$',views.remont_krishi),

    url(r'^parket/$',views.parket),
    url(r'^parket_save_order/$',views.parket),

    url(r'^vodoprovod/$',views.vodoprovod),
    url(r'^vodoprovod_save_order/$',views.vodoprovod),



]
