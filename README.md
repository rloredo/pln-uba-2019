# pln-uba-2019
Introducción al Procesamiento de Lenguaje Natural - UBA 2019

## Ejercicio 1 | stats.py
```console
Basic Statistics
================
sents: 17378
tokens: 517194
words: 46501
tags: 85

Example of word frequency
================
Frequency of "presidente": 682

Example of tag frequency
================
Frequency of "nc0s000": 63452

Most Frequent POS Tags
======================
tag	freq	%	top
sp000	79884	15.45	(de, en, a, del, con)
nc0s000	63452	12.27	(presidente, equipo, partido, país, año)
da0000	54549	10.55	(la, el, los, las, El)
aq0000	33906	6.56	(pasado, gran, mayor, nuevo, próximo)
fc	30147	5.83	(,)
np00000	29111	5.63	(Gobierno, España, PP, Barcelona, Madrid)
nc0p000	27736	5.36	(años, millones, personas, países, días)
fp	17512	3.39	(.)
rg	15336	2.97	(más, hoy, también, ayer, ya)
cc	15023	2.90	(y, pero, o, Pero, e)

Word Ambiguity Levels
=====================
n	words	%	top
1	43972	94.56	(,, con, por, su, El)
2	2318	4.98	(el, en, y, ", los)
3	180	0.39	(de, la, ., un, no)
4	23	0.05	(que, a, dos, este, fue)
5	5	0.01	(mismo, cinco, medio, ocho, vista)
6	3	0.01	(una, como, uno)
7	0	0.00	()
8	0	0.00	()
9	0	0.00	()
```


| Tag    |  Meaning |
|------- | -------- |
|sp000   |  Preposición 
|nc0s000 |  Sustantivo común singular
|da0000  |  Artículo
|aq0000  |  Adjetivo Descriptivo
|fc      |  Coma
|np00000 |  Nombre Propio (sustantivo)
|nc0p000 |  Sustantivo común plural
|fp      |  Punto
|rg      |  Adverbio
|cc      |  Conjunción
