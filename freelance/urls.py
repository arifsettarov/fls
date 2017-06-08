from django.conf.urls import url
from freelance import views
urlpatterns=[
    url(r'^$', views.index, name="Главная"),

    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^register/new-user/$',views.register_create_user),

    url(r'^pokraska/$',views.pokraska),
    url(r'^pokraska_save_order/$',views.pokraska_save),

    url(r'^uteplenie/$',views.uteplenie),
    url(r'^uteplenie_save_order/$',views.uteplenie_save),

    url(r'^design/$',views.design),
    url(r'^design_save_order/$',views.design_save),

    url(r'^otoplenie/$',views.otoplenie),
    url(r'^otoplenie_save_order/$',views.otoplenie_save),

    url(r'^osteklenie-balkonov/$',views.osteklenie_balkonov),
    url(r'^osteklenie-balkonov_save_order/$',views.osteklenie_balkonov_save),


    url(r'^redecorating/',views.kosmetik_remont),
    url(r'^redecorating_save_order/',views.kosmetik_remont_save),

    url(r'^plitka/',views.plitka),
    url(r'^plitka_save_order/',views.plitka_save),

    url(r'^krovlya/',views.krovlya),
    url(r'^krovlya_save_order/',views.krovlya_save),

    url(r'^pol/',views.poli),
    url(r'^pol_save_order/',views.poli_save),

    url(r'^raboti_pod_kluch/',views.pod_kluch),
    url(r'^raboti_pod_kluch_save_order/',views.pod_kluch_save),

    url(r'^santehnika/',views.santehnika),
    url(r'^santehnika_save_order/',views.santehnika_save),

    url(r'^potolki/',views.potolki),
    url(r'^potolki_save_order/',views.potolki_save),

    url(r'^gipsokarton-peregorodki/',views.gipsokarton_peregorodki),
    url(r'^gipsokarton-peregorodki_save_order/',views.gipsokarton_peregorodki_save),

    url(r'^remont-vannoy/',views.remont_vannoy),
    url(r'^remont-vannoy_save_order/',views.remont_vannoy_save),

    url(r'^reshetki/',views.reshetki),
    url(r'^reshetki_save_order/', views.reshetki_save),

    url(r'^oboi/',views.oboi),
    url(r'^oboi_save_order/',views.oboi_save),

    url(r'^beton/',views.beton),
    url(r'^beton_save_order/', views.beton_save),

    url(r'^natyazhnoi_potolok/',views.natyazhnoi_potolok),
    url(r'^natyazhnoi_potolok_save_order/',views.natyazhnoi_potolok_save),
]
