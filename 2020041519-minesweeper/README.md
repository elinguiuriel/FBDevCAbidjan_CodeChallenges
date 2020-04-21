Challenge Code 2020/04/[15-19]
------------------------------

# Le démineur

Avez-vous déjà joué au [démineur](http://demineur.hugames.fr/) ? Le but du jeu est de trouver où toutes les mines sont situées dans un champ de dimensions _M × N_.

Le jeu affiche un nombre dans un carré qui vous indique le nombre de mines adjacentes à ce carré. Chaque carré a au plus huit carrés adjacents.

En considérant le champ 4 × 4 en dessous, la vue à gauche contient deux mines, chacune représentée par un caractère «`*`». Si nous représentons le même champ par les nombres d'indices décrits ci-dessus, nous nous retrouvons avec le champ à droite :
```
* . . .     * 1 0 0
. . . .     2 2 1 0
. * . .     1 * 1 0
. . . .     1 1 1 0
```

### Entrée

L'entrée consistera en un nombre arbitraire de champs. La première ligne de chaque champ contient deux entiers _n_ et _m_ (0 < _n, m_ ≤ 100) qui représentent respectivement le nombre de lignes et de colonnes du champ. Chacune des n lignes suivantes contient exactement m caractères, représentant le champ. 
Les carrés de sécurité sont désignés par «.» et les carrés minés par «`*`», sans les guillemets bien-sûr.

La première ligne de champ où _n_ = _m_ = 0 représente la fin de l'entrée et ne doit pas être traitée.

### Sortie

Pour chaque champ, affichez le message ```Champ #x```: sur une seule ligne, où _x_ représente le numéro du champ à partir de 1. Les n lignes suivantes doivent contenir le champ avec les caractères «.» remplacés par le nombre de mines adjacentes à cette case. Il doit y avoir une ligne vide entre les sorties des champs.

Exemple: 
```
Entrée     |    Sortie
4 4             Cham p #1:
* . . .         * 1 0 0
. . . .         2 2 1 0
. * . .         1 * 1 0
. . . .         1 1 1 0
3 5
* * . . .       Champ #2:
. . . . .       * * 1 0 0
. * . . .       3 3 2 0 0
0 0             1 * 1 0 0
```
