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



## Ejercicio 2 | baseline.py

### Resultados de dumb tagger (etiqueta todo como nc0s000)

Accuracy: 12.65% / 0.00% / 12.65% (total / known / unk)

|g \ m  |sp000  |nc0s000        |da0000 |aq0000 |fc     |nc0p000        |rg     |np00000        |fp     |cc
|:-------:      |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:
|**sp000**|     -|      14.39|  -|      -|      -|      -|      -|      -|      -|      -|      
|**nc0s000**|   -|      12.65|  -|      -|      -|      -|      -|      -|      -|      -|      
|**da0000**|    -|      9.70|   -|      -|      -|      -|      -|      -|      -|      -|      
|**aq0000**|    -|      7.28|   -|      -|      -|      -|      -|      -|      -|      -|      
|**fc**|        -|      5.85|   -|      -|      -|      -|      -|      -|      -|      -|      
|**nc0p000**|   -|      5.53|   -|      -|      -|      -|      -|      -|      -|      -|      
|**rg**|        -|      3.73|   -|      -|      -|      -|      -|      -|      -|      -|      
|**np00000**|   -|      3.58|   -|      -|      -|      -|      -|      -|      -|      -|      
|**fp**|        -|      3.55|   -|      -|      -|      -|      -|      -|      -|      -|      
|**cc**|        -|      3.41|   -|      -|      -|      -|      -|      -|      -|      -|


### Resultados de baseline (etiqueta con la etiqueta más frecuente)
Accuracy: 87.58% / 95.27% / 18.01% (total / known / unk)

|g \ m  |sp000  |nc0s000        |da0000 |aq0000 |fc     |nc0p000        |rg     |np00000        |fp     |cc
|:-------:      |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:
|**sp000**|     14.28|  0.05|   -|      -|      -|      -|      0.01|   -|      -|      -|      
|**nc0s000**|   0.00|   12.22|  -|      0.25|   -|      0.00|   0.03|   0.00|   -|      0.00|   
|**da0000**|    -|      0.15|   9.54|   -|      -|      -|      -|      -|      -|      -|      
|**aq0000**|    0.01|   2.05|   -|      4.84|   -|      0.13|   0.00|   -|      -|      -|      
|**fc**|        -|      -|      -|      -|      5.85|   -|      -|      -|      -|      -|      
|**nc0p000**|   -|      1.24|   -|      0.20|   -|      4.09|   -|      -|      -|      -|      
|**rg**|        0.02|   0.31|   -|      0.04|   -|      -|      3.27|   -|      -|      0.02|   
|**np00000**|   0.00|   2.05|   -|      0.00|   -|      0.00|   -|      1.52|   -|      0.00|   
|**fp**|        -|      -|      -|      -|      -|      -|      -|      -|      3.55|   -|      
|**cc**|        0.00|   0.01|   -|      -|      -|      -|      0.05|   0.00|   -|      3.34|

## Ejercicio 3 | classifier.py

### Linear regression
Training time: 236.8 secs

Eval time: 2.04 secs

Accuracy: 91.69% / 95.01% / 61.68% (total / known / unk)

|g \ m  |sp000  |nc0s000        |da0000 |aq0000 |fc     |nc0p000        |rg     |np00000        |fp     |cc
|:-------:      |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:
|**sp000**|     14.26|  0.01|   -|      0.05|   -|      -|      0.01|   0.00|   -|      -|      
|**nc0s000**|   0.00|   11.89|  0.01|   0.52|   -|      0.02|   0.02|   0.09|   -|      -|      
|**da0000**|    -|      0.11|   9.50|   0.01|   -|      0.01|   -|      0.01|   -|      -|      
|**aq0000**|    0.00|   0.51|   -|      6.43|   -|      0.17|   0.01|   0.06|   -|      -|      
|**fc**|        -|      -|      -|      -|      5.85|   -|      -|      -|      -|      -|      
|**nc0p000**|   -|      0.35|   -|      0.46|   -|      4.61|   -|      0.04|   -|      -|      
|**rg**|        0.02|   0.04|   0.00|   0.39|   -|      0.00|   3.11|   0.03|   -|      0.02|   
|**np00000**|   -|      0.22|   -|      0.08|   -|      0.01|   -|      3.24|   -|      0.00|   
|**fp**|        -|      -|      -|      -|      -|      -|      -|      -|      3.55|   -|      
|**cc**|        0.00|   0.00|   -|      0.01|   -|      0.00|   0.05|   0.00|   -|      3.34|  

