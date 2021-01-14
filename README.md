
# ColoreRegioni
[![Build Status](https://travis-ci.com/MCilento93/ColoreRegioni.svg)](https://travis-ci.com/MCilento93/ColoreRegioni)
[![Coverage Status](https://coveralls.io/repos/github/MCilento93/ColoreRegioni/badge.svg)](https://coveralls.io/github/MCilento93/ColoreRegioni)
[![PyPI](https://img.shields.io/pypi/v/ColoreRegioni)](https://pypi.org/project/ColoreRegioni/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ColoreRegioni)](https://pypistats.org/packages/coloreregioni)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ColoreRegioni)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ColoreRegioni)
![GitHub contributors](https://img.shields.io/github/contributors/MCilento93/ColoreRegioni)
![GitHub issues](https://img.shields.io/github/issues-raw/MCilento93/ColoreRegioni)
![GitHub](https://img.shields.io/github/license/MCilento93/ColoreRegioni)

Web-scraping del [sito del governo italiano](http://www.governo.it/it/articolo/domande-frequenti-sulle-misure-adottate-dal-governo/15638?gclid=CjwKCAiAwrf-BRA9EiwAUWwKXicC1bzopYynHP9pvRxHUza7Ar4dte9hWHi55Uj4xfuAHanOCf7a1BoCTggQAvD_BwE) per la classificazione delle misure restrittive regionali per COVID-19.
Denominazione regione in accordo a [nomenclatura istat](https://www.istat.it/it/archivio/6789).

# Installazione
```
pip install ColoreRegioni
```

# Utilizzo
La classe ColoreRegioni() restituisce il dizionario con il colore e la corrispondente emoji:
```
from ColoreRegioni import ColoreRegioni

colore_regioni=ColoreRegioni()
full_dict=colore_regioni.colori_emoji
```
![full_dict](https://github.com/MCilento93/ColoreRegioni/blob/main/images/full_dict.png?raw=true)</br>
Disponibili anche i risultati parziali:
```
denominazioni=colore_regioni.denominazioni
dict_only_colors=colore_regioni.colori
dict_only_emoji=colore_regioni.emoji
```

# Licenza
Il software è liceziato con licenza [MIT](LICENSE) (c) 2020 GitHub, Inc.
