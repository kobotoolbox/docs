# Extraire des données d'un fichier CSV externe
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/e1faceb429db5362522392101ee2d88578d98fc8/source/pull_data_kobotoolbox.md" class="reference">6 mai 2026</a>

La fonction `pulldata()` dans XLSForm vous permet de récupérer dynamiquement des informations depuis un fichier CSV externe lors de la saisie d'un formulaire. Cela vous permet de référencer des bases de données existantes et d'importer automatiquement des informations associées, évitant ainsi aux enquêteurs de ressaisir les mêmes données.

Par exemple, vous pouvez utiliser `pulldata()` pour :
- **Remplir automatiquement des informations associées :** Lorsqu'un identifiant, un code ou une clé est saisi, récupérer automatiquement les détails associés tels qu'un nom, une catégorie ou une description.
- **Précharger des données de référence :** Charger des informations depuis des fichiers externes afin que les enquêteurs n'aient à collecter que les données nouvelles ou mises à jour.

<p class="note">
    <strong>Note :</strong> La fonction <code>pulldata()</code> utilise des fichiers CSV externes comme source de données. Si vous souhaitez référencer des données provenant d'un autre projet KoboToolbox plutôt que d'un fichier CSV, vous pouvez utiliser la <a href="../fr/dynamic_data_attachment.html">liaison dynamique de projets</a>.
</p>

L'utilisation de `pulldata()` contribue à réduire les erreurs, à gagner du temps lors de la collecte de données et à garantir la cohérence des formulaires avec les bases de données de référence externes. Cette fonction est disponible avec <a href="../fr/data_collection_kobocollect.html">l'application Android KoboCollect</a> et les <a href="../fr/data_through_webforms.html">formulaires web</a>. Nous recommandons d'utiliser <a href="../fr/getting_started_xlsform.html">XLSForm</a> pour configurer la fonction `pulldata()`.

Cet article couvre les étapes suivantes pour extraire des données d'un fichier CSV externe :
- Configurer votre fichier CSV externe
- Configurer votre XLSForm
- Importer votre fichier CSV externe dans KoboToolbox

## Configurer votre fichier CSV externe

Pour utiliser `pulldata()`, commencez par préparer un fichier CSV externe contenant les données de référence que vous souhaitez récupérer. Chaque ligne doit représenter un enregistrement unique (par exemple, un participant, un lieu ou un élément) et le fichier doit comporter au moins deux colonnes. L'une d'elles doit contenir la **variable d'index** qui correspond aux valeurs saisies dans votre formulaire.

La **variable d'index** joue le rôle de [clé primaire](https://fr.wikipedia.org/wiki/Cl%C3%A9_primaire) qui relie votre XLSForm au fichier CSV externe. Il doit s'agir d'un identifiant unique présent dans les deux fichiers, tel qu'un identifiant de participant, un nom de district ou tout autre code correspondant.

Les colonnes restantes peuvent contenir tous les détails supplémentaires que vous souhaitez récupérer, tels que des noms, des catégories ou des descriptions. Assurez-vous que le fichier CSV est propre, formaté de manière cohérente et enregistré avec l'extension `.csv`.

**Exemple : eligibility.csv**

| ID           | status          | age             |
|:-----------  |:----------------|:----------------|
| AH784N       | eligible        | 19              |
| DB839K       | ineligible      | 37              |
| SH849T       | eligible        | 42              |

<p class="note">
<strong>Note :</strong> Pour utiliser <code>pulldata()</code> avec des questions <code>select_one</code> ou <code>select_multiple</code>, la valeur dans le fichier externe doit correspondre au <strong>nom du choix</strong>, et non au libellé du choix. Pour les questions <code>select_multiple</code>, listez plusieurs noms de choix séparés par un espace.
</p>

## Configurer votre XLSForm

Une fois votre fichier CSV externe configuré, paramétrez votre XLSForm de la manière suivante :

1. Assurez-vous que votre XLSForm contient une question servant de **variable d'index**.
2. Ajoutez une nouvelle question à votre formulaire pour récupérer des données depuis le fichier externe, en utilisant l'une des deux approches suivantes :
    * Ajoutez une question `calculate` pour récupérer et stocker des valeurs en vue d'une utilisation ultérieure dans le formulaire ou la base de données. Par exemple, vous pouvez l'utiliser pour afficher une valeur dans une note ou le libellé d'une question, ou pour utiliser la valeur dans des calculs et une logique de saut.
    * Ajoutez une question `text`, `integer`, `decimal`, `date`, `select_one` ou `select_multiple` pour inclure les valeurs récupérées comme réponses par défaut dans des champs modifiables.
3. Dans la colonne `calculation` de votre nouvelle question, utilisez la fonction **pulldata()** pour indiquer quel champ du fichier CSV récupérer. Utilisez la syntaxe suivante : `pulldata('csv','pull_from', 'csv_index', ${survey_index})`.
    - `csv` est le nom du fichier CSV, sans l'extension.
    - `pull_from` désigne la colonne de votre fichier CSV contenant les données que vous souhaitez importer dans votre formulaire.
    - `csv_index` est la colonne de votre fichier CSV contenant la **variable d'index**.
    - `survey_index` est le nom de la question de votre formulaire contenant la **variable d'index**.

  **onglet survey**

  | type      | name               | label                                      | calculation |
