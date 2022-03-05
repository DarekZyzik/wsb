from CzyInwestowac import *
from inwestyjce import *
from plnusd import *
wiek = int(input('podaj wiek:    '))
plec = str(input('podaj plec:    '))
usd = przeliczenie()
zdolnosc = investments(usd)
can_invest(plec,wiek,zdolnosc)