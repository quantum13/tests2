#coding: utf-8
from datetime import datetime
from django.contrib.auth.models import User

from django.db import models

class Test(models.Model):
    TYPES = {
        ('test', u'Тест'),
        ('link', u'Ссылка'),
    }

    name = models.CharField(max_length=150, verbose_name=u'Название')
    description = models.CharField(max_length=750, verbose_name=u'Описание')

    created = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, verbose_name=u'Автор', default=User.objects.filter(is_superuser=True)[0])

    sum_votes = models.IntegerField(default=0)
    type = models.CharField(choices=TYPES, default='test', max_length=4)


class Question(models.Model):
    test = models.ForeignKey(Test, verbose_name='questions')

    text = models.CharField(max_length=350, verbose_name=u'Текст')


class Answer(models.Model):
    question = models.ForeignKey(Test, verbose_name='answers')

    text = models.CharField(max_length=350, verbose_name=u'Текст')
    balls = models.IntegerField(verbose_name=u'Баллы')

class Result(models.Model):
    test = models.ForeignKey(Test, verbose_name='results')

    text = models.TextField(verbose_name=u'Текст')

    min_balls = models.IntegerField(verbose_name=u'От')
    max_balls = models.IntegerField(verbose_name=u'До')



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.CharField(max_length=300)
    nickname = models.CharField(max_length=100)



from social_auth.signals import pre_update
from social_auth.backends.contrib.vkontakte import VKontakteOAuth2Backend


def facebook_extra_values(sender, user, response, details, **kwargs):
    user.first_name = response.get('first_name')
    user.last_name = response.get('last_name')

    profile,created = UserProfile.objects.get_or_create(user=user)
    profile.avatar = response.get('photo')
    profile.nickname = response.get('nickname')
    profile.save()

    return True

pre_update.connect(facebook_extra_values, sender=VKontakteOAuth2Backend)