### Support-vector machine (SVM)
Training time: 66.2 secs

Eval time: 2.05 secs

Accuracy: 94.11% / 97.57% / 62.76% (total / known / unk)

|g \ m  |sp000  |nc0s000        |da0000 |aq0000 |fc     |nc0p000        |rg     |np00000        |fp     |cc
|:-------:      |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:
|**sp000**|     14.30|  0.00|   -|      0.03|   -|      -|      0.00|   -|      -|      -|      
|**nc0s000**|   0.00|   12.09|  0.01|   0.33|   -|      0.02|   0.02|   0.08|   -|      0.00|   
|**da0000**|    -|      0.08|   9.53|   -|      -|      0.00|   -|      0.00|   -|      -|      
|**aq0000**|    0.00|   0.34|   -|      6.61|   -|      0.15|   0.01|   0.05|   -|      -|      
|**fc**|        -|      -|      -|      -|      5.85|   -|      -|      -|      -|      -|      
|**nc0p000**|   -|      0.25|   -|      0.31|   -|      4.90|   -|      0.04|   -|      -|      
|**rg**|        0.02|   0.02|   0.00|   0.21|   -|      0.01|   3.35|   0.01|   -|      0.02|   
|**np00000**|   0.00|   0.21|   -|      0.08|   -|      0.01|   -|      3.26|   -|      0.00|   
|**fp**|        -|      -|      -|      -|      -|      -|      -|      -|      3.55|   -|      
|**cc**|        0.00|   -|      -|      0.01|   -|      -|      0.05|   0.00|   -|      3.34|   

### Naive bayes classifier (NBC)
Training time: 6.5 secs

Eval time: 131.28 secs

Accuracy: 84.28% / 88.07% / 49.99% (total / known / unk)

|g \ m  |sp000  |nc0s000        |da0000 |aq0000 |fc     |nc0p000        |rg     |np00000        |fp     |cc
|:-------:      |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:  |:-----------:
|**sp000**|     14.31|  -|      0.01|   0.00|   0.00|   0.00|   0.00|   0.00|   -|      -|      
|**nc0s000**|   0.05|   12.05|  0.07|   0.09|   0.02|   0.01|   0.00|   0.29|   -|      0.00|   
|**da0000**|    0.00|   0.14|   9.52|   0.00|   0.00|   0.00|   -|      0.01|   -|      -|      
|**aq0000**|    0.22|   0.88|   0.19|   5.11|   0.14|   0.23|   0.01|   0.40|   0.00|   0.01|   
|**fc**|        0.00|   -|      -|      -|      5.85|   -|      -|      0.00|   -|      -|      
|**nc0p000**|   0.06|   0.28|   0.17|   0.07|   0.02|   4.64|   0.00|   0.26|   -|      0.00|   
|**rg**|        0.20|   0.17|   0.08|   0.14|   0.04|   0.01|   2.77|   0.23|   -|      0.02|   
|**np00000**|   0.03|   0.27|   0.05|   0.00|   0.00|   0.01|   0.00|   3.21|   -|      -|      
|**fp**|        0.00|   -|      -|      -|      -|      -|      -|      -|      3.55|   -|      
|**cc**|        0.01|   0.00|   0.00|   -|      -|      0.00|   0.05|   0.05|   -|      3.29|


## Ejercicio 4

Ver Ejercicio_4.ipynb