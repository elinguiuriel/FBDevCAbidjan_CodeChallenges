Challenge Code 2020/04/[22-29]
------------------------------

# Affichage LCD

Votre amie vient d'acheter un nouvel ordinateur. Avant cela, la machine la plus puissante qu'elle ait jamais utilisée était une calculatrice de poche. Elle est un peu déçue car elle aimait beaucoup l'écran LCD ([Liquid Crystal Display](http://www.vintagecalculators.com/html/liquid_crystal_display_calcs.html)) de sa calculatrice, plus que l'écran de son nouvel ordinateur ! Pour la rendre heureuse, écrivez un programme qui affiche des nombres dans un style d'affichage LCD.

### Entrée

L’entrée (passée après lancement du programme) contient plusieurs lignes, une pour chaque numéro à afficher. Chaque ligne contient des entiers _s_ et _n_, où _n_ est le nombre à afficher (0 ≤ _n_ ≤ 99 999 999) et _s_ est la taille avec laquelle il doit être affiché (1 ≤ _s_ ≤ 10). L'entrée se termine par une ligne contenant deux zéros (0 0), qui ne doivent pas être traités.

### Sortie

Affichez les nombres spécifiés dans l'entrée dans un style d'affichage LCD en utilisant s signe "`-`" pour les segments horizontaux et s signes "`|`" pour les segments verticaux. Chaque chiffre occupe exactement _s_ + 2 colonnes et _2s_ + 3 lignes. Assurez-vous de remplir tous les espaces blancs occupés par les chiffres avec des blancs, y compris le dernier chiffre. Il doit y avoir exactement une colonne de blancs entre deux chiffres.
Affichez une ligne vide après chaque numéro. Vous trouverez un exemple de chaque chiffre dans l'exemple de sortie ci-dessous.

Exemple d’entrée:

```
2 12345
3 67890
0 0
```

Exemple de sortie:
```
      --   --         --
   |    |     | |  | |
   |    |     | |  | |
      --   --    --   --
   | |        |    |    |
   | |        |    |    |
      --   --         --
 ---  ---   ---   ---   ---
|        | |   | |   | |   |
|        | |   | |   | |   |
|        | |   | |   | |   |
 ---  ---   ---   ---
|   |    | |   |     | |   |
|   |    | |   |     | |   |
|   |    | |   |     | |   |
 ---        ---   ---   ---
```