# Utiliser les balises HXL

## Qu'est-ce que HXL exactement ?

HXL est l'acronyme de **Humanitarian Exchange Language** (langage d'échange humanitaire). L'objectif de HXL est d'améliorer le partage d'informations lors d'une crise humanitaire en créant un moyen simple de favoriser l'interopérabilité des données. Pour ce faire, les données sont codées à l'aide de hashtags (#) similaires à ceux utilisés sur Twitter. Pour plus d'informations sur HXL, veuillez [consulter ce lien](https://hxlstandard.org).

## Comment utiliser la fonctionnalité HXL dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder)

_Crédits : [David Megginson](http://www.megginson.com)_ _Lien vers le [guide pas à pas en diapositives](https://docs.google.com/presentation/d/123bHSkNh4T30CNq0i37IxOLfrqSC-3V_Khtkf6bIdg0/edit#slide=id.p)_

1. Après avoir commencé un formulaire et créé une question, accédez aux paramètres de la question et, dans l'onglet Options des questions, choisissez votre balise HXL et ajoutez des attributs.

    ![image](/images/hxl/hxl.gif)

2. Une fois le formulaire créé, le projet déployé et les données collectées, accédez à l'onglet Téléchargements dans la page Données. Sélectionnez XLS comme type d'exportation et veillez à sélectionner **Valeurs et en-tête XML** pour le format des valeurs et de l'en-tête. Cliquez ensuite sur Exporter.

    ![image](/images/hxl/xml_values.gif)

3. Une fois les données exportées et téléchargées sur votre ordinateur, ouvrez le fichier XLS pour voir vos balises HXL. Il est normal que les métadonnées KoboToolbox ne comportent pas de hashtags HXL.

    ![image](/images/hxl/xls_affected.jpg)

<p class="note">Le hashtag avant le nom est obligatoire et les espaces ne sont pas autorisés.</p>

## Comment utiliser HXL dans un XLSForm

Lors de la création d'un XLSForm, il suffit d'insérer une colonne supplémentaire dans n'importe quelle feuille de calcul existante et de la remplir avec des hashtags HXL identifiant le type d'informations contenu dans chaque colonne.

**onglet survey**

| type                 | name     | label                                              | hxl        |
| :------------------- | :------- | :------------------------------------------------- | :--------- |
| select_one countries | country  | Sélectionner le pays affecté                       | #country   |
| select_one admin1    | province | Veuillez sélectionner la province                  | #adm1+code |
| select_one admin2    | county   | Sélectionner le comté                              | #adm2+name |
| select_one sector    | cluster  | Cluster                                            | #sector    |
| integer              | affected | Nombre de personnes affectées                      | #affected  |
| integer              | reached  | Nombre de personnes atteintes à ce jour            | #reached   |
| survey |