# Utiliser des fonctions avec XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/3e68d0f83165ae0b4339daef4fd4090b2efeeb46/source/functions_xls.md" class="reference">15 fév. 2026</a>

Les fonctions sont des opérations prédéfinies utilisées pour effectuer des calculs ou manipuler des données dans un XLSForm. Elles sont essentielles pour automatiser des tâches et extraire des informations clés de vos formulaires, vous permettant de calculer des indicateurs de projet, de créer des systèmes de notation et de gérer les dates efficacement.

Cet article répertorie les fonctions couramment utilisées dans XLSForm, notamment les fonctions permettant de manipuler des nombres, des chaînes de caractères, des dates et des points GPS.

<p class="note">
  Pour en savoir plus sur la logique de formulaire dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>. Pour en savoir plus sur les fonctions utilisées spécifiquement dans les groupes répétés, consultez l'article <a href="https://support.kobotoolbox.org/fr/repeat_groups_xls.html">Groupes répétés dans XLSForm</a>.
</p>

## Fonctions couramment utilisées dans XLSForm

Les fonctions suivantes sont parmi les plus fréquemment utilisées dans XLSForm. Elles permettent de contrôler le comportement du formulaire, de gérer les réponses et d'effectuer des calculs de base ou des opérations logiques sur l'ensemble des questions. Ces fonctions peuvent être appliquées dans des calculs, des contraintes, des conditions de pertinence et d'autres expressions dans votre formulaire.

| Fonction | Description |
|:-----------|:-------------|
| `if(expression, then, else)` | Si l'expression est TRUE, renvoie `then`. Sinon, renvoie `else`. |
| `selected(${question_name}, option_name)` | Permet de déterminer si un choix spécifique a été sélectionné dans une question `select_multiple`. |
| `random()` | Renvoie un nombre aléatoire compris entre 0,0 (inclus) et 1,0 (exclus). |
| `count-selected(${question_name})` | Renvoie le nombre d'options sélectionnées dans une question `select_multiple`. |
| `coalesce(${question1}, ${question2})` | Renvoie la première valeur non vide des deux arguments. Renvoie une chaîne vide si les deux sont vides ou inexistants. |
| `jr:choice-name(choice_name, '${question_name}')` | Renvoie la valeur du libellé, dans la langue active, associée à `choice_name` dans la liste de choix d'une question de type select. Pour récupérer le libellé du choix sélectionné, utilisez `jr:choice-name(${question_name}, '${question_name}')`. |
| `selected-at(${question_name}, n)` | Renvoie le choix sélectionné dans une question `select_multiple` à la position **n+1**. Par exemple, `selected-at(${question_name}, 2)` renvoie le troisième choix sélectionné dans une question `select_multiple`. |
| `once(expression)` | Évalue une expression une seule fois (par exemple, pour s'assurer qu'un nombre aléatoire n'est généré qu'une seule fois, ou pour conserver la première valeur saisie pour une question même si la réponse est modifiée ultérieurement). |
| `instance('list_name')/root/item[name = ${question}]/column_name` | Récupère une valeur dans l'onglet choices. Recherche dans la liste de choix nommée `list_name`, trouve la ligne où le `name` du choix correspond à la réponse à `${question}`, et renvoie la valeur de la colonne spécifiée comme `column_name`. |

## Fonctions pour manipuler les nombres

Les fonctions suivantes sont utilisées pour effectuer des opérations mathématiques ou transformer des valeurs numériques dans XLSForm. Elles vous permettent de calculer, d'arrondir ou de convertir des nombres, ainsi que d'appliquer des expressions mathématiques plus avancées si nécessaire.

| Fonction | Description |
|:---------|:------------|
| `int(number)` | Transforme un nombre décimal en entier sans arrondi. |
| `round(number, places)` | Arrondit une valeur décimale à un nombre prédéfini de décimales. |
| `pow(number, power)` | Calcule la puissance d'un nombre. |
| `number(x)` | Convertit x (une chaîne de caractères ou une expression booléenne) en valeur numérique. |
| `log(number)` <br> `log10(number)` | Renvoie le logarithme naturel ou le logarithme en base 10 d'un nombre. |
| `abs(number)` | Renvoie la valeur absolue d'un nombre. |
| `sin(number)` <br> `asin(number)` <br> `cos(number)` <br> `acos(number)` <br> `tan(number)` <br> `atan(number)` | Renvoie le sinus/arc sinus, le cosinus/arc cosinus ou la tangente/arc tangente d'un nombre. |
| `sqrt(number)` | Renvoie la racine carrée d'un nombre. |
| `exp(x)` <br> `exp10(x)` | Renvoie e^x ou 10^x. |
| `pi()` | Renvoie une approximation de la constante mathématique π. |

<p class="note">
  <strong>Note :</strong> À l'intérieur de ces fonctions, il est possible d'inclure des constantes ou des <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html#question-referencing">références à des questions</a>.
</p>

## Fonctions pour manipuler les chaînes de caractères

Les fonctions suivantes sont utilisées pour créer, modifier ou analyser des chaînes de caractères dans XLSForm. Elles sont utiles pour combiner du texte, rechercher des motifs ou des caractères spécifiques, et nettoyer ou mettre en forme des saisies textuelles.

