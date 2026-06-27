# Ajouter un logo personnalisé
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/add_logo.md" class="reference">29 Jul 2025</a>


Ajouter un logo personnalisé en haut de votre formulaire est une opération simple qui suit essentiellement les mêmes étapes que l'[ajout de contenu multimédia à vos formulaires](media.md).

Pour commencer :

1. Créez votre fichier image de logo et enregistrez-le avec un nom de fichier court.

2. Dans votre XLSForm, définissez la première question comme une question de type Note, laissez le libellé vide et ajoutez une colonne intitulée `media::image` avec le nom de votre fichier logo dans la cellule. Comme indiqué ci-dessous :

**onglet survey**

| type | name | label | media::image |
| :--- | :--- | :---- | :----------- |
| note | logo |       | logo.jpg     |
| survey|

3. Une fois les modifications apportées au formulaire, importez le XLSForm dans un projet nouveau ou existant.

4. Déployez ou redéployez votre formulaire, selon qu'il s'agit d'un nouveau projet ou qu'il remplace un formulaire existant.

5. Sur la page de votre projet, accédez à **PARAMÈTRES > MÉDIAS** et [importez](media.md) votre fichier `logo.jpg`.

## Conseils :

-   Gardez votre image de petite taille.
-   L'image de votre logo n'apparaîtra pas dans l'aperçu du formulaire, mais uniquement lorsque le formulaire sera ouvert.
-   Si vous omettez la dernière étape, votre formulaire s'affichera sans les fichiers multimédias. Assurez-vous que les fichiers multimédias sont importés avant de télécharger le formulaire sur vos appareils lorsque vous utilisez l'application Android.

<p class="note">Si vous ouvrez l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong> après avoir déployé votre XLSForm avec le fichier image du logo, un libellé textuel sera automatiquement attribué à la question et vous devrez le supprimer pour éviter que ce texte automatique n'apparaisse à côté de votre logo dans le formulaire.</p>