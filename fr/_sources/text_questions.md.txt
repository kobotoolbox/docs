# Questions de type texte dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/text_questions.md" class="reference">23 Apr 2026</a>

Le type de question **Texte** dans KoboToolbox permet aux répondants de saisir des réponses ouvertes dans leurs propres mots. Il est particulièrement adapté lorsque l'éventail des réponses possibles n'est pas prédéfini, par exemple pour collecter des noms, des descriptions, des explications ou des commentaires généraux.

Cet article explique comment ajouter une question de type texte dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, décrit les options d'apparence disponibles et présente les points importants à prendre en compte lors de l'utilisation de ce type de question.

<p class="note">
<strong>Note :</strong> Les questions de type texte peuvent accepter jusqu'à 1 Mo de texte, ce qui équivaut à environ 300 pages.
</p>

## Ajouter une question de type texte dans le Formbuilder

Pour ajouter une question de type texte à votre formulaire :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez le libellé de votre question.
3. Cliquez sur **+ AJOUTER UNE QUESTION**.
4. Choisissez le type de question <i class="k-icon-qt-text"></i> **Texte**.

![Sélectionner le type de question Texte](images/text_questions/text.png)

## Apparences des questions de type texte

Par défaut, les questions de type texte s'affichent sous la forme d'une zone de texte sur une seule ligne.

- Dans les [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html), la zone de texte conserve la même taille quelle que soit la quantité de texte saisie. Elle ne prend pas en charge les sauts de ligne.
- Dans [KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html), la zone de texte s'agrandit au fur et à mesure de la saisie et prend en charge les sauts de ligne, ce qui permet aux répondants de saisir des paragraphes.

![Apparence des questions de type texte dans les formulaires web et KoboCollect](images/text_questions/table.png)

### Apparences avancées

Vous pouvez appliquer des apparences avancées aux questions de type texte pour modifier leur affichage et leur comportement dans votre formulaire.

Pour ajouter une apparence avancée :
1. Ouvrez les paramètres de la question en cliquant sur <i class="k-icon-settings"></i> **Paramètres** à droite de la question. Vous accéderez alors à l'onglet **Options des questions**.
2. Dans **Apparence (avancée)**, choisissez l'apparence souhaitée.
    - Si l'apparence n'est pas répertoriée, sélectionnez **autre** et saisissez le nom de l'apparence dans la zone de texte, exactement tel qu'il est indiqué ci-dessous.

![Choisir l'apparence d'une question de type texte](images/text_questions/appearance.png)

Les apparences suivantes sont disponibles pour les questions de type texte :

| Apparence | Description | Compatibilité |
|:---|:---|:---|
| `multiline` | Affiche une zone de texte plus grande pour les réponses textuelles longues.<br>![Apparence multiline](images/text_questions/multiline.png) | Formulaires web et KoboCollect |
| `numbers` | Affiche un clavier numérique à la place du clavier textuel (par exemple, pour collecter des numéros de téléphone).<br>![Apparence numbers](images/text_questions/numbers.png) | KoboCollect uniquement |
| `url` (autre) | Affiche une URL cliquable (formulaires web) ou un bouton **Open URL** (KoboCollect) sous le texte de la question et rend la question en lecture seule. Saisissez l'URL dans le paramètre **Réponse par défaut** de la question.<br>![Apparence url](images/text_questions/url.png) | Formulaires web et KoboCollect |
| `masked` (autre) | Masque le texte saisi par le répondant (par exemple, un mot de passe ou des informations confidentielles).<br>![Apparence masked](images/text_questions/masked.png) | KoboCollect uniquement |

<p class="note">
<strong>Note :</strong> Utilisez l'apparence <code>numbers</code> pour saisir des valeurs numériques devant être stockées sous forme de texte. Cela est particulièrement important pour les valeurs commençant par un zéro, comme les numéros de téléphone ou les numéros de compte bancaire, afin de préserver le zéro initial.
</p>

## Bonnes pratiques pour l'utilisation des questions de type texte

Les questions de type texte doivent être utilisées pour les réponses ouvertes, lorsqu'il n'est pas possible de proposer une liste prédéfinie d'options de réponse. Si vous êtes en mesure de définir un ensemble fixe de réponses, envisagez d'utiliser les types de questions **Choix unique** ou **Choix multiple**. Limiter les réponses peut améliorer la qualité des données et faciliter leur nettoyage, leur traitement et leur analyse.

<p class="note">
  Pour plus d'informations, consultez l'article <a href="https://support.kobotoolbox.org/fr/select_one_and_select_many.html">Questions à choix multiple dans KoboToolbox</a>.
</p>

### Utiliser les questions de type texte dans la logique de formulaire

Les réponses textuelles étant ouvertes, l'application d'une [logique de saut](https://support.kobotoolbox.org/fr/skip_logic.html) ou de [critères de validation](https://support.kobotoolbox.org/fr/validation_criteria.html) peut s'avérer plus complexe.

Vous pouvez utiliser des **expressions régulières** pour valider et contrôler la saisie de texte. Par exemple, vous pouvez :

- Limiter le nombre de caractères dans une réponse
- Restreindre les caractères aux chiffres ou aux lettres majuscules
- Imposer un format spécifique, tel qu'un identifiant unique

<p class="note">
  Pour plus d'informations, consultez l'article <a href="https://support.kobotoolbox.org/fr/restrict_responses.html">Utiliser des expressions régulières avec XLSForm</a>.
</p>

Vous pouvez également utiliser des **fonctions de chaîne de caractères** dans les calculs pour manipuler des valeurs textuelles, notamment pour :

- Combiner plusieurs chaînes de caractères
- Convertir des caractères minuscules en majuscules
- Extraire une partie spécifique d'une chaîne
- Retourner la longueur en caractères d'une chaîne

<p class="note">
  Pour plus d'informations, consultez l'article <a href="https://support.kobotoolbox.org/fr/functions_xls.html#functions-to-manipulate-strings">Utiliser des fonctions avec XLSForm</a>.
</p>