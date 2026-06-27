# Question de type Consentement

La question de type « Consentement » affiche une seule option, permettant de sélectionner « OK » dans le formulaire.

Vous pouvez utiliser le type « Consentement » pour les questions qui ne nécessitent que 2 états de réponse : répondu et non répondu, ou accepté et non accepté. Vous pouvez utiliser ce type de question avec un consentement éclairé dans votre formulaire d'enquête, ou comme moyen de s'assurer que la personne interrogée a lu et accepté les conditions, généralement présentées à l'aide d'une [question de type « Note »](question_types.md).

## Configurer la question

1. Dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question.
2. Saisissez le texte de la question. Par exemple, « Si vous acceptez de poursuivre l'enquête, cliquez sur OK. »
3. Cliquez sur « <i class="k-icon k-icon-plus"></i> AJOUTER UNE QUESTION » (ou appuyez sur la touche Entrée du clavier).
4. Choisissez le type de question « <i class="k-icon k-icon-qt-acknowledge"></i> Consentement ».

![Ajout de la question de type Consentement](images/acknowledge/acknowledge_adding.gif)

## Affichage dans les formulaires web et KoboCollect

La question de type « Consentement » affiche un seul bouton radio avec le libellé « OK », comme illustré ci-dessous :

![Questions de type Consentement dans KoboCollect et Enketo](images/acknowledge/acknowledge.png)

## Utiliser la logique de saut et les critères de validation

Une question de type « Consentement » ne comporte que 2 états de réponse : l'un où la question a reçu une réponse, et l'autre où elle n'en a pas reçu, c'est-à-dire que la valeur de la réponse est soit « OK », soit _vide_.

![Questions de type Consentement dans la logique de saut](images/acknowledge/acknowledge_skip.gif)

Dans l'exemple ci-dessus, le groupe « Survey » ne s'affiche que si la question de type « Consentement » a reçu une réponse (l'utilisateur a cliqué sur OK).

Voici la logique de formulaire équivalente en syntaxe XLSForm :

**onglet survey**

| type        | name    | label                                                                  | relevant          |
| :---------- | :------ | :--------------------------------------------------------------------- | :---------------- |
| acknowledge | consent | Si vous acceptez de poursuivre l'enquête, cliquez sur OK               |                   |
| begin_group | survey  | Survey                                                                 | ${consent} = "OK" |
| text        | name    | Quel est votre nom ?                                                   |                   |
| integer     | age     | Quel est votre âge ?                                                   |                   |
| end_group   |         |                                                                        |                   |
| survey |

<p class="note">
  Vous pouvez télécharger l'exemple de XLSForm
  <a
    download
    class="reference"
    href="./_static/files/acknowledge/acknowledge.xlsx"
    >ici <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>