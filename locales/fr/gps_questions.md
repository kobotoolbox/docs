# Types de questions GPS
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/27e85949b3f42b42dcb60701fbfc80aadddbb616/source/gps_questions.md" class="reference">30 juil. 2022</a>

Dans KoboToolbox, vous pouvez collecter des coordonnées GPS dans le cadre de votre formulaire de collecte de données. Vous pouvez utiliser 3 types de questions GPS, à savoir « Point », « Ligne » et « Zone ».

Utilisez un type de question « Point » lorsque vous souhaitez enregistrer une seule coordonnée GPS. C'est parfait pour les questions où vous devez indiquer l'emplacement d'un élément unique tel qu'une maison ou un forage.

Utilisez un type de question « Ligne » lorsque vous souhaitez enregistrer plusieurs points GPS pour tracer un chemin. Ce type de question peut être utilisé pour collecter des données de localisation sur des éléments tels que des routes, des pistes et des rivières.

Le type de question « Zone » est utilisé pour collecter plusieurs points GPS qui forment les limites d'un élément. Vous pouvez l'utiliser, par exemple, pour tracer les limites de parcelles de jardin dans une enquête où vous recensez des propriétés foncières.

## Comment configurer les types de questions « Point », « Ligne » et « Zone »

### Configuration dans l'interface de création de formulaires

Ajouter des questions GPS au formulaire est simple :

- Dans l'interface de création de formulaires, cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question
- Saisissez le texte de la question, par exemple « Capturez l'emplacement de l'unité d'habitation », puis cliquez sur **AJOUTER UNE QUESTION** ou appuyez sur ENTRÉE sur votre clavier
- Choisissez le type de question (par exemple Point)

![Ajout de questions GPS](images/gps_questions/adding_gps_questions.gif)

### Configuration dans XLSForm

Vous pouvez ajouter des questions « Point », « Ligne » et « Zone » dans XLSForm en utilisant les types de questions `geopoint`, `geotrace` et `geoshape` respectivement, comme dans l'exemple suivant :

| type     | name   | label                                       |
| :------- | :----- | :------------------------------------------ |
| geopoint | point  | Capturez l'emplacement de l'unité d'habitation |
| geotrace | road   | Tracez l'itinéraire de la route             |
| geoshape | garden | Tracez la limite du jardin                  |
| survey   |

## Apparence des types de questions « Point », « Ligne » et « Zone » dans les formulaires web et KoboCollect

### Apparence par défaut

![Apparences par défaut des questions GPS](images/gps_questions/gps_default_appearances.png)

## Collecte de points GPS en arrière-plan

En plus d'inclure des questions GPS dans votre formulaire, vous pouvez également collecter des coordonnées GPS en arrière-plan pendant la collecte de données. Cela est possible en activant l'option « Audit » dans l'interface de création de formulaires (Mise en page et paramètres -> Questions méta) ou en ajoutant la question méta `audit` à votre XLSForm. Pour en savoir plus sur la façon de procéder, consultez [cet article](audit_logging.md).

## Calcul de la distance et de la surface avec les types de questions « Ligne » et « Zone »

Lorsque vous collectez vos données GPS, vous pourriez avoir besoin de calculer la distance et la surface à partir de vos questions « Ligne » et « Zone ».

### Calcul de la distance à partir des questions « Ligne »

Pour calculer la distance à partir d'un type de question « Ligne » dans l'interface de création de formulaires, utilisez le type de question « Calculer » et la fonction [`distance()`](https://docs.getodk.org/form-operators-functions/#distance) comme indiqué ci-dessous :

![Calculer la distance](images/gps_questions/calculate_distance.png)

Dans l'exemple ci-dessus, la question « Tracez l'itinéraire de la piste » a été ajoutée en tant que type de question « Ligne ». Le « Nom de la colonne de données » dans les paramètres de la question a été défini sur « track ».

La question avec le libellé `distance(${track})` est un type de question « Calculer » avec un « Nom de la colonne de données » de « distance ». Le résultat sera en mètres.

La question « Note » est facultative et a été ajoutée dans le but d'afficher la distance calculée dans le formulaire.

Dans XLSForm, vous pouvez faire de même comme suit :

| type      | name             | label                                  | calculation        |
| :-------- | :--------------- | :------------------------------------- | :----------------- |
| geotrace  | track            | Tracez l'itinéraire de la piste        |                    |
| calculate | distance         |                                        | distance(${track}) |
| note      | display_distance | La distance est de ${distance} mètres  |                    |
| survey    |

### Calcul de la surface à partir des questions « Zone »

Vous pouvez calculer une surface en utilisant le type de question « Calculer » et la fonction [`area()`](https://docs.getodk.org/form-operators-functions/#area) comme indiqué ci-dessous :

![Calculer la surface](images/gps_questions/calculate_area.png)

Dans l'exemple ci-dessus, la question « Tracez les limites » a été ajoutée en tant que type de question « Zone ». Le « Nom de la colonne de données » dans les paramètres de la question a été défini sur « boundary ».

La question avec le libellé `area(${boundary})` est un type de question « Calculer » avec un Nom de la colonne de données « area ». Le résultat sera en mètres carrés.

La question « Note » est facultative et a été ajoutée dans le but d'afficher la surface calculée dans le formulaire.

Dans XLSForm, vous pouvez faire de même, comme suit :

| type      | name         | label                                 | calculation       |
| :-------- | :----------- | :------------------------------------ | :---------------- |
| geoshape  | boundary     | Tracez les limites                    |                   |
| calculate | area         |                                       | area(${boundary}) |
| note      | display_area | La surface est de ${area} mètres carrés |                   |
| survey    |

<p class="note">
  Vous pouvez télécharger un XLSForm avec des exemples de cet article
  <a
    download
    class="reference"
    href="./_static/files/gps_questions/gps_questions.xlsx"
    >ici</a
  >.
</p>