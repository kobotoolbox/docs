# Question de type Code-barres / code QR

La question de type « Code-barres / code QR » permet de scanner, décoder et capturer des codes-barres et des codes QR à l'aide de la caméra de l'appareil. Lorsqu'un code est scanné, la valeur (qu'il s'agisse de chiffres ou de texte) stockée dans le code est capturée.

<p class="note">
Le scan de codes-barres / codes QR fonctionne uniquement lors de <a href="https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html">l'utilisation de KoboCollect</a> sur des appareils mobiles.
</p>

Un large éventail de formats de codes-barres et de codes QR est disponible, notamment les suivants :

- UPC-A
- UPC-E
- EAN-8
- EAN-13
- Code 39
- Code 93
- Code 128
- Codabar
- ITF
- RSS-14
- RSS-Expanded
- QR Code
- Data Matrix
- Aztec
- PDF 417
- MaxiCode

Les questions de type « Code-barres / code QR » peuvent être utilisées dans différents contextes, notamment pour la gestion d'actifs ou la distribution d'articles. Par exemple, vous pouvez scanner un code QR sur la carte d'identité d'un bénéficiaire afin de capturer son numéro d'identification. Vous pouvez ensuite utiliser la fonction `pulldata()` pour renseigner automatiquement des champs à partir d'un fichier CSV joint à votre projet ou d'un [projet lié](dynamic_data_attachment.md) contenant des informations sur le bénéficiaire. Pour en savoir plus sur la fonction `pulldata()`, consultez [cette page](https://xlsform.org/en/#how-to-pull-data-from-csv).

## Configurer la question de type « Code-barres / code QR »

### Configuration dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder)

Pour ajouter une question de type « Code-barres / code QR » :

- Cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question
- Saisissez le texte de la question, par exemple « Collecter le code d'identification du bénéficiaire », puis cliquez sur **AJOUTER UNE QUESTION** ou appuyez sur ENTRÉE sur votre clavier
- Choisissez le type de question

![Ajout de questions Code-barres / code QR](images/barcode_qrcode_questions/adding_barcode_qrcode_questions.gif)

### Configuration dans XLSForm

Pour ajouter une question de type « Code-barres / code QR » dans un XLSForm, ajoutez une question avec le type `barcode` comme suit :

| type    | name           | label                                          |
| :------ | :------------- | :--------------------------------------------- |
| barcode | beneficiary_id | Capture the beneficiary ID code |
| survey  |

## Affichage des questions « Code-barres / code QR » dans les formulaires web et KoboCollect

### Apparence par défaut

![Apparence par défaut des questions Code-barres / code QR](images/barcode_qrcode_questions/barcode_qrcode_default.png)

### Apparence avancée

Lors de l'ajout d'une question de type « Code-barres / code QR », vous pouvez modifier les paramètres d'apparence pour passer de la caméra par défaut (caméra arrière) de l'appareil à la caméra avant.

### Modifier l'apparence avancée dans le Formbuilder

Accédez aux paramètres de la question « Code-barres / code QR » et saisissez « front » dans le champ « Apparence (avancée) ».

![Modification de l'apparence des questions Code-barres / code QR](images/barcode_qrcode_questions/change_appearance_barcode_qrcode_questions.png)

### Modifier l'apparence avancée dans XLSForm

Dans un XLSForm, vous pouvez définir la caméra avant comme caméra par défaut pour la capture des questions « Code-barres / code QR » en saisissant « front » dans la colonne `appearance` comme suit :

| type    | name             | label                                          | appearance |
| :------ | :--------------- | :--------------------------------------------- | :--------- |
| barcode | beneficiary_id_2 | Capture the beneficiary ID code | front      |
| survey  |

<p class="note">
  Vous pouvez télécharger un XLSForm contenant des exemples tirés de cet article
  <a
    download
    class="reference"
    href="./_static/files/barcode_qrcode_questions/barcode_qrcode_questions.xlsx"
    >ici</a
  >.
</p>