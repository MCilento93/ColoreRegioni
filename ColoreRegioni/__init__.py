# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:31:58 2020

@author: mario
"""

from bs4 import BeautifulSoup as Soup
import urllib.request

class ColoreRegioni():

    url='http://www.governo.it/it/articolo/domande-frequenti-sulle-misure-adottate-dal-governo/15638?gclid=CjwKCAiAwrf-BRA9EiwAUWwKXicC1bzopYynHP9pvRxHUza7Ar4dte9hWHi55Uj4xfuAHanOCf7a1BoCTggQAvD_BwE'
    req = urllib.request.Request(url)#, headers=self.headers)
    response = urllib.request.urlopen(req)
    page = response.read()
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

if __name__=='__main__':
    print(f'Dizionario completo: {ColoreRegioni().colori_emoji}')
    print(f'Solo colori: {ColoreRegioni().colori}')
    print(f'Denominazione regioni: {ColoreRegioni().denominazioni}')
