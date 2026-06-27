# Importer un XLSForm via une URL

Lors de l'importation d'un XLSForm via une URL, assurez-vous que l'URL pointe directement vers le fichier XLS et qu'il est accessible publiquement. Un moyen rapide de vérifier cela est de charger l'URL dans un navigateur : cela devrait déclencher le téléchargement du fichier. (Si une page se charge dans le navigateur, l'URL n'est pas la bonne.)

## Google Sheets

Pour obtenir le lien correct d'un tableur Google Sheets, suivez ces étapes :

1. Cliquez sur **Fichier > Publier** sur le Web.

2. Dans le menu déroulant **Page Web**, sélectionnez **Microsoft Excel (.xlsx)**. Laissez **Document entier** sélectionné dans le menu déroulant précédent.

3. Copiez le lien depuis le champ qui apparaît.

![image](/images/xls_url/link.jpg)

**Note pour les utilisateurs avancés :** dans nos tests, la case à cocher « Republier automatiquement lors des modifications » ne fonctionne pas toujours correctement. Il peut être nécessaire d'arrêter la publication puis de republier le tableur pour obtenir un lien mis à jour.

## Dropbox

Pour obtenir le lien correct d'un tableur dans Dropbox, suivez ces étapes :

1. Assurez-vous que le fichier XLSForm se trouve dans un dossier Dropbox public de votre compte.

2. Copiez son lien. Il doit se terminer par le suffixe `?dl=0`. Remplacez le 0 par 1, de sorte que votre lien se termine par `?dl=1`.