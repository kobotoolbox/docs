# Limites des réponses numériques et textuelles

Il existe des contraintes techniques inhérentes à la longueur des réponses dans les questions de type **Chiffre** ou **Texte**.

Les **questions de type Chiffre** peuvent enregistrer jusqu'à 17 chiffres (nombre positif ou négatif). Plus précisément, le nombre le plus grand pouvant être saisi est 2147483647 et le plus petit -2147483648.

Si vous souhaitez une réponse numérique mais avez besoin d'un nombre comportant plus de 9 chiffres (c'est-à-dire supérieur au nombre indiqué ci-dessus) — par exemple pour les numéros de téléphone longs dans certains pays — il existe une astuce. Au lieu d'une question de type Chiffre, ajoutez une question de type Texte à votre formulaire. Ensuite, dans le paramètre d'apparence de la question, définissez-le comme numbers. Le clavier numérique s'affichera alors à la place du clavier de texte standard.

Les **questions de type Texte** (ainsi que les questions de type Code-barres) sont pratiquement illimitées en termes de caractères pouvant être saisis. (La longueur totale du texte doit être inférieure à 1 Mo, ce qui représente plus de 300 pages de texte — bien plus que ce que l'on peut jamais attendre comme réponse à une question.)