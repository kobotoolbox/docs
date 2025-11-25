# Limites des réponses numériques et textuelles
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/0c5dd6987a26369bd16e779f6ee2ad77e2243b26/source/number_text_responses.md" class="reference">21 juin 2020</a>

Il existe des contraintes techniques sous-jacentes à la longueur de la réponse dans une question de type **Nombre** ou **Texte**.
 
Les **questions de type Nombre** peuvent enregistrer jusqu'à 17 chiffres (nombre positif ou négatif). Pour être exact, le nombre le plus grand qui peut être saisi est 2147483647 et le plus petit -2147483648.
 
Si vous souhaitez une réponse numérique mais avez besoin d'un nombre avec plus de 9 chiffres (c'est-à-dire plus grand que celui indiqué ci-dessus) - par exemple pour de longs numéros de téléphone dans certains pays - vous pouvez utiliser une astuce. Au lieu d'une question de type Nombre, ajoutez une question de type Texte à votre formulaire. Ensuite, dans le paramètre Apparence de la question, définissez-le sur nombres. Cela affichera le clavier numérique au lieu du clavier de texte standard.

Les **questions de type Texte** (ainsi que les questions de type Code-barres) sont presque illimitées en termes de caractères pouvant être saisis. (La longueur totale du texte doit être inférieure à 1 Mo, ce qui représente plus de 300 pages de texte - plus que ce qui peut jamais être attendu dans une réponse à une question.)