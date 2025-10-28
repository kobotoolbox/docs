# Créer des numéros de série uniques dans les formulaires
<a href="../unique_serial_numbers.html">Read in English</a> | <a href="../es/unique_serial_numbers.html">Leer en español</a> | <a href="../ar/unique_serial_numbers.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/unique_serial_numbers.md" class="reference">29 juil. 2025</a>

Il arrive que vous souhaitiez générer un numéro de série unique pour chaque formulaire d'un projet. Cet article présente différentes solutions pour créer des numéros de série uniques en utilisant le type de question `calculate`.

## Approche 1 : Créer des numéros de série uniques séquentiels basés sur la date et l'heure

Cette méthode fonctionne mieux avec les [formulaires Web Enketo](data_through_webforms.md). Elle utilise une fonction de calcul pour créer un numéro de série unique basé sur la date et l'heure à la première milliseconde près. Bien que cette méthode ne réponde pas nécessairement à tous vos besoins, elle devrait vous donner une illustration de la flexibilité des fonctions de calcul.

Créez un
<a class="reference" href="calculate_questions.html">type de question <code>calculate</code></a> dans l'interface de création de formulaires ou dans **XLSForm** et utilisez la formule ci-dessous.

```
concat(substr(today(), 0, 4), substr(today(), 5, 7), substr(today(), 8, 10), substr(now(), 11, 13), substr(now(), 14, 16), substr(now(), 17, 19))
```

<p class="note">
  La même formule peut fonctionner comme une question de type <code>integer</code> lorsque vous travaillez dans un <strong>XLSForm</strong>.
</p>

![Exemple de calcul](/images/unique_serial_numbers/calculate_example.png)

Dans l'exemple, lorsque vous prévisualisez le formulaire déployé dans **Enketo**, vous devriez pouvoir voir le numéro de série dans la question de type note comme illustré dans l'image ci-dessous :

![Aperçu du formulaire](/images/unique_serial_numbers/preview_form.png)

## Approche 2 : Créer des numéros de série uniques à partir de variables sélectionnées

Cet exemple montre comment créer des numéros de série uniques à partir de variables existantes déjà définies dans votre formulaire en utilisant l'expression
[`concat()`](https://docs.getodk.org/form-operators-functions/#concat)
dans un type de question `calculate`. L'exemple est présenté sous forme d'**XLSForm**, mais peut tout aussi facilement être réalisé dans l'interface de création de formulaires.

**Feuille survey**

| type      | name    | label                                           | calculation                                                           |
| :-------- | :------ | :---------------------------------------------- | :-------------------------------------------------------------------- |
| text      | Q1      | Nom de la région                                |                                                                       |
| text      | Q2      | Nom du district                                 |                                                                       |
| text      | Q3      | Nom du cluster                                  |                                                                       |
| text      | Q4      | Nom du village                                  |                                                                       |
| text      | Q5      | Numéro de série du ménage                       |                                                                       |
| calculate | Q1_C    |                                                 | substr(${Q1}, 0, 3)                                                   |
| calculate | Q2_C    |                                                 | substr(${Q2}, 0, 3)                                                   |
| calculate | Q3_C    |                                                 | substr(${Q3}, 0, 3)                                                   |
| calculate | Q4_C    |                                                 | substr(${Q4}, 0, 3)                                                   |
| calculate | ID      |                                                 | concat(${Q1_C}, '-', ${Q2_C}, '-', ${Q3_C}, '-', ${Q4_C}, '-', ${Q5}) |
| note      | note_id | Votre identifiant unique pour ce formulaire est : ${ID} |                                                                       |
| survey |

Lorsque vous prévisualisez l'exemple dans les formulaires Web **Enketo**, le numéro de série sera présenté dans la question de type note comme illustré dans l'image ci-dessous :

![Aperçu de l'identifiant unique](/images/unique_serial_numbers/preview_uniqueid.png)