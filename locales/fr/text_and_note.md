# Types de questions Texte et Note
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/4d3ba5b4639335723af5b5a376159a536c904323/source/text_and_note.md" class="reference">9 mai 2022</a>

Le type de question « Texte » est particulièrement adapté aux questions nécessitant des réponses ouvertes ou non définies, telles que des noms, des commentaires, des explications ou des descriptions.

Le type de question « Note » ne permet pas de saisir une réponse. Il peut être utilisé pour ajouter des instructions ou toute information supplémentaire afin de rendre le questionnaire plus clair ou plus facile à parcourir. Par exemple, vous pouvez l'utiliser pour informer la personne interrogée ou l'enquêtrice ou enquêteur du contenu de la section suivante, fournir un contexte sur les raisons pour lesquelles l'enquête est menée, [afficher différents types de médias](media.md), ou [afficher les résultats de calculs masqués ou les réponses aux questions précédentes](responses_inside_question.md).

## Comment configurer les questions

La configuration des questions de type `text` ou `note` est très similaire :

-   Dans l'interface de création de formulaires, cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question.
-   Saisissez le texte de la question. Par exemple, « Quel est votre nom ? ». Puis cliquez sur **+ AJOUTER UNE QUESTION** (ou appuyez sur Entrée).
-   Choisissez le type de question (« Texte » ou « Note »)

![Configuration des questions de type texte et note](images/text_and_note/text_note_setup.gif)

## Apparence dans les formulaires web et KoboCollect

### Apparence par défaut

![Apparence par défaut des questions texte et note](images/text_and_note/text_note_default_appearance.png)

<p class="note">
  La zone de texte par défaut dans Enketo Webform n'accepte qu'une seule ligne de texte. Cependant, dans KoboCollect, le champ de texte s'agrandit au fur et à mesure que vous tapez. Vous pouvez également ajouter des sauts de ligne pour former des paragraphes
</p>

### Apparences avancées

Vous pouvez modifier l'apparence des questions de type « Texte » dans leurs paramètres.

![Paramètres d'apparence](images/text_and_note/text_appearance_settings.png)

![Apparences avancées pour le texte](images/text_and_note/text_advanced_appearance.png)

## Considérations lors de l'utilisation des questions de type « Texte »

Pour des raisons de qualité des données, il peut être conseillé d'utiliser les [types de questions « Sélection unique » ou « Sélection multiple »](select_one_and_select_many.md) lorsque vous êtes en mesure de prédéfinir une liste de réponses. Limiter les réponses peut faciliter le nettoyage, le traitement et l'analyse des données.

L'utilisation du type de question « Texte » est particulièrement adaptée aux questions ouvertes, lorsque vous ne pouvez pas disposer d'une liste prédéfinie de réponses.

## Utilisation de la logique de question

Étant donné que les réponses aux questions de type « Texte » sont ouvertes, l'utilisation de la logique de question peut être plus difficile et est mieux facilitée par l'utilisation d'« Expressions régulières ».

Avec les expressions régulières (RegEx), vous pouvez mettre en œuvre une logique de validation, comme limiter la longueur des réponses textuelles, restreindre les caractères et la séquence (comme un identifiant unique) ou n'autoriser que les réponses en lettres majuscules.

Pour en savoir plus sur la mise en œuvre des expressions régulières, consultez l'article d'assistance [Restreindre les réponses textuelles avec les expressions régulières](restrict_responses.md)