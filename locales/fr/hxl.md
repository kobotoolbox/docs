# Utilisation des balises HXL
<a href="../hxl.html">Read in English</a> | <a href="../es/hxl.html">Leer en español</a> | <a href="../ar/hxl.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/hxl.md" class="reference">29 juil. 2025</a>

## Qu'est-ce que HXL exactement ?

HXL signifie **Humanitarian Exchange Language** (langage d'échange humanitaire). L'objectif de HXL est d'améliorer le partage d'informations lors d'une crise humanitaire en créant un moyen simple de promouvoir l'interopérabilité des données. Il le fait en codant les données par des hashtags (#) similaires à Twitter. Pour plus d'informations sur HXL, veuillez [consulter ce lien](https://hxlstandard.org).

## Comment utiliser la fonctionnalité HXL dans l'interface de création de formulaires

_Crédits : [David Megginson](http://www.megginson.com)_ _Lien vers le [guide pas à pas sous forme de diaporama](https://docs.google.com/presentation/d/123bHSkNh4T30CNq0i37IxOLfrqSC-3V_Khtkf6bIdg0/edit#slide=id.p)_

1. Après avoir commencé un formulaire et créé une question, allez dans les Paramètres de la question et dans l'onglet Options de la question, choisissez votre balise HXL et ajoutez des attributs.

    ![image](/images/hxl/hxl.gif)

2. Une fois le formulaire créé, le projet déployé et les données collectées, allez dans l'onglet Téléchargements de la page DONNÉES. Sélectionnez le type d'export XLS et assurez-vous de sélectionner **Valeurs et en-têtes XML** pour le format de valeur et d'en-tête. Puis Exportez.

    ![image](/images/hxl/xml_values.gif)

3. Une fois que vous avez exporté et téléchargé les données sur votre ordinateur, ouvrez le fichier XLS pour voir vos balises HXL. Il est normal d'avoir des métadonnées Kobo qui n'ont pas de hashtags HXL.

    ![image](/images/hxl/xls_affected.jpg)

<p class="note">Le hashtag avant le nom est obligatoire et les espaces ne sont pas autorisés.</p>

## Comment utiliser HXL dans un XLSForm

Lors de la création d'un XLSForm, insérez simplement une colonne supplémentaire dans n'importe quelle feuille de calcul existante et remplissez-la avec des hashtags HXL identifiant le type d'information dans chaque colonne.

**Feuille survey**

| type                 | name     | label                                        | hxl        |
| :------------------- | :------- | :------------------------------------------- | :--------- |
| select_one countries | country  | Sélectionnez le pays affecté                 | #country   |
| select_one admin1    | province | Veuillez sélectionner la province            | #adm1+code |
| select_one admin2    | county   | Sélectionnez le comté                        | #adm2+name |
| select_one sector    | cluster  | Cluster                                      | #sector    |
| integer              | affected | Nombre de personnes affectées                | #affected  |
| integer              | reached  | Nombre de personnes atteintes à ce jour      | #reached   |
| survey |