from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Link_Section(models.Model):
    class Meta:
        verbose_name = "Иконки разделов"

    def __str__(self):
        return self.name
    name = models.CharField(max_length=120, verbose_name="Навание вида работы:")
    image = models.ImageField(verbose_name="Изображение")
    link=models.CharField( max_length=120, verbose_name="Ссылка")

class Pokraska(models.Model):
    class Meta:
        db_table = "pokraska"
        verbose_name ="Побелить покрасить"
    ploshad = models.CharField(max_length=25)
    rooms = models.CharField(max_length=15)
    potolki = models.CharField(max_length=20, default="не требуется")
    material_ot = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)


class Uteplenie(models.Model):
    class Meta:
        db_table = "uteplenie"
        verbose_name ="Утепление"

    ploshad = models.CharField(max_length=25)
    material = models.CharField(max_length=100)
    otkosi = models.CharField(max_length=100)
    finish = models.CharField(max_length=20)
    finish_material = models.CharField(max_length=20)
    material_ot = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)


class Design(models.Model):
    class Meta:
        db_table = "design"
        verbose_name = "Дизайн интерьер/проект"
    room_type =models.CharField(max_length=30)
    what_do = models.CharField(max_length=50, default="Не определено.")
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)


class Otoplenie(models.Model):
    class Meta:
        db_table = "otoplenie"
        verbose_name = "Отопление"
    room_type = models.CharField(max_length=20)
    ploshad = models.CharField(max_length=20)
    works = models.CharField(max_length=250)
    kotyol = models.CharField(max_length=50)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)


class Osteklenie_balkonov(models.Model):
    class Meta:
        db_table="osteklenie_balkonov"
        verbose_name = "Остекление балконов"

    ploshad = models.CharField(max_length=20)
    glassing_type = models.CharField(max_length=50)
    etazh = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Redecorating(models.Model):
    class Meta:
        db_table="cosmetic_remont"
        verbose_name = "Косметический ремонт"

    ploshad = models.CharField(max_length=20)
    rooms = models.CharField(max_length=50)
    works = models.TextField()
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Plitka(models.Model):
    class Meta:
        db_table="plitka"
        verbose_name = "Плитка"
    ploshad = models.CharField(max_length=20)
    santehnika = models.CharField(max_length=10)
    material_ot =models.CharField(max_length=15)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Krovlya(models.Model):
    class Meta:
        db_table="krovlya"
        verbose_name = "Кровля"
    ploshad = models.CharField(max_length=20)
    postavka_materiala = models.CharField(max_length=10)
    dop = models.CharField(max_length=50)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Poli(models.Model):
    class Meta:
        db_table="poli"
        verbose_name="Полы"
    ploshad = models.CharField(max_length=20)
    type_pokr = models.CharField(max_length=20)
    works= models.TextField()
    materiali_ot = models.CharField(max_length=20, default="заказчик")
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Raboti_pod_kluch(models.Model):
    class Meta:
        db_table="raboti_pod_kluch"
        verbose_name="Работы под ключ"

    ploshad = models.CharField(max_length=20)
    room_type = models.CharField(max_length=20)
    works = models.TextField()
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Santehnika(models.Model):
    class Meta:
        db_table="santehnika"
        verbose_name="Сантехника"
    work_type = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Potolki(models.Model):
    class Meta:
        db_table = "potolki"
        verbose_name = "Потолки"

    ploshad = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    isol = models.CharField(max_length=200)
    svet = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Gipsokarton_peregorodki(models.Model):
    class Meta:
        db_table = "Gipsokarton_peregorodki"
        verbose_name = "Гипсокартонные перегородки"

    ploshad = models.CharField(max_length=20)
    finish = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Remont_vannoy(models.Model):
    class Meta:
        db_table = "Remont_vannoy"
        verbose_name = "Ремонт ванной"
    ploshad = models.CharField(max_length=20)
    plitka = models.CharField(max_length=20)
    santehika = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Reshetki(models.Model):
    class Meta:
        db_table = "Reshetki"
        verbose_name = "Решетки"
    count = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Oboi(models.Model):
    class Meta:
        db_table = "Oboi"
        verbose_name = "Поклейка обоев"
    ploshad = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Beton(models.Model):
    class Meta:
        db_table = "Beton"
        verbose_name = "Бетонные работы"
    ploshad = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)

class Natyazhnoi_potolok(models.Model):
    class Meta:
        db_table = "Natyazhnoi_potolok"
        verbose_name = "Наятяжной потолок"
    ploshad = models.CharField(max_length=20)
    svet = models.CharField(max_length=20)
    details = models.TextField()
    money = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(default=None)
    mailed = models.BooleanField(default=False)


class Work(models.Model):
    class Meta:
        verbose_name="Под-обл. деятельности"
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200, verbose_name="Название")


class Workers(models.Model):
    class Meta:
        db_table="Workers"
        verbose_name="Соискатели"
    def __str__(self):
        return self.surname+" "+self.name
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(verbose_name="E-mail")
    telephone = models.CharField(max_length=20, verbose_name="Телефон")
    SNILS = models.IntegerField(verbose_name="СНИЛС")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    type = models.TextField(default="")
    region = models.CharField(max_length=200, default="")
