# Type de question Signature
<a href="../collecting_signatures.html">Read in English</a> | <a href="../es/collecting_signatures.html">Leer en español</a> | <a href="../ar/collecting_signatures.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/collecting_signatures.md" class="reference">29 juil. 2025</a>

Certains formulaires peuvent nécessiter l'inclusion de signatures. Vous pouvez utiliser l'apparence `signature` à la fois sur l'application Android Collect et sur Enketo. Le widget de dessin n'est disponible que lors de l'utilisation d'Enketo pour la collecte de données.

## Application Android Collect

Collect permet de collecter une signature numérique directement sur l'écran du téléphone/de la tablette.

Pour ajouter ceci à votre formulaire :

1. Ouvrez ou téléchargez la version XLS de votre formulaire.
2. Créez la question et définissez le type comme `image`
3. Définissez l'apparence sur `signature`

## Enketo

Les signatures numériques fonctionnent également sur les formulaires web Enketo, où vous avez l'option supplémentaire d'utiliser un widget de dessin pour collecter des signatures. Dans votre XLSForm, ajoutez simplement `signature` ou `draw` dans la colonne `appearance` pour une question de type `image`.

**Feuille survey**

| type  | name | label            | appearance | hint                                       |
| :---- | :--- | :--------------- | :--------- | :----------------------------------------- |
| image | draw | Widget de dessin | draw       | Type image avec apparence draw             |
| image | sign | Widget signature | signature  | Type image avec widget signature           |
| survey |

[Suivez ce lien](https://enke.to/draw) pour tester la différence entre les widgets de dessin et de signature.

## Créer un type de question Signature dans l'interface de création de formulaires

1. Créez une nouvelle question et sélectionnez Photo comme type de question.

![image](/images/collecting_signatures/new_question.jpg)

2. Dans les Paramètres sous Options de question, cliquez sur le menu déroulant Apparence et sélectionnez Signature.

![image](/images/collecting_signatures/signature.jpg)