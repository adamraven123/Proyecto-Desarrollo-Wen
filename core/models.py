# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import date


POSITION_CHOICE= (  
    ('Base', 'Base'),
    ('Escolta', 'Escolta'),
    ('Alero', 'Alero'),
    ('Ala-pivot','Ala-pivot'),
    ('Pivot','Pivot'),
)

POSITION_DEFAULT = 'Base'

class Team(models.Model):
    name = models.CharField(max_length=100)
    team_description = models.TextField()
    team_img = models.ImageField()
    team_code = models.CharField(max_length=3)
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    nick_name = models.CharField(max_length=240)
    age = models.IntegerField(default=18)
    birth_date = models.DateField(default=date.today)
    rut = models.CharField(max_length=240)
    height = models.IntegerField(default=170)
    weight = models.IntegerField(default=70)
    mail = models.TextField()
    position = models.CharField(
            max_length=9,
            choices= POSITION_CHOICE,
            default= POSITION_DEFAULT
        )
    team = models.ForeignKey(Team,on_delete=models.CASCADE, blank = True, null=True)
    photo = models.ImageField()
    def __str__(self):
        return self.name
    
class Coach(models.Model):
    name = models.CharField(max_length=200)
    mail = models.TextField()
    age = models.IntegerField(default=18)
    nick_name = models.CharField(max_length=240)
    rut = models.CharField(max_length=240)
    team = models.ForeignKey(Team,on_delete=models.CASCADE, blank = True, null=True )
    def __str__(self):
        return self.name

class Match(models.Model):
    match = models.TextField(max_length=200)
    def __str__(self):
        return self.match
