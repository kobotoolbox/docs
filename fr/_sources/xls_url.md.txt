# Importer un XLSForm via URL
<a href="../xls_url.html">Read in English</a> | <a href="../es/xls_url.html">Leer en español</a> | <a href="../ar/xls_url.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/d14c3f76675d9085da27e1c5dd4fcf981a6b3a7d/source/xls_url.md" class="reference">7 Jan 2025</a>

Lors de l'importation d'un XLSForm via URL, assurez-vous que l'URL pointe directement vers le fichier XLS et qu'il est accessible publiquement. Un moyen rapide de tester cela est de charger l'URL dans un navigateur : cela devrait déclencher le téléchargement du fichier. (Si cela charge une page dans le navigateur, alors ce n'est pas la bonne URL.)

## Google Sheets

Pour obtenir le lien correct pour une feuille de calcul Google Sheets, suivez ces étapes :

1. Cliquez sur **Fichier > Publier** sur le Web.

2. Sous le menu déroulant **Page Web**, sélectionnez **Microsoft Excel (.xlsx)**. Conservez **Document entier** sélectionné dans le menu déroulant précédent.

3. Copiez le lien du champ résultant.

    ![image](/images/xls_url/link.jpg)

**Remarque pour les utilisatrices et utilisateurs avancés :** lors de nos tests, la case à cocher « Republier automatiquement en cas de modifications » ne fonctionne pas toujours bien. Vous devrez peut-être arrêter la publication et republier la feuille de calcul pour obtenir un lien mis à jour.

## Dropbox

Pour obtenir le lien correct pour une feuille de calcul dans Dropbox, suivez ces étapes :

1. Assurez-vous que le fichier XLSForm se trouve dans un dossier Dropbox public de votre compte.

2. Copiez son lien. Il devrait se terminer par le suffixe `?dl=0`. Remplacez le 0 par 1, de sorte que votre lien se termine par `?dl=1`.