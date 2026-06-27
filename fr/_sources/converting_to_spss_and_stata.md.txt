# Convertir vos données pour SPSS et Stata
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/converting_to_spss_and_stata.md" class="reference">15 Feb 2022</a>


<p class="note">
  Cet article vous explique comment convertir vos données pour <strong>SPSS</strong> et
  <strong>Stata</strong>. Veuillez noter que vous avez besoin
  d'<strong>IBM SPSS</strong> ou de <strong>Stata</strong>, qui sont des
  applications tierces.
</p>

**KoboToolbox** n'exportant pas les données directement au format **SPSS** ou **Stata**, cet article vous guidera dans la procédure de conversion.

## Convertir vers SPSS

1. Téléchargez vos données au format XLS en suivant les instructions de
   [Exporter et télécharger vos données](export_download.md) ou comme illustré dans l'image
   ci-dessous.

    ![Export XLS](/images/converting_to_spss_and_stata/export_xls.gif)

2. Téléchargez les **Libellés SPSS** depuis le même onglet **DONNÉES**, comme indiqué dans l'image
   ci-dessous. Cette opération génère un dossier compressé contenant la syntaxe **SPSS**.

    ![Export SPSS Labels](/images/converting_to_spss_and_stata/export_spss_labels.gif)

3. Vous aurez besoin d'**IBM SPSS** pour importer les données XLS en utilisant la méthode
   suivante, compatible avec toutes les versions de **SPSS**.

    - Dans **SPSS**, cliquez sur **File -> Open -> Data** (comme ci-dessous).
    - Une fois que vous avez cliqué sur l'onglet **Data**, une boîte de dialogue apparaît.
      Dans le champ **Files of type**, sélectionnez **Excel**.
    - Naviguez jusqu'au dossier contenant votre fichier **Excel** et localisez le
      fichier **Excel** qui contient les données téléchargées.
    - Ouvrez le fichier : la boîte de dialogue **Read Excel File** s'affiche.

    ![Import into SPSS](/images/converting_to_spss_and_stata/import_into_spss.gif)

4. Ouvrez maintenant la syntaxe téléchargée à l'_étape 2_ et exécutez-la.

    ![Run Syntax](/images/converting_to_spss_and_stata/run_syntax.jpg)

Vos données sont maintenant prêtes à être analysées dans **SPSS**.

## Convertir le fichier SPSS en fichier Stata

Il n'existe malheureusement pas d'option permettant de télécharger directement un fichier **SPSS DO**.
Vous devez suivre la procédure décrite ci-dessus, puis enregistrer les données finales sous forme de fichier
**Stata** `.dta`.

Veillez à sélectionner toutes les options souhaitées au moment de l'enregistrement.

![dta data](/images/converting_to_spss_and_stata/dta_data.jpg)