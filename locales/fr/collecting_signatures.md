# Type de question Signature

Certains formulaires peuvent nécessiter l'inclusion de signatures. Vous pouvez utiliser l'apparence `signature` aussi bien dans l'application Android KoboCollect que dans Enketo. Le widget draw n'est disponible que lors de l'utilisation d'Enketo pour la collecte de données.

## Application Android KoboCollect

KoboCollect permet de collecter une signature numérique directement sur l'écran du téléphone ou de la tablette.

Pour ajouter cette fonctionnalité à votre formulaire :

1. Ouvrez ou téléchargez la version XLS de votre formulaire.
2. Créez la question et définissez le type comme `image`.
3. Définissez l'apparence comme `signature`.

## Enketo

Les signatures numériques fonctionnent également dans les formulaires web Enketo, où vous avez la possibilité supplémentaire d'utiliser un widget draw pour collecter des signatures. Dans votre XLSForm, ajoutez simplement `signature` ou `draw` dans la colonne `appearance` pour une question de type `image`.

**onglet survey**

| type  | name | label            | appearance | hint                             |
| :---- | :--- | :--------------- | :--------- | :------------------------------- |
| image | draw | Draw widget      | draw       | Image type with draw appearance  |
| image | sign | Signature widget | signature  | Image type with signature widget |
| survey |

[Suivez ce lien](https://enke.to/draw) pour tester la différence entre les widgets draw (dessin) et signature.

## Créer une question de type Signature dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**

1. Créez une nouvelle question et sélectionnez Photographie comme type de question.

![image](/images/collecting_signatures/new_question.jpg)

2. Dans les Paramètres sous Options de questions, cliquez sur le menu déroulant Apparence et sélectionnez signature.

![image](/images/collecting_signatures/signature.jpg)