# Déployer vos formulaires pour la collecte de données
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/deploy_form_new_project.md" class="reference">23 avr. 2026</a>

Avant de pouvoir collecter des données dans KoboToolbox, votre formulaire doit être **déployé**. Le déploiement rend le formulaire actif et disponible pour les soumissions. Vous pouvez **redéployer** un formulaire à tout moment lorsque vous apportez des modifications et souhaitez que ces modifications soient mises en ligne. 

Cet article explique comment déployer et redéployer des formulaires dans KoboToolbox, comment les mises à jour affectent les formulaires web et KoboCollect, ce qu'il faut vérifier avant de mettre un formulaire en ligne, et quelles modifications éviter une fois la collecte de données commencée.

<p class="note">
Pour en savoir plus sur la collecte de données avec KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/data-collection-tools.html">Collecter des données avec KoboToolbox</a>. 
</p>

## Déployer un formulaire pour la collecte de données

Lorsque votre formulaire est prêt à recevoir des données, ouvrez le projet et cliquez sur **DÉPLOYER** dans la page **FORMULAIRE** pour le mettre en ligne. 

![Déployer un formulaire](images/deploy_form_new_project/deploy.png)

Une fois que vous avez déployé un formulaire, vous pouvez commencer à [collecter des données](https://support.kobotoolbox.org/fr/data-collection-tools.html) avec celui-ci. 

Après qu'un formulaire a déjà été déployé, vous serez invité à **REDÉPLOYER** chaque fois que vous apportez des modifications qui ne sont pas encore publiques. Une bannière jaune apparaîtra indiquant « Si vous voulez rendre ces changements publics, vous devez déployer ce formulaire. »

<p class="note">
<strong>Note :</strong>
    Redéployez toujours les formulaires après avoir apporté des modifications aux médias du formulaire, aux traductions ou aux titres de formulaire, même si KoboToolbox ne vous invite pas à redéployer.
</p>

## Mettre à jour les formulaires après que les modifications ont été redéployées

Après avoir redéployé un formulaire, les utilisateurs devront actualiser ou télécharger la version mise à jour pour voir les modifications.

### Formulaires web

Lors de l'utilisation de **formulaires web**, les mises à jour peuvent prendre quelques secondes avant d'apparaître. Une fois la nouvelle version prête, une bannière jaune apparaîtra en haut du formulaire indiquant : « Une nouvelle version de ce formulaire a été téléchargée. Actualisez cette page pour charger la version mise à jour. » Actualisez la page pour charger la dernière version. 

![La bannière affiche : Une nouvelle version de ce formulaire a été téléchargée. Actualisez cette page pour charger la version mise à jour.](images/deploy_form_new_project/banner.png)

Si quelqu'un a déjà commencé à saisir des données, il peut toujours actualiser. KoboToolbox lui demandera soit d'ignorer les données déjà saisies, soit de les charger dans la nouvelle version du formulaire.

![Invite d'enregistrement non sauvegardé trouvé](images/deploy_form_new_project/unsaved.png)

### KoboCollect

Lors de l'utilisation de **KoboCollect**, les utilisateurs doivent télécharger la dernière version du formulaire pour recevoir les mises à jour. Cela nécessite une connexion Internet. 

La récupération de la dernière version d'un formulaire peut être [effectuée manuellement](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html#downloading-forms) chaque fois que le formulaire change, ou elle peut être configurée pour se produire automatiquement à une fréquence définie via les [paramètres de mise à jour de formulaire](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings) dans KoboCollect.

<p class="note">
<strong>Note :</strong>
    Après avoir redéployé un formulaire, assurez-vous que tous les collecteurs de données mettent à jour vers la dernière version. Sinon, certains utilisateurs peuvent continuer à soumettre des données avec une version obsolète, ce qui peut entraîner des erreurs ou des incohérences dans les données collectées. 
</p>

## Bonnes pratiques pour déployer et redéployer des formulaires

Les étapes suivantes sont recommandées avant de lancer la collecte de données :

1. **Testez l'aperçu du formulaire avant le déploiement.** Ne déployez un nouveau formulaire, ou ne redéployez des modifications à un formulaire existant, qu'après l'avoir testé minutieusement dans l'aperçu du formulaire. Cela aide à éviter que des formulaires défectueux ne soient mis en ligne.
2. **Testez le formulaire déployé en ligne.** Après le déploiement, ouvrez le formulaire et soumettez des données de test pour confirmer que les soumissions fonctionnent correctement et que les données apparaissent dans le tableau de données comme prévu.
3. **Si pertinent, testez le formulaire dans KoboCollect.** Testez toujours la ou les mêmes méthodes de collecte de données qui seront utilisées pour la collecte de données réelle, qu'il s'agisse de formulaires web, de KoboCollect, ou des deux. Ceci est particulièrement important pour KoboCollect, car il ne peut pas être entièrement testé tant que le formulaire n'a pas été déployé.
4. **Partagez votre formulaire en mode Afficher seulement pour des tests externes.** Une fois qu'un formulaire a été déployé, vous pouvez également le partager avec d'autres pour des tests en utilisant le [mode de formulaire web](https://support.kobotoolbox.org/fr/data_through_webforms.html#data-collection-modes) **Afficher seulement**.

Une fois que vous avez testé minutieusement votre formulaire, vous pouvez commencer la collecte de données. Tester minutieusement avant le lancement aide à réduire le besoin d'apporter des modifications après le début de la collecte de données.

### Considérations importantes lors du redéploiement d'un formulaire

Si vous apportez des modifications à un formulaire après que la collecte de données a déjà commencé, ces modifications peuvent affecter à la fois votre structure de données et votre capacité à examiner ou modifier les soumissions plus anciennes. Pour cette raison, il est préférable d'**éviter les changements structurels majeurs** une fois la collecte de données en direct en cours, sauf s'ils sont absolument nécessaires. 

Les modifications qui peuvent affecter votre structure de données incluent :

- **Modifier le [nom du champ](https://support.kobotoolbox.org/fr/glossary.html#data-column-name) d'une question** : KoboToolbox le traitera comme une nouvelle variable et créera une nouvelle colonne dans le tableau de données.
- **Modifier un type de question tout en conservant le même nom de champ** : Cela peut créer des données incohérentes dans la même colonne et entraîner des erreurs (par exemple, dans la vue **DONNÉES > Rapports**).
- **Déplacer des questions dans ou hors de groupes** : KoboToolbox traitera ces questions comme de nouvelles variables et créera de nouvelles colonnes dans le tableau de données.
- **Supprimer des choix d'une liste de choix** : Les soumissions précédentes peuvent toujours contenir ces valeurs de choix, mais elles peuvent ne plus avoir de libellé associé dans le formulaire.
- **Ajouter de nouveaux choix à une question Choix unique ou Choix multiple** : Assurez-vous que chaque nouveau choix a une [valeur XML](https://support.kobotoolbox.org/fr/glossary.html#xml-value) unique au sein d'une liste de choix donnée.
- **Supprimer une question qui est utilisée ailleurs dans le formulaire** : Si la question est référencée dans un calcul, une condition de pertinence, une contrainte ou une autre expression, vous devrez également mettre à jour ces références.
- **Modifier les libellés de questions ou de choix** : N'affecte pas la structure des données si le nom du champ ou la valeur XML reste la même, mais les données précédemment collectées utiliseront le libellé mis à jour.
- **Modifier la signification des valeurs de choix existantes** : Modifier les noms ou libellés de choix peut rendre les données incohérentes entre les versions de formulaire et conduire à une mauvaise interprétation. Par exemple, cela peut se produire si vous inversez la signification de valeurs telles que `1 = Oui` et `0 = Non`, ou changez la direction d'une échelle de Likert.

<p class="note">
<strong>Note :</strong>
    Si votre formulaire utilise plusieurs langues, n'oubliez pas de <a href="https://support.kobotoolbox.org/fr/language_dashboard.html">mettre à jour les traductions</a> chaque fois que vous modifiez le formulaire. Ceci est facile à oublier après le redéploiement.
</p>

Les modifications apportées à un formulaire peuvent également affecter le comportement des soumissions plus anciennes lorsque vous les modifiez, car une soumission créée avec une version antérieure du formulaire peut ne plus correspondre à la version actuelle. Par exemple :

- **Ajouter de nouvelles questions obligatoires** : Les soumissions plus anciennes peuvent nécessiter de nouvelles réponses avant de pouvoir être soumises à nouveau.
- **Supprimer des questions ou ajouter une logique de saut** : Les soumissions plus anciennes peuvent perdre des données précédemment collectées dans ces questions lorsqu'elles sont modifiées.
- **Ajouter de nouvelles règles de validation ou contraintes** : Les réponses plus anciennes peuvent ne plus respecter les règles mises à jour et peuvent ne pas être soumises à nouveau.

## Résolution de problèmes

<details>
<summary><strong>Erreur lors du déploiement : Les noms de choix doivent être uniques pour chaque liste de choix</strong></summary>
Cette erreur signifie que deux choix ou plus dans la même liste de choix ont la même <a href="https://support.kobotoolbox.org/fr/glossary.html#xml-value">valeur XML (ou nom de choix)</a>.
<br><br>
Si vous utilisez le <strong>Formbuilder</strong>, vérifiez les <a href="https://support.kobotoolbox.org/fr/question_types.html#setting-xml-values-for-option-choices">valeurs XML</a> que vous avez définies manuellement pour chaque choix de réponse afin de vous assurer que chaque valeur XML est unique au sein d'une liste de choix donnée.
<br><br>
Si vous ne pouvez pas identifier quel choix cause le problème, <a href="https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox">téléchargez le formulaire</a> en tant qu'<strong>XLSForm</strong> et vérifiez l'onglet <code>choices</code> pour trouver plus facilement la valeur en double. Le message d'erreur fournira généralement le numéro de ligne dans l'onglet <code>choices</code> qui cause l'erreur.
</details>

<br>

<details>
<summary><strong>Erreur lors du déploiement : Impossible de trouver external_file.csv
</strong></summary>
Cette erreur signifie que votre formulaire fait référence à une pièce jointe externe, telle qu'un fichier utilisé avec <code>pulldata()</code>, mais que ce fichier n'a pas été importé dans le projet.
<br><br>
Importez la pièce jointe manquante dans les paramètres <a href="https://support.kobotoolbox.org/fr/upload_media.html">médias du formulaire</a>, puis essayez de déployer à nouveau.
</details>

<br>

<details>
<summary><strong>Erreur lors du déploiement : Impossible de trouver survey.xml</strong></summary>
Cette erreur signifie généralement que les <a href="https://support.kobotoolbox.org/fr/dynamic_data_attachment.html">liaisons dynamiques de projets</a> n'ont pas été configurées correctement dans les paramètres du projet.
<br><br>
Vérifiez que les liaisons dynamiques de projets ont été ajoutées et configurées correctement, puis essayez de déployer à nouveau le formulaire.
</details>

<br>