| Fonction | Description |
|:---------|:------------|
| `concat()` | Concatène un ou plusieurs arguments (séparés par des virgules) en une seule chaîne de caractères. |
| `regex(string, expression)` | Renvoie `TRUE` si la chaîne correspond exactement et intégralement à une <a href="https://support.kobotoolbox.org/fr/restrict_responses.html">expression régulière</a>. |
| `contains(string, substring)` | Renvoie `TRUE` si la chaîne contient la sous-chaîne. |
| `starts-with(string, substring)` | Renvoie `TRUE` si la chaîne commence par la sous-chaîne. |
| `ends-with(string, substring)` | Renvoie `TRUE` si la chaîne se termine par la sous-chaîne. |
| `substr(string, start, end)` | Renvoie la sous-chaîne de `string` commençant à l'index `start` et s'étendant jusqu'à l'index `end` (non inclus), ou jusqu'à la fin de `string` si `end` n'est pas fourni. |
| `substring-before(string, target)` | Renvoie la sous-chaîne de `string` située avant la première occurrence de la sous-chaîne cible. Si la cible n'est pas trouvée, ou si `string` commence par la sous-chaîne cible, cette fonction renvoie une chaîne vide. |
| `substring-after(string, target)` | Renvoie la sous-chaîne de `string` située après la première occurrence de la sous-chaîne cible. Si la cible n'est pas trouvée, cette fonction renvoie une chaîne vide. |
| `translate(string, fromchars, tochars)` | Renvoie une copie de la chaîne dans laquelle chaque occurrence d'un caractère de `fromchars` est remplacée par le caractère correspondant dans `tochars` (par exemple, pour remplacer toutes les lettres minuscules par des majuscules). <br><br> <strong>Note :</strong> Si `fromchars` est plus long que `tochars`, chaque occurrence d'un caractère de `fromchars` qui n'a pas de caractère correspondant dans `tochars` sera supprimée. |
| `string-length(string)` | Renvoie le nombre de caractères dans `string` (par exemple, pour ajouter une limite de mots à une question de type texte). |
| `normalize-space(string)` | Renvoie une chaîne dans laquelle les espaces en début et en fin de chaîne sont supprimés, et les séquences d'espaces sont remplacées par un espace unique. |

## Fonctions pour manipuler les dates et les heures

Les fonctions suivantes sont utilisées pour enregistrer, mettre en forme et calculer des valeurs de date et d'heure dans XLSForm. Elles permettent de capturer la date ou l'heure actuelle, de convertir du texte en format de date, ou d'afficher des dates et des heures dans un format spécifique.

| Fonction | Description |
|:---------|:------------|
| `today()` | Renvoie la date actuelle sans composante horaire. |
| `now()` | Renvoie la date et l'heure actuelles au format ISO 8601, fuseau horaire inclus. |
| `date('YYYY-MM-DD')` | Force les dates dans le format de date correct (notamment pour les dates antérieures à 1970). |
| `format-date(date, format)` | Renvoie `date` sous forme de chaîne formatée selon <code>format</code>. Les formats courants incluent : <ul><li><code>%Y</code> : année sur 4 chiffres</li><li><code>%y</code> : année sur 2 chiffres</li><li><code>%m</code> : mois avec zéro de remplissage</li><li><code>%n</code> : mois numérique</li><li><code>%b</code> : mois en texte court (Jan, Fév, Mar…)</li><li><code>%d</code> : jour du mois avec zéro de remplissage</li><li><code>%e</code> : jour du mois</li><li><code>%a</code> : jour en texte court (Dim, Lun, Mar…).</li></ul> |
| `format-date-time(datetime, format)` | Renvoie `datetime` sous forme de chaîne formatée selon <code>format</code>. Les formats courants incluent : <ul><li><code>%H</code> : heure avec zéro de remplissage (format 24 h)</li><li><code>%h</code> : heure (format 24 h)</li><li><code>%M</code> : minutes avec zéro de remplissage</li><li><code>%S</code> : secondes avec zéro de remplissage</li><li><code>%3</code> : millisecondes avec zéro de remplissage.</li></ul> |
| `decimal-time()` | Convertit une heure en valeur décimale (par exemple, 12 h 00 devient 0,5), facilitant la logique de formulaire basée sur le temps. |

## Fonctions pour manipuler les données GPS

Les fonctions suivantes sont utilisées pour travailler avec des données géographiques collectées via des questions GPS dans XLSForm. Elles permettent de calculer des distances, des périmètres ou des surfaces à partir de réponses de type geopoint, geotrace ou geoshape.

| Fonction | Description |
|:---------|:------------|
| `area(${geoshape})` | Renvoie la superficie, en mètres carrés, d'une valeur `geoshape`. |
| `distance(geo)` | Renvoie la distance, en mètres, correspondant à : <ul><li>le périmètre d'une valeur `geoshape`</li><li>la longueur d'une valeur `geotrace`</li><li>une liste de geopoints spécifiés sous forme de chaînes de caractères ou de références à d'autres champs (y compris issus de groupes répétés), séparés par des virgules</li></ul> |
| `geofence(${geopoint}, ${geoshape})` | Renvoie `TRUE` si le `${geopoint}` spécifié se trouve à l'intérieur du `${geoshape}` spécifié, `FALSE` dans le cas contraire. Disponible uniquement dans KoboCollect. |