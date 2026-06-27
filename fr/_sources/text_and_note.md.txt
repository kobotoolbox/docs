# Questions de type texte et note

Le type de question "Texte" est particulièrement adapté aux questions nécessitant des réponses libres ou ouvertes, telles que des noms, des commentaires, des explications ou des descriptions.

Le type de question "Note" ne permet pas de saisir une valeur de réponse ; il peut en revanche être utilisé pour ajouter des instructions ou toute information complémentaire afin de rendre le formulaire plus clair ou plus facile à parcourir. Par exemple, vous pouvez l'utiliser pour informer les répondants ou les enquêteurs du contenu de la section de questions suivante, fournir un contexte de fond expliquant pourquoi le formulaire est réalisé, [afficher différents types de médias](media.md) ou [afficher les résultats de calculs masqués ou les réponses à des questions précédentes](responses_inside_question.md).

## Configurer les questions

La configuration des questions de type `text` ou `note` est très similaire :

-   Dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question.
-   Saisissez le texte de la question. Par exemple, « Quel est votre nom ? ». Cliquez ensuite sur **+ ADD QUESTION** (ou appuyez sur Entrée).
-   Choisissez le type de question (« Texte » ou « Note »).

![Configurer les questions de type texte et note](images/text_and_note/text_note_setup.gif)

## Apparence dans les formulaires web et KoboCollect

### Apparence par défaut

![Apparence par défaut des questions de type texte et note](images/text_and_note/text_note_default_appearance.png)

<p class="note">
  La zone de texte par défaut dans Enketo Webform n'accepte qu'une seule ligne de texte. Dans KoboCollect, en revanche, le champ de texte s'agrandit au fur et à mesure de la saisie. Vous pouvez également ajouter des sauts de ligne pour former des paragraphes.
</p>

### Apparences avancées

Vous pouvez modifier l'apparence des questions de type « Texte » dans ses paramètres.

![Paramètres d'apparence](images/text_and_note/text_appearance_settings.png)

![Apparences avancées pour le texte](images/text_and_note/text_advanced_appearance.png)

## Considérations lors de l'utilisation des questions de type « Texte »

Dans un souci de qualité des données, il peut être préférable d'utiliser les [types de questions « Choix unique » ou « Choix multiple »](select_one_and_select_many.md) lorsque vous êtes en mesure de prédéfinir une liste de réponses. Limiter les réponses permet de simplifier le nettoyage, le traitement et l'analyse des données.

Le type de question « Texte » est mieux adapté aux questions ouvertes, pour lesquelles il n'est pas possible de prédéfinir une liste de réponses.

## Utiliser la logique de formulaire

Les réponses aux questions de type « Texte » étant ouvertes, l'utilisation de la logique de formulaire peut s'avérer plus complexe et est facilitée par le recours aux expressions régulières (Regular Expressions).

Grâce aux expressions régulières (regex), vous pouvez mettre en place une logique de validation, par exemple en limitant la longueur des réponses textuelles, en restreignant les caractères et leur séquence (comme un identifiant unique) ou en n'autorisant que les réponses en lettres majuscules.

Pour en savoir plus sur la mise en œuvre des expressions régulières, consultez l'article d'aide [Utiliser des expressions régulières avec XLSForm](restrict_responses.md).