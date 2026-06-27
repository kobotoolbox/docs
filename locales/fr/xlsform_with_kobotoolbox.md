# Utiliser XLSForm avec KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/2766eac60a2cfda9bee74f5ec77308dd80bfd029/source/xlsform_with_kobotoolbox.md" class="reference">6 mai 2026</a>

XLSForm s'intègre parfaitement à KoboToolbox pour créer, prévisualiser, modifier et déployer des formulaires de collecte de données. Par exemple, vous pouvez commencer à créer un formulaire dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, puis le télécharger en tant que XLSForm pour le personnaliser davantage. Cela fournit une base structurée, utile pour les nouveaux projets ou les utilisateurs ayant moins d'expérience dans la création de formulaires.

Une fois personnalisés, les formulaires créés dans XLSForm peuvent être importés dans KoboToolbox pour être examinés, modifiés et déployés.

Cet article couvre les sujets suivants :
-   Télécharger un XLSForm depuis KoboToolbox
-   Importer et prévisualiser un XLSForm dans KoboToolbox
-   Remplacer un formulaire existant par un XLSForm
-   Importer un XLSForm via une URL
-   Tester et valider votre XLSForm

## Télécharger un XLSForm depuis KoboToolbox

Lorsque vous travaillez dans KoboToolbox, vous pouvez avoir besoin de télécharger votre formulaire en tant que XLSForm pour y apporter des modifications plus efficacement, par exemple pour dupliquer de nombreuses questions, modifier de grandes listes d'options, ajouter des traductions ou utiliser des fonctionnalités avancées non disponibles dans le Formbuilder. De plus, télécharger votre formulaire en tant que XLSForm vous permet de créer des formulaires hors ligne, de les partager sous forme de fichiers `.xlsx` pour la collaboration et la gestion des versions, et de les partager avec l'équipe d'assistance de KoboToolbox ou sur le Forum communautaire pour demander de l'aide.

Tout formulaire créé avec le Formbuilder peut être téléchargé en tant que fichier XLSForm :

1.  Accédez à la page **FORMULAIRE** de votre projet dans KoboToolbox.
2.  Cliquez sur l'icône <i class="k-icon k-icon-more"></i> **Plus d'actions**.
3.  Sélectionnez <i class="k-icon k-icon-xls-file"></i> **Télécharger XLS**.

![Menu Télécharger XLS](images/xlsform_with_kobotoolbox/download_xls.png)

## Importer un XLSForm dans KoboToolbox

Vous pouvez également avoir besoin de créer un nouveau projet à partir d'un XLSForm que vous avez créé de zéro ou qui vous a été partagé.

Pour importer et prévisualiser un XLSForm dans un nouveau projet dans KoboToolbox :

1.  Accédez à la page d'accueil **Projets** dans KoboToolbox et cliquez sur **NOUVEAU**.
2.  Sélectionnez **Importer un XLSForm** et importez votre fichier Excel.
3.  Saisissez les détails du projet et cliquez sur **Créer le projet**.
4.  Cliquez sur le bouton <i class="k-icon k-icon-view"></i> **Aperçu** pour prévisualiser votre formulaire.

