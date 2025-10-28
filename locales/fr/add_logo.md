# Ajouter un logo personnalisé
<a href="../add_logo.html">Read in English</a> | <a href="../es/add_logo.html">Leer en español</a> | <a href="../ar/add_logo.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/add_logo.md" class="reference">29 juil. 2025</a>

Ajouter un logo personnalisé en haut de votre formulaire est un processus simple qui suit principalement les mêmes étapes que [l'ajout de contenu média à vos formulaires](media.md).

Pour commencer :

1. Commencez par créer votre fichier image de logo et enregistrez-le avec un nom de fichier court.

2. Dans votre XLSForm, faites de la première question une question de type Note, laissez l'étiquette vide et ajoutez une colonne intitulée `media::image` avec le nom de votre fichier de logo dans la cellule. Comme indiqué ci-dessous :

**feuille survey**

| type | name | label | media::image |
| :--- | :--- | :---- | :----------- |
| note | logo |       | logo.jpg     |
| survey|

3. Lorsque vous avez terminé de modifier le formulaire, importez l'XLSForm dans un projet nouveau ou existant.

4. Déployez ou redéployez votre formulaire, selon qu'il s'agit d'un nouveau projet ou qu'il remplace un formulaire existant.

5. Dans la page de votre projet, allez dans **PARAMÈTRES>MÉDIA** et [importez](media.md) votre fichier `logo.jpg`.

## Conseils :

-   Gardez votre image petite.
-   Votre image de logo n'apparaîtra pas dans l'aperçu du formulaire, seulement lorsque le formulaire sera ouvert.
-   Sauter l'étape finale signifiera que votre formulaire sera affiché sans les fichiers média. Assurez-vous que les fichiers média sont importés avant de télécharger le formulaire sur vos appareils lors de l'utilisation de l'application Android.

<p class="note">Si vous ouvrez l'interface de création de formulaires après avoir déployé votre XLSForm avec le fichier image de logo, elle donnera automatiquement à la question une étiquette de texte et vous devrez la supprimer pour que le texte automatisé n'apparaisse pas à côté de votre logo dans votre formulaire.</p>

`logo.jpg` en faisant glisser le fichier ou en le sélectionnant depuis votre ordinateur.

- Les formats d'image recommandés sont JPEG et PNG. Les images SVG ne sont pas prises en charge.
- Les dimensions recommandées pour les logos sont une largeur de 400 pixels et une hauteur de 100 pixels.

- Gardez votre image petite.