|:-----------|:------------------|:-------------------------------------------|:-------------|
| text       | respondent_id      | Respondent ID                              |              |
| calculate  | eligibility_status |                                            | pulldata('eligibility', 'status', 'ID', ${respondent_id}) |
| note       | eligibility_note   | Respondent is ${eligibility_status} for the study. |              |
| integer    | respondent_age     | Respondent age | pulldata('eligibility', 'age', 'ID', ${respondent_id}) |
| survey | 

Dans l'exemple ci-dessus, le calcul récupère la valeur de la colonne `status` du fichier `eligibility.csv`, dans la ligne où l'`ID` du fichier CSV correspond à l'identifiant saisi dans la question `respondent_id` de votre formulaire. Ensuite, il récupère et affiche l'âge du répondant depuis la colonne `age` du fichier `eligibility.csv`.

<p class="note">
<strong>Note :</strong> Après avoir utilisé la fonction <code>pulldata()</code> pour récupérer des données d'un fichier CSV externe, vous pouvez référencer ce champ dans des conditions de logique de saut, des contraintes et des libellés ultérieurs, comme n'importe quel autre champ ou calcul.
</p>

## Importer votre fichier CSV externe dans KoboToolbox

La dernière étape pour lier votre fichier CSV externe à votre formulaire consiste à importer le fichier dans KoboToolbox. Pour ce faire :
1. Accédez aux **PARAMÈTRES** de votre projet et ouvrez l'onglet **Média**.
2. Importez le ou les fichiers CSV en utilisant exactement le nom que vous avez indiqué dans votre XLSForm.
3. Déployez ou redéployez le formulaire.

![Upload media](images/pull_data_kobotoolbox/upload_media.png)

<p class="note">
    Pour en savoir plus sur l'importation de fichiers multimédias, consultez l'article <a href="../fr/upload_media.html">Importer des fichiers multimédias dans un projet</a>.
</p>

## Résolution de problèmes

<details>
  <summary><strong>Les polices non latines ou les caractères spéciaux ne s'affichent pas correctement</strong></summary>
  Enregistrez votre fichier CSV au <strong>format UTF-8</strong>. Cela garantit que les appareils Android peuvent afficher correctement les textes non latins ou les caractères spéciaux.
</details>

<br>

<details>
  <summary><strong>Les valeurs numériques ne fonctionnent pas comme prévu</strong></summary>
  Toutes les données extraites d'un fichier CSV sont traitées comme du texte. Pour utiliser ces valeurs comme des nombres, appliquez les <a href="../fr/functions_xls.html">fonctions</a> <code>int()</code> ou <code>number()</code> à la valeur récupérée dans votre XLSForm.
</details>

<br>

<details>
  <summary><strong>Protection des données sensibles</strong></summary>
  Si votre fichier CSV contient des informations sensibles que vous ne souhaitez pas importer sur le serveur, importez un fichier CSV vide avec votre formulaire. Remplacez-le ensuite manuellement sur chaque appareil par le vrai fichier CSV. Cette approche fonctionne uniquement avec l'application KoboCollect.
</details>

<br>

<details>
  <summary><strong>Chargement lent du formulaire avec des fichiers volumineux</strong></summary>
    Si vous utilisez des fichiers CSV très volumineux, le chargement du formulaire dans KoboCollect ou les formulaires web peut être lent. Pour améliorer les performances, n'incluez que les données nécessaires au formulaire et envisagez de diviser un formulaire volumineux en plusieurs formulaires, chacun avec son propre fichier CSV. Vous pouvez également diviser les fichiers CSV volumineux en fichiers plus petits lorsque cela est possible, et/ou utiliser la colonne <a href="../fr/question_options_xls.html#additional-question-options">trigger</a> pour n'extraire les données que du fichier pertinent et uniquement lorsque cela est nécessaire.
</details>

<br>

<details>
  <summary><strong>Extraction de dates depuis des fichiers CSV externes</strong></summary>
  Si vous stockez des dates dans un fichier CSV externe et souhaitez les importer dans un formulaire, assurez-vous qu'elles sont au format AAAA-MM-JJ. Si vous modifiez votre fichier CSV dans Excel, ajoutez une apostrophe <code>'</code> devant la date pour éviter la mise en forme automatique des dates par Excel.
</details>

<br>

<details>
  <summary><strong>La fonction pulldata() ne fonctionne pas correctement</strong></summary>
  Si la fonction pulldata() ne fonctionne pas correctement, essayez les solutions suivantes :
  <ul>
  <li>Renommez votre fichier CSV pour supprimer les tirets bas ou les caractères spéciaux.</li>
  <li>Vérifiez que votre fichier CSV est correctement configuré avec une variable par colonne (voir la publication du <a href="https://community.kobotoolbox.org/t/pulldata-is-not-working-on-kobocollect-android/6462/39">Forum communautaire</a>).</li>
  <li>Vérifiez que vous utilisez l'orthographe exacte pour les noms de fichiers et les noms de colonnes.</li>
  <li>Vérifiez que les cellules de votre fichier CSV ne contiennent pas d'espaces supplémentaires avant ou après la valeur.</li>
</ul>
</details>

<br>