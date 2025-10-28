# Type de question Code-barres/Code QR
<a href="../barcode_qrcode_questions.html">Read in English</a> | <a href="../es/barcode_qrcode_questions.html">Leer en español</a> | <a href="../ar/barcode_qrcode_questions.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/c5889af525a55f27747f919a026f9b7103f5c180/source/barcode_qrcode_questions.md" class="reference">24 Sep 2025</a>

Le type de question « Code-barres/Code QR » est utilisé pour scanner, décoder et capturer des codes-barres et des codes QR à l'aide de l'appareil photo de l'appareil. Lorsqu'un code est scanné avec l'appareil photo, la valeur (qu'il s'agisse de chiffres ou de texte) stockée dans le code est capturée.

<p class="note">
  Le scan de codes-barres/codes QR ne fonctionne que lors de <a href="https://support.kobotoolbox.org/kobocollect_on_android_latest.html">l'utilisation de KoboCollect</a> sur des appareils mobiles.
</p>

Une large gamme de formats de codes-barres et de codes QR est prise en charge, notamment les suivants :

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

Les questions « Code-barres/Code QR » peuvent être utilisées dans différents scénarios, notamment la gestion d'actifs ou la distribution d'articles. Par exemple, vous pouvez scanner un code QR sur une carte d'identité de bénéficiaire pour capturer son numéro d'identification. Vous pouvez ensuite utiliser la fonction `pulldata()` pour remplir automatiquement des champs à partir d'un fichier CSV joint à votre projet ou à partir d'un [projet lié](dynamic_data_attachment.md) avec des informations sur le bénéficiaire. Vous pouvez en savoir plus sur la fonction `pulldata()` [ici](https://xlsform.org/en/#how-to-pull-data-from-csv).

## Comment configurer le type de question « Code-barres/Code QR »

### Configuration dans l'interface de création de formulaires

Pour ajouter une question « Code-barres/Code QR » :

- Cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question
- Saisissez le texte de la question, par exemple « Collectez le code d'identification du bénéficiaire », puis cliquez sur **AJOUTER UNE QUESTION** ou appuyez sur ENTRÉE sur votre clavier
- Choisissez le type de question

![Ajout de questions Code-barres/Code QR](images/barcode_qrcode_questions/adding_barcode_qrcode_questions.gif)

### Configuration dans XLSForm

Pour ajouter une question « Code-barres/Code QR » dans XLSForm, ajoutez une question de type `barcode` comme suit :

| type    | name           | label                                      |
| :------ | :------------- | :----------------------------------------- |
| barcode | beneficiary_id | Capturez le code d'identification du bénéficiaire |
| survey  |

## Comment les questions « Code-barres/Code QR » sont affichées sur les formulaires Web et KoboCollect

### Apparence par défaut

![Apparence par défaut des questions Code-barres/Code QR](images/barcode_qrcode_questions/barcode_qrcode_default.png)

### Apparence avancée

Lors de l'ajout du type de question « Code-barres/Code QR », vous pouvez modifier les paramètres d'apparence pour passer de l'utilisation de l'appareil photo par défaut (arrière) de l'appareil à l'utilisation de l'appareil photo avant.

### Modification de l'apparence avancée dans l'interface de création de formulaires

Accédez aux paramètres de la question « Code-barres/Code QR », et saisissez « front » dans la case « Apparence (Avancé) »

![Modification de l'apparence des questions Code-barres/Code QR](images/barcode_qrcode_questions/change_appearance_barcode_qrcode_questions.png)

### Modification de l'apparence avancée dans XLSForm

Dans XLSForm, vous pouvez définir l'appareil photo par défaut pour capturer le « Code-barres/Code QR » comme étant l'appareil photo avant en saisissant « front » dans la colonne `appearance` comme suit :

| type    | name             | label                                      | appearance |
| :------ | :--------------- | :----------------------------------------- | :--------- |
| barcode | beneficiary_id_2 | Capturez le code d'identification du bénéficiaire | front      |
| survey  |

<p class="note">
  Vous pouvez télécharger un XLSForm avec des exemples de cet article
  <a
    download
    class="reference"
    href="./_static/files/barcode_qrcode_questions/barcode_qrcode_questions.xlsx"
    >ici</a
  >.
</p>