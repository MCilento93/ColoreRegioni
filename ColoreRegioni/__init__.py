# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:31:58 2020

@author: mario
"""

from bs4 import BeautifulSoup as Soup
import requests

class ColoreRegioni():

    url='http://www.governo.it/it/articolo/domande-frequenti-sulle-misure-adottate-dal-governo/15638?gclid=CjwKCAiAwrf-BRA9EiwAUWwKXicC1bzopYynHP9pvRxHUza7Ar4dte9hWHi55Uj4xfuAHanOCf7a1BoCTggQAvD_BwE'
    response = requests.request("GET", url)
    page = response.text[1:-1]
    soup = Soup(page, "html.parser")

    def get_color(onclick):
        if onclick != None:
            if 'rosso' in onclick:
                return 'rosso','🔴'
            elif 'arancione' in onclick:
                return 'arancione','🟠'
            elif 'giallo' in onclick:
                return 'giallo','🟡'
            elif 'verde' in onclick:
                return 'verde','🟢'
        else:
            return None,None

    def __init__(self):
        results={}
        for elem in ColoreRegioni.soup.find_all("path"):
            reg_name=elem.attrs.get('id')
            reg_color,reg_emoji=ColoreRegioni.get_color(elem.attrs.get('onclick'))
            if reg_name:
                results[reg_name]=[reg_color,reg_emoji]
        self.__dict=results
        self.__cambio_denominazione()

    def __cambio_denominazione(self):
        """ Renaming according to istat nomenclature https://www.istat.it/it/archivio/6789 """

        keys_dict={'piemonte':'Piemonte',
                   'veneto':'Veneto',
                   'lombardia':'Lombardia',
                   'emiliaromagna':'Emilia-Romagna',
                   'umbria':'Umbria',
                   'lazio':'Lazio',
                   'toscana':'Toscana',
                   'abruzzo':'Abbruzzo',
                   'molise':'Molise',
                   'basilicata':'Basilicata',
                   'puglia':'Puglia',
                   'marche':'Marche',
                   'sicilia':'Sicilia',
                   'sardegna':'Sardegna',
                   'liguria':'Liguria',
                   'trento':'Trentino-Alto Adige/Südtirol',
                   'bolzano':'Bolzano',
                   'friuliveneziagiulia':'Friuli-Venezia Giulia',
                   'valledaosta':"Valle d'Aosta/Vallée d'Aoste",
                   'campania':'Campania',
                   'calabria':'Calabria'}

        new_dict={}

        for key,value in self.__dict.items():
            new_dict[keys_dict[key]] = self.__dict[key]

        self.__dict=new_dict

    @property
    def denominazioni(self):
        return list(self.__dict.keys())

    @property
    def colori_emoji(self):
        return self.__dict

    @property
    def colori(self):
        colori={}
        for key,value in self.__dict.items():
            colori[key]=value[0]
        return colori

    @property
    def emoji(self):
        emoji={}
        for key,value in self.__dict.items():
            emoji[key]=value[1]
        return emoji

if __name__=='__main__':
    print(f'\nDenominazione regioni: {ColoreRegioni().denominazioni}')
    print(f'\nDizionario completo: {ColoreRegioni().colori_emoji}')
    print(f'\nSolo colori: {ColoreRegioni().colori}')
    print(f'\nSolo emoji: {ColoreRegioni().emoji}')