![Boîte de dialogue d'importation XLSForm](images/xlsform_with_kobotoolbox/upload_xls.png)

## Remplacer un formulaire par un XLSForm

Une fois un projet créé, vous pouvez remplacer tout formulaire existant par un XLSForm mis à jour :

1.  Accédez à la page **FORMULAIRE** de votre projet dans KoboToolbox.
2.  Cliquez sur <i class="k-icon k-icon-replace"></i> **Remplacer le formulaire** en haut à droite.
3.  Sélectionnez **Importer un XLSForm** et importez votre fichier Excel.

![Boîte de dialogue de remplacement du formulaire](images/xlsform_with_kobotoolbox/replace_form.png)

## Importer un XLSForm via une URL

Si vous utilisez Google Sheets ou si vous stockez le fichier dans Dropbox, vous pouvez importer un XLSForm via une URL. L'URL doit être accessible publiquement et doit déclencher le téléchargement d'un fichier lorsqu'elle est ouverte dans un navigateur pour que l'importation fonctionne. Les XLSForms peuvent également être importés depuis des logiciels similaires, tels qu'Excel Web et OneDrive.

<details><summary><strong>Obtenir un lien depuis Google Sheets</strong></summary>

Pour obtenir l'URL correcte d'une feuille de calcul Google Sheets :

1.  Cliquez sur **Fichier > Partager > Publier sur le Web**.
2.  Dans le menu déroulant **Page Web**, sélectionnez **Microsoft Excel (.xlsx)**. Conservez **Document entier** sélectionné dans le premier menu déroulant.
3.  Cliquez sur **Publier**.
4.  Copiez le lien du document obtenu.

<p class="note">
Pour plus d'informations, consultez la <a href="https://support.google.com/docs/answer/183965?hl=en&co=GENIE.Platform%3DDesktop">documentation Google Sheets</a>.
</p>

</details>

<br>

<details><summary><strong>Obtenir un lien depuis Dropbox</strong></summary>

Pour obtenir l'URL correcte d'une feuille de calcul stockée dans Dropbox :

1.  Copiez le lien du fichier dans Dropbox en cliquant sur <i class="k-icon k-icon-link"></i> **Copier le lien**.
2.  À la fin du lien, remplacez le suffixe ``dl=0`` par ``dl=1``. Il s'agira de l'URL à importer dans KoboToolbox.

</details>

<br>

Une fois que vous avez récupéré l'URL du fichier, vous pouvez importer votre XLSForm dans KoboToolbox :

1.  Accédez à la page d'accueil **Projets** dans KoboToolbox et cliquez sur **NOUVEAU**.
2.  Sélectionnez **Importer un XLSForm via une URL**.
3.  Collez votre URL et cliquez sur **Importer**.
4.  Saisissez les détails du projet et cliquez sur **Créer le projet**.

![Boîte de dialogue d'importation XLSForm via URL](images/xlsform_with_kobotoolbox/import_via_url.png)

<p class="note">
    <b>Note :</b> Les modifications apportées à un fichier dans Dropbox ou Google Sheets ne sont pas automatiquement répercutées dans KoboToolbox. Vous devez réimporter le XLSForm via l'URL et redéployer les modifications du formulaire.
</p>

## Tester et valider votre XLSForm

Valider, prévisualiser et tester votre XLSForm est essentiel pour garantir son intégrité structurelle, sa fonctionnalité et l'expérience utilisateur. Chacune de ces étapes permet d'identifier les erreurs ou problèmes susceptibles d'empêcher le formulaire de fonctionner comme prévu.

| Étape | Description |
| :--- | :--- |
| Validation | Cette étape consiste à importer le formulaire et à vérifier les erreurs (par exemple, fautes d'orthographe ou de casse, expressions de logique de formulaire incorrectes, référencement de questions incorrect, libellés manquants). Les messages d'erreur du formulaire apparaissent généralement lors de l'importation, du déploiement ou de l'ouverture d'un formulaire. |
| Prévisualisation | Cette étape vous permet de visualiser le formulaire tel qu'il sera affiché aux répondants et de vérifier que tous les éléments fonctionnent correctement avant le déploiement (par exemple, la mise en page du formulaire, les libellés des questions et des choix). |
| Test | Cette étape consiste à saisir des données pour tester le fonctionnement du formulaire (par exemple, vérifier les apparences des questions, les options de choix et la logique de formulaire). Les tests peuvent être effectués en mode **APERÇU** avant le déploiement. |

Valider et tester continuellement votre XLSForm au fur et à mesure des modifications simplifiera la résolution de problèmes et aidera à identifier la cause de tout problème. Il est essentiel de s'assurer que votre formulaire fonctionne comme prévu avant de lancer la collecte de données.

Lors de la prévisualisation et du test de votre formulaire, utilisez la même plateforme que celle que vous utiliserez pour la collecte de données : [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html), [KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html), ou les deux.

<p class="note">
Pour en savoir plus sur la configuration de KoboCollect pour prévisualiser et tester vos formulaires, consultez l'article <a href="https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html">Configurer l'application KoboCollect</a>.
</p>

Si vous avez du mal à trouver la source d'une erreur dans votre XLSForm, essayez d'importer le formulaire dans [XLSForm Online](https://getodk.org/xlsform/) par ODK, qui peut souvent fournir des messages d'erreur et des avertissements plus détaillés pour vous aider à identifier et corriger les problèmes avant d'importer le formulaire dans KoboToolbox.

## Résolution de problèmes

<details>
<summary><strong>Message d'erreur lors de l'importation, de la prévisualisation ou du déploiement d'un XLSForm</strong></summary>

Si votre XLSForm contient une erreur, un message d'erreur s'affiche, indiquant généralement la ligne, la question ou l'expression exacte où se trouve le problème. Après avoir corrigé l'erreur dans votre tableur, vous devrez importer à nouveau le fichier.

| Messages d'erreur courants | Explication courante |
| :--- | :--- |
| `The survey sheet is either empty or missing important column headers.` | Des en-têtes de colonnes obligatoires sont manquants ou mal orthographiés. |
| `The survey element named 'name' has no label or hint.` | L'une des questions de votre formulaire ne possède pas de libellé. |
| `FormLogicError: Could not evaluate: [expression], message: The string did not match the expected pattern.` | Une expression de logique de formulaire contient des erreurs, telles qu'une syntaxe de référencement de questions incorrecte ou une parenthèse manquante. |
| `unable to deploy ODK Validate Errors: >> XForm is invalid` | Une expression de logique de formulaire contient des erreurs, telles qu'une syntaxe de référencement de questions incorrecte ou une parenthèse manquante. |
| `There has been a problem trying to replace ${question} with the XPath to the survey element named 'question'. There is no survey element with this name.` | Vous faites référence à une question de votre formulaire qui n'existe pas ou dont le nom est mal orthographié. Assurez-vous d'utiliser le nom **exact** de la question dans vos expressions de logique de formulaire. |
| `'list_name'`<br>`​​List name not in choices sheet` | La liste d'options d'une question n'a pas été définie, ou il y a une faute de frappe dans le `list_name`. |
| `Choice names must be unique for each choice list. If this is intentional, use the setting 'allow_choice_duplicates'.` | Des noms de choix en double ont été utilisés dans la même liste d'options. Supprimez le ou les noms de choix en double, ou autorisez les doublons dans les <a href="https://support.kobotoolbox.org/fr/form_settings_xls.html#available-form-settings-in-xlsform">paramètres de formulaires</a>. |
| `Unmatched begin statement: group (group)` | Un groupe de questions ne possède pas la ligne `end_group` correspondante. |
| `Can't find external_file.csv` <br> `Failed to load external_file.csv.` | Une <a href="https://support.kobotoolbox.org/fr/pull_data_kobotoolbox.html">pièce jointe externe</a> liée à votre formulaire (par exemple, lors de l'utilisation de `pulldata()`) n'a pas été importée dans KoboToolbox. |
| `Can't find survey.xml` | Les <a href="https://support.kobotoolbox.org/fr/dynamic_data_attachment.html">liaisons dynamiques de projets</a> n'ont pas été correctement configurées dans les paramètres de votre projet. |
| `'select_from_list_name'` | Un nom de liste est manquant dans la colonne `type` après `select_one` ou `select_multiple`. |
</details>

<br>

<details>
<summary><strong>Message d'erreur : Choice names must be unique for each choice list</strong></summary>
<br>

![Message d'erreur nom invalide](images/xlsform_with_kobotoolbox/error-message-invalid-name.png)

Cette erreur signifie qu'au moins deux lignes de la même liste de <strong>choix</strong> partagent la même valeur dans le champ <strong>name</strong>.

Par exemple :

| list_name | name | label |
|:---|:---|:---|
| yn | yes | Yes, always |
| yn | yes | Yes, sometimes |
| yn | no | No, never |
| choices |

Pour corriger les noms de choix en double :
1. Ouvrez votre XLSForm.
2. Accédez à l'**onglet choices**.
3. Trouvez le numéro de ligne référencé dans le message d'erreur.
4. Vérifiez la colonne `name` pour repérer les valeurs en double au sein du même `list_name`.
5. Mettez à jour la valeur `name` en double afin que chaque `name` de la liste soit unique.
5. Enregistrez le fichier, puis <a href="https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#replacing-a-form-with-an-xlsform">importez</a> et redéployez à nouveau le formulaire.

Si les valeurs `name` en double sont intentionnelles (par exemple, lors de l'utilisation de [filtres de choix](https://support.kobotoolbox.org/fr/choice_filters_xls.html)), vous pouvez autoriser les doublons dans les [paramètres de formulaires](https://support.kobotoolbox.org/fr/form_settings_xls.html#available-form-settings-in-xlsform).

</details>

<br>

<details>
<summary><strong>Message d'erreur : List name not in choices sheet</strong></summary>
<br>

![Message d'erreur nom de liste](images/xlsform_with_kobotoolbox/error-message-list-name.png)

Cette erreur se produit lorsqu'une question utilise une liste d'options qui n'existe pas dans l'**onglet choices**, ou lorsque le nom de liste dans la colonne `list_name` est mal orthographié.

Par exemple :

**onglet survey**
| type | name | label |
|:---|:---|:---|
| select_one yes_no | service | Do you like the service at the supermarket? |
| survey |

**onglet choices**

| list_name | name | label |
|:---|:---|:---|
| yes_n | yes_always | Yes, always |
| yes_n | yes_sometimes | Yes, sometimes |
| yes_n | no | No, never |
| choices |

Pour corriger le nom de liste manquant ou incorrect :

<ol>
<li>Ouvrez votre XLSForm.</li>
<li>Accédez à l'onglet <code>survey</code>.</li>
<li>Trouvez la question qui utilise le nom de liste référencé dans le message d'erreur (par exemple, <code>select_one yes_no</code>).</li>
<li>Accédez à l'onglet <code>choices</code> et vérifiez dans la colonne <code>list_name</code> qu'il existe une correspondance exacte avec le nom de liste référencé dans le message d'erreur.</li>
<li>Effectuez l'une des actions suivantes :
  <ul>
    <li><strong>Si le nom de liste est manquant :</strong> Ajoutez une nouvelle liste de choix pour cette question. Assurez-vous que le <code>list_name</code> est écrit exactement comme il apparaît dans l'onglet <code>survey</code>.</li>
    <li><strong>Si le nom de liste existe mais est orthographié différemment :</strong> Corrigez la faute de frappe afin que le nom de liste corresponde exactement dans les onglets <code>survey</code> et <code>choices</code>.</li>
  </ul>
</li>
<li>Enregistrez le fichier, puis <a href="https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#replacing-a-form-with-an-xlsform">importez</a> et redéployez à nouveau le formulaire.</li>
</ol>

</details>

<br>

<details>
<summary><strong>Difficulté à identifier l'erreur dans le XLSForm</strong></summary>
Si vous avez du mal à trouver la source d'une erreur dans votre XLSForm, essayez d'importer le formulaire dans <a href="https://getodk.org/xlsform/">XLSForm Online</a> par ODK. Cet outil peut fournir des messages d'erreur et des avertissements plus détaillés, ce qui peut vous aider à identifier et corriger les problèmes avant d'importer le formulaire dans KoboToolbox.

</details>

<br>

<details>
<summary><strong>Erreur lors de l'importation d'un XLSForm via une URL</strong></summary>
Vérifiez que l'URL que vous utilisez est correcte. Lorsqu'elle est chargée dans un navigateur, l'URL doit déclencher le téléchargement d'un fichier, et non ouvrir une page web.
</details>

<br>

<details>
<summary><strong>L'importation via URL n'affiche pas la version non déployée</strong></summary>
Si vous avez importé un lien et que vous ne voyez pas la nouvelle version du formulaire, actualisez votre navigateur.
</details>

<br>

<details>
<summary><strong>Échec de la soumission d'un formulaire web</strong></summary>
Si la soumission d'un formulaire web échoue, vérifiez si votre formulaire utilise un <strong>terme réservé XLSForm</strong> dans la colonne <code>name</code>. Les termes réservés sont des termes qui ne peuvent pas être utilisés comme noms de questions car ils sont utilisés par le moteur XForms sous-jacent pour la structure, la logique ou l'analyse des données (par exemple, type, label, start, today). L'utilisation de ces termes peut entraîner des erreurs de validation du formulaire, des échecs de publication ou des problèmes d'export de données.<br><br>

Pour corriger le problème, renommez la question concernée avec une valeur différente, puis redéployez le formulaire. Ce problème affecte généralement les formulaires web même lorsque le formulaire s'ouvre normalement, tandis que KoboCollect peut continuer à fonctionner comme prévu. Notez que les soumissions déjà enregistrées avec l'ancienne version du formulaire peuvent rester non soumettables ; il est donc important de mettre à jour le formulaire dès que possible si vous collectez des données via des formulaires web. Veillez toujours à <strong>tester la soumission du formulaire avant de lancer la collecte de données</strong> afin de détecter rapidement les problèmes de nommage.
</details>