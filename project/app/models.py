from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    Tanks = 'SP'
    Hillers = 'CS'
    DD = 'DD'
    Market_man = 'MM'
    Hild_master = 'HM'
    Kvest_GIver = 'KG'
    Blakcsmith = 'BS'
    Skin_Maker = 'SM'
    Poison_maker = 'PM'
    Master_of_magik = 'MOM'
    CATEGORIES = (
        (Tanks, 'Танки'),
        (Hillers, 'Хилы'),
        (Market_man, 'Тогровцы'),
        (Hild_master, 'Гилдмастеры'),
        (Kvest_GIver, 'Квестгиверы'),
        (Blakcsmith, 'Кузнецы'),
        (Skin_Maker, 'Кожевенники'),
        (Poison_maker, 'Зельевары'),
        (Master_of_magik, 'Мастера заклинаний')

    )

    choises_field = models.CharField(choices=CATEGORIES, default=Tanks, max_length=3)

class Ad(models.Model):

    owner = models.ForeignKey(User, related_name='ads', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Response(models.Model):
    ad = models.ForeignKey(Ad, related_name='responses', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='responses', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
