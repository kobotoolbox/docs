# Type de question Acknowledge
<a href="../acknowledge.html">Read in English</a> | <a href="../es/acknowledge.html">Leer en español</a> | <a href="../ar/acknowledge.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/cbfd264f05913df75ec184d5d9eb002f6e66f905/source/acknowledge.md" class="reference">17 juil. 2025</a>

Le type de question « Acknowledge » affiche une seule option, pour sélectionner « OK » sur le
formulaire.

Vous pouvez utiliser le type « Acknowledge » pour les questions qui ne nécessitent que 2 états de
réponse : répondu et non répondu, ou accepté et non accepté. Vous pourriez utiliser
ce type de question avec un consentement éclairé dans votre formulaire d'enquête, ou comme moyen de
vous assurer que la personne interrogée a lu et accepte les conditions, généralement
décrites à l'aide d'un [type de question « Note »](question_types.md).

## Comment configurer la question

1. Dans l'interface de création de formulaires, cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour
   ajouter une nouvelle question.
2. Saisissez le texte de la question. Par exemple, « Si vous acceptez de poursuivre l'enquête, cliquez sur OK. »
3. Cliquez sur « <i class="k-icon k-icon-plus"></i> ADD QUESTION » (ou appuyez sur la touche Entrée
   du clavier).
4. Choisissez le type de question « <i class="k-icon k-icon-qt-acknowledge"></i> Acknowledge ».

![Ajout de la question acknowledge](images/acknowledge/acknowledge_adding.gif)

## Comment elle s'affiche dans les formulaires web et KoboCollect

La question « Acknowledge » affiche un seul bouton radio avec l'étiquette « OK » comme
illustré ci-dessous :

![Questions Acknowledge dans KoboCollect et Enketo](images/acknowledge/acknowledge.png)

## Utilisation de la logique de saut et des critères de validation

Une question « Acknowledge » n'a que 2 états de réponse : un où la question
est répondue, et un où elle ne l'est pas, c'est-à-dire que la valeur de réponse est soit « OK » soit
_vide_.

![Questions Acknowledge dans la logique de saut](images/acknowledge/acknowledge_skip.gif)

Dans l'exemple ci-dessus, le groupe « Survey » ne sera affiché que si la
question « Acknowledge » a été répondue (l'utilisatrice ou l'utilisateur a cliqué sur OK).

Ci-dessous se trouve la logique de formulaire équivalente en syntaxe XLSForm :

**feuille survey**

| type        | name    | label                                              | relevant          |
| :---------- | :------ | :------------------------------------------------- | :---------------- |
| acknowledge | consent | If you agree to continue with the survey, click OK |                   |
| begin_group | survey  | Survey                                             | ${consent} = "OK" |
| text        | name    | What is your name?                                 |                   |
| integer     | age     | How old are you?                                   |                   |
| end_group   |         |                                                    |                   |
| survey |

<p class="note">
  Vous pouvez télécharger l'exemple XLSForm
  <a
    download
    class="reference"
    href="./_static/files/acknowledge/acknowledge.xlsx"
    >ici <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>