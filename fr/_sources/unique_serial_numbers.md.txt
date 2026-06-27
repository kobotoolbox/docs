# Créer des numéros de série uniques
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/unique_serial_numbers.md" class="reference">23 Apr 2026</a>


Il peut arriver que vous souhaitiez générer un numéro de série unique pour chaque formulaire d'un projet. Cet article présente différentes méthodes pour créer des numéros de série uniques à l'aide du type de question `calculate`.

## Méthode 1 : Créer des numéros de série séquentiels basés sur la date et l'heure

Cette méthode fonctionne mieux avec les [formulaires web](data_through_webforms.md). Elle utilise une fonction de calcul pour créer un numéro de série unique basé sur la date et l'heure à la milliseconde près. Bien que cette méthode ne réponde pas nécessairement à tous vos besoins, elle vous donnera un aperçu des possibilités offertes par les fonctions de calcul.

Créez une <a class="reference" href="calculate_questions.html"><code>question de type calculate</code></a> dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** ou dans un **XLSForm**, et utilisez la formule ci-dessous.

```
concat(substr(today(), 0, 4), substr(today(), 5, 7), substr(today(), 8, 10), substr(now(), 11, 13), substr(now(), 14, 16), substr(now(), 17, 19))
```

<p class="note">
  La même formule peut fonctionner avec une question de type <code>integer</code> dans un <strong>XLSForm</strong>.
</p>

![Calculate example](/images/unique_serial_numbers/calculate_example.png)

Dans cet exemple, lorsque vous prévisualisez le formulaire déployé dans les **formulaires web**, vous devriez voir le numéro de série dans la question de type note, comme illustré dans l'image ci-dessous :

![Preview form](/images/unique_serial_numbers/preview_form.png)

## Méthode 2 : Créer des numéros de série uniques à partir de variables sélectionnées

Cet exemple montre comment créer des numéros de série uniques à partir de variables déjà définies dans votre formulaire, en utilisant l'expression [`concat()`](https://docs.getodk.org/form-operators-functions/#concat) dans une question de type `calculate`. L'exemple est présenté sous forme de **XLSForm**, mais peut tout aussi facilement être réalisé dans le Formbuilder.

**onglet survey**

| type      | name    | label                                              | calculation                                                           |
| :-------- | :------ | :------------------------------------------------- | :-------------------------------------------------------------------- |
| text      | Q1      | Region Name                                        |                                                                       |
| text      | Q2      | District Name                                      |                                                                       |
| text      | Q3      | Cluster Name                                       |                                                                       |
| text      | Q4      | Village Name                                       |                                                                       |
| text      | Q5      | Household Serial Number                            |                                                                       |
| calculate | Q1_C    |                                                    | substr(${Q1}, 0, 3)                                                   |
| calculate | Q2_C    |                                                    | substr(${Q2}, 0, 3)                                                   |
| calculate | Q3_C    |                                                    | substr(${Q3}, 0, 3)                                                   |
| calculate | Q4_C    |                                                    | substr(${Q4}, 0, 3)                                                   |
| calculate | ID      |                                                    | concat(${Q1_C}, '-', ${Q2_C}, '-', ${Q3_C}, '-', ${Q4_C}, '-', ${Q5}) |
| note      | note_id | Your Unique ID for this form is: ${ID} |                                                                       |
| survey |

Lorsque vous prévisualisez l'exemple dans les formulaires web, le numéro de série s'affiche dans la question de type note, comme illustré dans l'image ci-dessous :

![Preview unique id](/images/unique_serial_numbers/preview_uniqueid.png)