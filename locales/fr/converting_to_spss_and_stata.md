# Convertir les données en SPSS et/ou Stata
<a href="../converting_to_spss_and_stata.html">Read in English</a> | <a href="../es/converting_to_spss_and_stata.html">Leer en español</a> | <a href="../ar/converting_to_spss_and_stata.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/converting_to_spss_and_stata.md" class="reference">15 fév. 2022</a>

<p class="note">
  Cet article vous aide à convertir vos données en <strong>SPSS</strong> et
  <strong>Stata</strong>. Veuillez noter que vous avez besoin
  d'<strong>IBM SPSS</strong> ou de <strong>Stata</strong> qui sont des applications
  tierces.
</p>

Étant donné que **KoboToolbox** n'exporte pas les données directement au format **SPSS** ou **Stata**,
cet article vous guidera pour effectuer la conversion.

## Convertir en SPSS

1. Téléchargez vos données au format XLS en suivant les instructions fournies dans
   [cet article d'assistance](export_download.md) ou comme illustré dans l'image
   ci-dessous.

    ![Export XLS](/images/converting_to_spss_and_stata/export_xls.gif)

2. Téléchargez les **étiquettes SPSS** depuis le même onglet **DONNÉES** comme indiqué dans l'image
   ci-dessous. Ce processus générera un dossier compressé qui contient la
   syntaxe **SPSS**.

    ![Export SPSS Labels](/images/converting_to_spss_and_stata/export_spss_labels.gif)

3. Vous aurez maintenant besoin d'**IBM SPSS** pour importer les données en XLS en utilisant la méthode
   suivante qui est compatible avec toutes les versions de **SPSS**.

    - Dans **SPSS**, cliquez sur **Fichier -> Ouvrir -> Données** (comme ci-dessous).
    - Une fois que vous cliquez sur l'onglet **Données**, une boîte de données apparaîtra.
      Dans la boîte **Type de fichiers**, sélectionnez **Excel**.
    - Naviguez vers le dossier qui contient votre fichier **Excel**, et trouvez le
      fichier **Excel** qui contient les données que vous avez téléchargées.
    - Ouvrez le fichier, et vous obtiendrez la boîte de dialogue **Lire le fichier Excel**.

    ![Import into SPSS](/images/converting_to_spss_and_stata/import_into_spss.gif)

4. Ouvrez maintenant la syntaxe que vous avez téléchargée à l'_Étape 2_ et exécutez la syntaxe.

    ![Run Syntax](/images/converting_to_spss_and_stata/run_syntax.jpg)

Vous êtes maintenant prêt à manipuler vos données dans **SPSS**.

## Convertir le fichier SPSS en fichier STATA

Malheureusement, nous n'avons pas d'option pour télécharger directement un fichier **SPSS DO**.
Vous devez passer par le processus ci-dessus puis enregistrer les données finales sous forme de données
**Stata** `.dta`.

Assurez-vous de choisir d'enregistrer toutes les options dont vous avez besoin lors de l'enregistrement.

![dta data](/images/converting_to_spss_and_stata/dta_data.jpg)