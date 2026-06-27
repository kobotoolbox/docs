# Questions numériques dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/number_decimal_range.md" class="reference">23 avr. 2026</a>

Les questions numériques permettent de collecter des données quantitatives telles que des dénombrements, des mesures, des prix ou des évaluations. Elles garantissent que les réponses sont saisies dans un format numérique, ce qui facilite les calculs, les validations et l'analyse des données.

KoboToolbox propose plusieurs types de questions numériques pour répondre à différents besoins de collecte de données, notamment les **nombres entiers, les valeurs décimales** et les **réponses dans une plage définie**.

Cet article présente les types de questions numériques disponibles, explique comment les ajouter et les configurer dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, décrit les options d'apparence applicables et précise les limites propres à chaque plateforme à prendre en compte lors de la collecte de données numériques.

## Types de questions numériques

Les types de questions suivants sont disponibles dans le Formbuilder pour permettre aux répondants de saisir des données numériques :

| Type de question | Description |
|:---|:---|
| <i class="k-icon-qt-number"></i> Chiffre &emsp; &emsp; | Permet aux répondants de saisir des nombres entiers (par exemple, un âge ou un nombre de participants). |
| <i class="k-icon-qt-decimal"></i> Décimale | Permet aux répondants de saisir des nombres pouvant contenir des décimales (par exemple, une superficie ou un prix). |
| <i class="k-icon-qt-range"></i> Intervalle | Permet aux répondants de sélectionner une valeur numérique dans une plage définie par des valeurs minimale et maximale. |

## Ajouter une question numérique dans le Formbuilder

Pour ajouter une question numérique à votre formulaire :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez le libellé de votre question.
4. Cliquez sur **+ AJOUTER UNE QUESTION.**
5. Choisissez le type de question approprié.

![Types de questions numériques](images/number_decimal_range/numeric.png)

### Configurer les questions de type Intervalle

Les questions de type **Intervalle** permettent de collecter des réponses numériques dans une plage définie. Elles affichent une échelle graduée coulissante permettant aux répondants de sélectionner des valeurs comprises entre un minimum et un maximum.

Ce type de question est utile pour collecter des réponses sur une échelle, par exemple des évaluations de satisfaction de 1 à 5 ou des scores dans une plage fixe.

Après avoir ajouté une question de type **Intervalle** dans le Formbuilder, configurez les composants suivants :
- **start** : la valeur numérique minimale de la plage.
- **end** : la valeur numérique maximale de la plage.
- **step** : l'écart entre chaque valeur de la plage.

![Question de type Intervalle](images/number_decimal_range/range.png)

## Apparences des questions numériques

Le tableau ci-dessous présente les apparences par défaut des questions numériques :

![Apparences des questions numériques](images/number_decimal_range/table.png)

### Apparences avancées

Vous pouvez appliquer des apparences avancées aux questions numériques pour modifier leur affichage et leur comportement dans votre formulaire.

Pour ajouter une apparence avancée :
1. Ouvrez les paramètres de la question en cliquant sur <i class="k-icon-settings"></i> **Paramètres** à droite de la question. Vous accédez alors à l'onglet **Options des questions**.
2. Dans **Apparence (avancée)**, saisissez le nom de l'apparence dans le champ de texte, exactement tel qu'il est indiqué ci-dessous.

![Apparence de la question](images/number_decimal_range/appearance.png)

Les apparences avancées suivantes sont disponibles pour les questions numériques :
![Apparence de la question](images/number_decimal_range/table1.png)
![Apparence de la question](images/number_decimal_range/table2.png)

## Limites des questions numériques

Les questions numériques sont soumises à des limites propres à chaque plateforme, qui peuvent affecter la saisie, le stockage et l'export des réponses. Il est important de prendre en compte ces limites lors de la conception de votre formulaire, notamment si vous attendez des nombres de grande taille ou des codes d'identification.

### Limites numériques dans KoboCollect

Dans KoboCollect :

- Les questions de type **Chiffre** sont limitées à 9 caractères.
- Les questions de type **Décimale** sont limitées à 15 caractères.
- Les signes négatifs et les points décimaux sont comptabilisés dans la limite de caractères.

Si une valeur dépasse ces limites, elle ne peut pas être saisie. Cette restriction s'applique au moment de la saisie des données et empêche l'enregistrement de nombres plus longs.

### Limites numériques dans les formulaires web

Les formulaires web KoboToolbox permettent aux répondants de saisir des nombres plus longs, mais des limites s'appliquent à leur stockage :

- Jusqu'à **17 chiffres** sont enregistrés intégralement.
- De **18 à 21 chiffres**, les chiffres supplémentaires sont remplacés par des zéros et la partie décimale est supprimée.
- À partir de **22 chiffres ou plus**, la valeur est automatiquement stockée en notation scientifique.
- Les signes négatifs ne sont pas comptabilisés dans la limite de chiffres.

### Collecter des valeurs numériques longues

Si vous devez collecter des valeurs numériques dépassant ces limites, utilisez une question de type **Texte** plutôt qu'une question de type Chiffre ou Décimale.

Dans les paramètres **Apparence (avancée)** de la question de type Texte, sélectionnez `numbers`. Cela affiche un pavé numérique dans KoboCollect lors de la collecte de données, tout en stockant la valeur sous forme de texte.

Utilisez cette approche lorsque :

- Le nombre risque de dépasser les limites de la plateforme
- La valeur ne doit pas être modifiée ni arrondie
- Le nombre commence par un zéro, comme un numéro de téléphone ou un numéro de compte bancaire

Stocker les valeurs numériques longues sous forme de texte garantit que tous les chiffres, y compris les zéros en tête, sont conservés exactement tels qu'ils ont été saisis.

<p class="note">
   Pour en savoir plus sur l'utilisation des questions de type Texte avec l'apparence <code>numbers</code>, consultez l'article <a href="https://support.kobotoolbox.org/fr/text_questions.html#advanced-appearances">Questions de type texte dans KoboToolbox</a>.
</p>