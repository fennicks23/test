a = 'Hello world'
room_301 = ['Aidar','Beka','Rozya', 'Doni','Mara','Adi','Bekbolot', 'Abdul', 'Tima', 'Husan']
team= ['eliza', 'Agil','Nurdic', 'Azamat','Dair', 'Nazgul','Egida', 'Aidai', 'Olga', 'Bekmamat', 'Dias','Husan']
team1 = []
team2 = []
team3 = []

from random import random, choice as ch, sample
from time import sleep
a = (team1,team2,team3)
while len(a) != 4 :
    team1.append(ch(team))
    team2.append(ch(team))
    team3.append(ch(team))
print(team3,team2,team1)
sleep(0.1)