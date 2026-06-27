# Gérer les choix de réponse dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/1b55b2580defd73765e9c2ad608141a3428ee504/source/option_choices_xls.md" class="reference">4 Jan 2026</a>

XLSForm simplifie la création et la gestion des **listes de choix de réponse** pour les formulaires d'enquête. Cela est particulièrement utile pour les listes longues ou répétitives, comme les noms de pays ou de villes. Les choix de réponse sont définis pour les questions de type `select_one`, `select_multiple` ou `rank` ([questions à choix multiple](https://support.kobotoolbox.org/fr/question_types_xls.html#select-question-types)).

Cet article explique comment définir et gérer les choix de réponse dans XLSForm pour des formulaires complexes, ainsi que les bonnes pratiques pour nommer les choix.

<p class="note">
Pour en savoir plus sur la création de formulaires avec XLSForm, consultez l'article <a href="getting_started_xlsform.html">Créer un XLSForm</a>.
</p>

## Définir les choix de réponse dans XLSForm
Les choix de réponse sont définis dans l'**onglet choices** de votre XLSForm. L'onglet choices comprend trois colonnes obligatoires :

| Colonne | Description |
| :---------  | :--------  |
| `list_name` | Identifiant unique d'une liste de choix de réponse, qui relie la question de l'onglet `survey` à sa liste de choix dans l'onglet `choices`. |
| `name` | Nom court et unique utilisé pour désigner chaque choix de réponse. |
| `label` | Texte du choix tel qu'il sera affiché dans le formulaire. |

Pour définir une liste de choix de réponse dans XLSForm :

1.  Dans l'**onglet choices**, saisissez le **nom de la liste de choix** dans la colonne `list_name`.
2.  Saisissez un `name` court et un `label` pour chaque option, en utilisant le même `list_name` pour toutes les options de la liste.

**onglet choices**

| list_name | name | label |
| :---------  | :---------  | :---------  |
| marital_options | single | Single |
| marital_options | married | Married |
| marital_options | separated_divorced | Separated/Divorced |
| marital_options | widowed | Widowed |
| choices |

3.  Dans l'**onglet survey**, ajoutez votre question. Dans la colonne `type`, saisissez le type de question suivi d'un espace et du `list_name` correspondant à votre liste de choix.
    - Une liste de choix peut être réutilisée pour plusieurs questions dans l'onglet `survey`.

**onglet survey**

| type | name | label |
| :---------  | :---------  | :---------  |
| acknowledge | consent | Do you agree to proceed with the interview? |
| select_one marital_options | marital_status | What is your marital status? |
| survey |

 
## Bonnes pratiques pour nommer les choix de réponse

Lorsque les données sont téléchargées au [format pour les valeurs et l'en-tête XML](https://support.kobotoolbox.org/fr/export_download.html#value-and-header-format), chaque question apparaît comme une variable ou une colonne distincte dans la base de données. Les valeurs dans chaque colonne correspondent aux **noms des choix** définis dans l'onglet `choices`, et non aux libellés complets affichés aux répondants. Ce format est recommandé pour l'analyse, car il fournit des noms de variables courts et cohérents ainsi que des valeurs codées plus faciles à utiliser que les libellés complets des questions ou des options.

Lors de la définition des noms de choix :
- Utilisez uniquement des **lettres, des chiffres et des tirets bas**. Les espaces et les caractères spéciaux ne sont pas autorisés.
- Évitez les chaînes de texte trop longues ou complexes, car ces valeurs apparaîtront dans votre base de données exportée et pourront être utilisées dans la [logique de formulaire](https://support.kobotoolbox.org/fr/form_logic_xls.html).
- Veillez à ce que les noms soient **cohérents** d'une liste à l'autre afin de faciliter l'analyse des données.
 

## Gérer les listes de choix dans XLSForm

### Réutiliser des listes de choix
L'utilisation de `list_name` dans XLSForm vous permet de **réutiliser facilement des listes de choix** pour plusieurs questions, sans avoir à les ressaisir manuellement. Par exemple, vous pouvez créer une liste de choix `yes_no` et l'appliquer à toutes vos questions Oui/Non. Cela permet de créer des formulaires de manière plus efficace et cohérente.

### Traduire des listes de choix

XLSForm simplifie la traduction des listes de choix. Vous pouvez ajouter plusieurs libellés pour différentes langues, chaque traduction dans une colonne `label` distincte. Les noms des choix sous-jacents restent identiques, ce qui garantit la cohérence de la base de données exportée entre les différentes traductions et facilite l'analyse.

<p class="note">
Pour en savoir plus sur l'ajout de traductions dans XLSForm, consultez l'article <a href="language_xls.html">Ajouter des traductions dans XLSForm</a>.
</p>

### Fichiers média comme choix de réponse

En plus du texte, les choix de réponse dans XLSForm peuvent également être des **fichiers média**, tels que des images, des fichiers audio ou des vidéos. Cela enrichit l'expérience de l'enquête en fournissant des repères visuels ou sonores aux répondants.

<p class="note">
Pour en savoir plus sur l'utilisation de fichiers média comme choix de réponse, consultez l'article <a href="media.html">Ajouter des médias à un XLSForm</a>.
</p>

### Filtrer des listes de choix

XLSForm vous permet de filtrer les listes de choix de réponse en fonction des réponses aux questions précédentes. Cette fonctionnalité, connue sous le nom de **filtres de choix**, peut être utilisée de différentes manières. Par exemple, elle peut servir pour des **questions à sélection en cascade**, où la liste de choix d'une question secondaire (ex. : villes) est filtrée en fonction de la réponse à une question principale (ex. : pays). Elle peut également être utilisée pour filtrer une question à choix multiple afin d'afficher uniquement les options sélectionnées dans une question précédente.

<p class="note">
Pour en savoir plus sur le filtrage des listes de choix dans XLSForm, consultez l'article <a href="choice_filters_xls.html">Ajouter des filtres de choix dans XLSForm</a>.
</p>

### Dupliquer des noms de choix

Au sein d'une liste de choix de réponse donnée, **les noms des choix doivent être uniques**. Cependant, le même nom de choix peut être réutilisé dans différentes listes. Par exemple, une liste de choix `yes_no` et une liste `yes_no_maybe` peuvent toutes deux inclure les noms de choix `yes` et `no`.

Par défaut, le déploiement d'un formulaire contenant des noms de choix répétés dans la même liste génère une erreur. Toutefois, lors de l'utilisation de filtres de choix, il peut être nécessaire d'autoriser des noms de choix en double au sein d'une liste. Pour activer cette option, activez le paramètre `allow_choice_duplicates` dans l'**onglet settings**.

<p class="note">
Pour plus d'informations, consultez l'article <a href="form_settings_xls.html">Paramètres de formulaires dans XLSForm</a>.
</p>

### Gérer les longues listes de choix

Pour les listes de choix très longues, contenant des centaines ou des milliers d'options, il est recommandé d'utiliser les types de questions `select_one_from_file` ou `select_multiple_from_file`, qui relient une question à un **fichier externe** contenant la liste de choix. Cette approche est plus efficace que la saisie manuelle des choix dans le XLSForm, permet d'éviter des temps de chargement lents et des XLSForms volumineux, et simplifie la gestion ou la modification de listes d'options étendues.

<p class="note">
Pour en savoir plus sur les listes de choix externes dans XLSForm, consultez l'article <a href="select_from_file_xls.html">Sélectionner des options à partir d'un fichier externe avec XLSForm</a>.
</p>