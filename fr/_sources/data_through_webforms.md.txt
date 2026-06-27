# Collecte de données via des formulaires web
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/7422ce15732061510b56a7bf2bfb464ddee641a0/source/data_through_webforms.md" class="reference">6 mai 2026</a>

Les formulaires web KoboToolbox vous permettent de **collecter des données directement dans un navigateur web**, sans installer d'application. Ce sont des versions de votre formulaire accessibles depuis un navigateur, que vous pouvez utiliser pour prévisualiser et tester votre questionnaire, ou pour collecter des données réelles sur des téléphones, tablettes et ordinateurs.

Les formulaires web fonctionnent sur la plupart des appareils modernes, notamment les appareils Android, les iPhones, les iPads, les ordinateurs portables et les ordinateurs de bureau. Ils sont particulièrement utiles dans les projets où les répondants remplissent un formulaire via un lien partagé, où l'équipe de collecte de données utilise différents types d'appareils, ou lorsque vous souhaitez saisir des données sur un ordinateur plutôt que via une application.

Les formulaires web permettent également la **collecte de données hors ligne** une fois le formulaire ouvert et mis en cache dans le navigateur. Ils intègrent toute la logique de formulaire configurée dans KoboToolbox, notamment la logique de saut et les critères de validation, et leur apparence peut être personnalisée grâce à différents [thèmes de formulaires web](https://support.kobotoolbox.org/fr/alternative_enketo.html).

<p class="note">
<strong>Note :</strong>
 Les formulaires web KoboToolbox étaient auparavant propulsés par <a href="https://enketo.org">Enketo</a>, c'est pourquoi ils étaient appelés « formulaires web Enketo » dans les anciennes documentations.
</p>

Cet article couvre les points suivants :
- Partager des formulaires web KoboToolbox pour la collecte de données
- Choisir le bon mode de formulaire web
- Collecter des données et enregistrer des brouillons dans le navigateur
- Utiliser les formulaires web hors ligne
- Personnaliser les liens de formulaires web pour des cas d'utilisation spécifiques
- Résoudre les problèmes courants

## Partager des formulaires web pour la collecte de données

Une fois votre projet prêt pour la collecte de données, vous pouvez facilement partager un lien avec les répondants ou les enquêteurs pour la saisie des données.

Pour partager un lien avec des répondants :

1. Ouvrez la page **FORMULAIRE** et assurez-vous que votre formulaire a été [déployé](https://support.kobotoolbox.org/fr/deploy_form_new_project.html).
2. Dans la section **Collection de données**, cliquez sur **COPIER** pour copier le lien et le partager avec les enquêteurs ou les répondants.
3. Vous pouvez également cliquer sur **OUVRIR** pour lancer le formulaire dans un nouvel onglet du navigateur.

![Ouvrir ou copier un formulaire](images/data_through_webforms/copy_open.png)

### Exigence d'authentification

Par défaut, les projets déployés [exigent que les utilisateurs se connectent](https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication) avant de pouvoir ouvrir un formulaire web ou soumettre des données.

- Pour maintenir l'authentification obligatoire, partagez le projet avec des utilisateurs KoboToolbox spécifiques et accordez-leur la permission **Ajouter des soumissions**.
- Pour permettre à toute personne disposant du lien de soumettre des données sans nom d'utilisateur ni mot de passe, vous pouvez désactiver l'exigence d'authentification dans la section **Collection de données** en activant l'option « Autoriser les soumissions sans nom d'utilisateur ni mot de passe pour ce formulaire ».

<p class="note">
Pour en savoir plus sur les droits d'accès au partage de formulaires, consultez les articles <a href="https://support.kobotoolbox.org/fr/project_sharing_settings.html">Droits d'accès au niveau du projet</a> et <a href="https://support.kobotoolbox.org/fr/managing_permissions.html">Droits d'accès au niveau de l'utilisateur</a>.
</p>

### Modes de collecte de données

KoboToolbox propose plusieurs options de liens de formulaires web dans la section **Collection de données**. Ces options affectent le lien que vous ouvrez ou partagez, mais ne modifient pas le formulaire lui-même.

![Sélectionner le mode de collecte de données](images/data_through_webforms/modes.png)

Les modes de formulaires web disponibles sont les suivants :

| Mode de collecte de données | Description |
|:---|:---|
| Online-Offline (soumissions multiples) | Permet la collecte de données en ligne ou hors ligne et prend en charge plusieurs soumissions depuis le même appareil. |
| En ligne seulement (soumissions multiples) | Prend en charge plusieurs soumissions depuis le même appareil, mais nécessite une connexion internet. |
| En ligne seulement (une soumission) | Permet une soumission à la fois depuis le même appareil et peut être utilisé avec un <a href="https://support.kobotoolbox.org/fr/data_through_webforms.html#redirecting-users-to-another-webpage-after-submission">lien de redirection</a> après la soumission. Les utilisateurs ne sont pas empêchés de rouvrir le lien pour soumettre à nouveau des données. |
| En ligne uniquement (une soumission autorisée par répondant) | Empêche le même utilisateur sur le même navigateur et le même appareil de soumettre plus d'une fois. |
| Code de formulaire web | Fournit un code HTML pour intégrer le formulaire sur votre propre site web. |
| Afficher seulement | Ouvre le formulaire pour la prévisualisation et les tests sans autoriser les soumissions. |

### Imprimer un formulaire web

Vous pouvez également **imprimer un formulaire web** pour le partager lors du développement du formulaire ou l'utiliser pour la collecte de données sur papier. Pour ce faire :

1. Ouvrez votre formulaire web.
2. Cliquez sur le bouton d'impression en haut à droite.

La version imprimée inclut toutes les questions et les instructions supplémentaires (guidance hints), quelle que soit la logique de formulaire configurée.

![Cliquer sur l'icône d'impression pour imprimer le formulaire](images/data_through_webforms/print.png)

## Collecter des données avec des formulaires web

Après avoir ouvert le formulaire, les utilisateurs peuvent le remplir directement dans leur navigateur. Si le formulaire comprend [plusieurs langues](https://support.kobotoolbox.org/fr/collecting_data_multiple_languages.html), les utilisateurs peuvent changer la langue en haut du formulaire.

![Changer la langue du formulaire](images/data_through_webforms/change_language.png)

À la fin du formulaire, les utilisateurs peuvent soit enregistrer leur travail comme brouillon, soit le soumettre :

- **Envoyer** finalise la soumission et l'envoie au serveur lorsqu'une connexion est disponible. Une fois soumise, la saisie ne peut plus être modifiée dans le navigateur.
- **Sauvegarder le brouillon** stocke la soumission sur l'appareil afin qu'elle puisse être rouverte et complétée ultérieurement.

![Enregistrer ou soumettre un formulaire](images/data_through_webforms/save_submit.png)

### Gérer les brouillons

Enregistrer un brouillon stocke la soumission dans le navigateur afin qu'elle puisse être rouverte et complétée ultérieurement. Les brouillons ne sont pas envoyés au serveur KoboToolbox tant qu'ils ne sont pas rouverts, finalisés et soumis.

Lorsque vous enregistrez un formulaire comme brouillon, il vous sera demandé de lui donner un **nom** pour le retrouver plus facilement.

Le **compteur de file d'attente** en haut à gauche indique le nombre de brouillons enregistrés dans le navigateur. Pour rouvrir un brouillon :

1. Cliquez sur le **compteur de file d'attente** pour ouvrir la liste des brouillons enregistrés.
2. Sélectionnez le brouillon que vous souhaitez ouvrir.
3. Vérifiez ou modifiez le brouillon, puis soumettez-le.

![Icône du compteur de file d'attente](images/data_through_webforms/queue.png)

<p class="note">
<strong>Note :</strong>
Les brouillons sont stockés dans le navigateur jusqu'à leur soumission, même si vous fermez le navigateur, éteignez l'appareil ou vous déconnectez d'internet. Ne videz pas le cache de votre navigateur ni les données du site pendant la collecte de données, et assurez-vous que l'appareil n'est pas configuré pour les effacer automatiquement, car cela pourrait supprimer définitivement les brouillons enregistrés.
</p>

### Collecte de données hors ligne

Les formulaires web **permettent la collecte de données hors ligne** sur tous les navigateurs et appareils couramment utilisés. Lors de l'utilisation de formulaires web, KoboToolbox peut stocker le formulaire et les réponses dans le navigateur afin que les utilisateurs puissent continuer à saisir des données sans connexion internet.

<p class="note">
<strong>Note :</strong>
Lors de la saisie de données hors ligne, ne videz pas le cache de votre navigateur ni les données du site pendant la collecte de données, et assurez-vous que l'appareil n'est pas configuré pour les effacer automatiquement, car cela pourrait supprimer définitivement les formulaires hors ligne et les soumissions en file d'attente.
</p>

Pour collecter des données hors ligne avec des formulaires web :

1. Avant de vous déconnecter d'internet, ouvrez le formulaire en étant connecté et attendez qu'il soit entièrement chargé et mis en cache sur l'appareil. Cela peut prendre jusqu'à 30 secondes.
2. Une fois le formulaire mis en cache, une **icône de confirmation** apparaît en haut à gauche pour indiquer qu'il peut désormais être utilisé hors ligne.
    - Si vous vous déconnectez d'internet avant que le formulaire ait été mis en cache, vous risquez de perdre l'accès à la page lors de son actualisation.

    ![Icône de barres de signal](images/data_through_webforms/signal_bars.png)
3. Lors de la soumission de données hors ligne, les soumissions sont ajoutées à la file d'attente. Le **compteur de file d'attente** indique le nombre de saisies en attente d'envoi.

![Icône du compteur de file d'attente](images/data_through_webforms/queue.png)

4. Cliquez sur le **compteur de file d'attente** pour afficher les soumissions finalisées en attente d'envoi lorsqu'une connexion internet sera disponible. Vous pouvez également exporter les soumissions en file d'attente sous forme de fichier ZIP.
5. Une fois l'appareil reconnecté, les soumissions enregistrées sont envoyées automatiquement en arrière-plan pendant que le formulaire reste ouvert.

<p class="note">
<strong>Note :</strong>
Pour un accès plus facile pendant la collecte de données hors ligne, vous pouvez mettre le formulaire en favori ou ajouter un raccourci sur l'écran d'accueil de votre téléphone via l'option <strong>Ajouter à l'écran d'accueil</strong> dans le menu de votre navigateur.
</p>

## Personnaliser les liens de formulaires web

Vous pouvez modifier un lien de formulaire web pour contrôler la façon dont le formulaire s'ouvre ou se comporte pour différents utilisateurs et cas d'utilisation. Par exemple, vous pouvez ouvrir le formulaire dans une langue spécifique, préremplir certaines valeurs ou rediriger les utilisateurs vers une autre page après la soumission du formulaire.

### Ouvrir le formulaire dans une langue spécifique

Si votre formulaire est disponible en plusieurs langues, vous pouvez ajouter un paramètre de langue à l'URL du formulaire web afin qu'il s'ouvre dans une langue spécifique. Cela peut être utile lorsque vous partagez différents liens avec différents groupes d'utilisateurs.

Pour partager un lien qui ouvre le formulaire dans une langue différente de la langue par défaut :

1. Copiez votre lien de formulaire dans **FORMULAIRE > Collection de données**.
2. Ajoutez `?lang=code_langue` à la fin de l'URL, où `code_langue` est le code de la langue sélectionnée.
    - Par exemple : `https://ee.kobotoolbox.org/x/[form_id]?lang=fr`.

<p class="note">
Pour plus d'informations, consultez l'article <a href="https://support.kobotoolbox.org/fr/collecting_data_multiple_languages.html#language-specific-form-url">Collecter des données dans plusieurs langues</a>.
</p>

### Préremplir un champ depuis le lien web

Vous pouvez également préremplir un champ de votre formulaire via le lien web. Cela est utile lorsque vous souhaitez transmettre automatiquement une valeur connue dans le formulaire.

Par exemple, vous pourriez partager différents liens à différents endroits, et chaque lien pourrait ouvrir le même formulaire avec un champ caché indiquant la provenance du lien. Vous pourriez également partager un lien différent avec chaque répondant, avec l'identifiant unique de cette personne déjà intégré dans le lien.

Pour partager un lien qui préremplie un champ de votre formulaire :

1. Ajoutez la question que vous souhaitez préremplir à votre formulaire, puis définissez son [nom du champ](https://support.kobotoolbox.org/fr/glossary.html#data-column-name).
    - Il peut s'agir d'une question de type [Caché](https://support.kobotoolbox.org/fr/form_logic.html#storing-constants-in-your-form) si vous souhaitez stocker la valeur en arrière-plan, ou de tout type de question standard si vous souhaitez que les répondants la voient dans le formulaire.
2. Copiez votre lien de formulaire dans **FORMULAIRE > Collection de données**.
3. Ajoutez `?d[nom_du_champ]=valeur` à la fin de l'URL, où `nom_du_champ` est le nom du champ de la question Caché et `valeur` est la valeur préremplie.
    - Par exemple : `https://ee.kobotoolbox.org/x/[form_id]?d[champ_prerempli]=12345`.

<p class="note">
<strong>Note :</strong>
Utilisez le nom du champ complet dans le paramètre d'URL. Si la question se trouve dans un ou plusieurs groupes, le nom doit également inclure le ou les <strong>noms de groupe</strong> (par exemple, <code>groupe1/question1</code>). Vous pouvez trouver le nom exact dans le champ <a href="https://support.kobotoolbox.org/fr/question_options.html#data-column-name">Nom du champ</a> de la question dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, ou dans la colonne <code>name</code> d'un XLSForm.
</p>

### Rediriger les utilisateurs vers une autre page web après la soumission

Lorsque vous utilisez le mode de collecte de données **En ligne seulement (une soumission)**, vous pouvez rediriger les utilisateurs vers une autre page web après la soumission de leur formulaire.

Pour rediriger les utilisateurs vers une autre page web :

1. Dans **FORMULAIRE > Collection de données**, sélectionnez le mode de collecte de données **En ligne seulement (une soumission)**.
2. Copiez votre lien de formulaire.
3. Ajoutez `?return_url=page_web` à la fin de l'URL, où `page_web` est l'URL de la page web.
    - Par exemple : `https://ee.kobotoolbox.org/x/[form_id]?return_url=https://website.com`.

<p class="note">
<strong>Note :</strong>
Vous pouvez combiner plusieurs paramètres dans le même lien en les séparant par <code>&</code>.
</p>

## Résolution de problèmes

<details>
<summary><strong>Le formulaire ne fonctionne pas hors ligne</strong></summary>
Avant de vous déconnecter d'internet, assurez-vous que le formulaire a été entièrement ouvert et mis en cache dans le navigateur. Vérifiez l'indicateur de disponibilité hors ligne dans le formulaire avant de commencer la collecte de données sans connexion internet.

![Icône de barres de signal](images/data_through_webforms/signal_bars.png)
</details>

<br>

<details>
<summary><strong>Le navigateur plante pendant la collecte de données</strong></summary>
Si votre appareil redémarre, que le navigateur s'actualise ou que le formulaire se ferme pendant que vous êtes en train de saisir des données, vos réponses sont généralement sauvegardées dans le navigateur. Lorsque vous rouvrez le formulaire, KoboToolbox vous proposera soit d'ignorer les données précédemment saisies, soit de les recharger dans le formulaire pour continuer.
</details>

<br>

<details>
<summary><strong>Les soumissions n'arrivent pas au serveur</strong></summary>
Si le formulaire a été utilisé hors ligne, les soumissions sont peut-être encore en attente dans la file d'attente. Vérifiez le compteur de file d'attente et assurez-vous que l'appareil s'est reconnecté à internet. Les formulaires web envoient automatiquement les soumissions en file d'attente lorsqu'une connexion est disponible.

![Icône du compteur de file d'attente](images/data_through_webforms/queue.png)
</details>

<br>

<details>
<summary><strong>Les répondants sont invités à se connecter</strong></summary>
Vérifiez si le projet est configuré pour <a href="https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication">exiger une authentification</a> pour les soumissions. Si c'est le cas, les utilisateurs doivent se connecter avec un compte disposant de la permission d'ajouter des soumissions, ou vous pouvez désactiver cette exigence dans <strong>FORMULAIRE > Collection de données</strong>.
</details>

<br>

<details>
<summary><strong>Changer de compte dans les formulaires web</strong></summary>
Si <a href="https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication">l'authentification est requise</a> pour les soumissions, les formulaires web peuvent vous maintenir connecté avec le compte précédemment utilisé pour les formulaires web dans ce navigateur. Cela peut prêter à confusion si le formulaire est partagé avec un compte différent ou si vous devez soumettre en tant qu'un autre utilisateur.<br><br>Pour changer de compte, cliquez sur <strong>se déconnecter</strong> sous le bouton <strong>Envoyer</strong> dans le formulaire web. Fermez ensuite le formulaire web et rouvrez-le. Vous serez alors invité à vous connecter avec l'autre compte.<br><br>Notez que la connexion au formulaire web est distincte du compte auquel vous êtes connecté sur KoboToolbox dans le même navigateur. Si vous n'êtes pas sûr du compte avec lequel vous êtes actuellement connecté depuis l'interface du formulaire web, nous vous recommandons de vous déconnecter et de vous reconnecter.
</details>

<br>

<details>
<summary><strong>Des données semblent manquantes</strong></summary>
Ne videz pas le cache du navigateur ni ne supprimez les données du navigateur pendant la collecte de données avec des formulaires web. Vider le cache <strong>supprime les formulaires stockés, les brouillons et les soumissions en file d'attente de l'appareil</strong>, et ces données ne peuvent pas être récupérées si elles n'ont pas déjà été envoyées au serveur KoboToolbox.
</details>

<br>

<details>
<summary><strong>Navigateur non compatible</strong></summary>
Utilisez la dernière version d'un navigateur moderne. Chrome est généralement recommandé pour travailler avec des formulaires web, mais Safari, Firefox, Edge, Opera, Samsung Internet et d'autres navigateurs fonctionnent également bien. Internet Explorer n'est pas compatible.
</details>

<br>

<details>
<summary><strong>La soumission du formulaire web échoue</strong></summary>
Si la soumission d'un formulaire web échoue, vérifiez si votre formulaire utilise un <strong>terme réservé XLSForm</strong> comme <a href="https://support.kobotoolbox.org/fr/glossary.html#data-column-name">nom du champ</a>. Les termes réservés sont des termes qui ne peuvent pas être utilisés comme noms de variables car ils sont utilisés par le moteur XForms sous-jacent pour la structure, la logique ou l'analyse des données (par exemple, type, label, start, today). L'utilisation de ces termes peut entraîner des erreurs de validation de formulaire, des échecs de publication ou des problèmes d'export de données.<br><br>

Pour résoudre le problème, renommez la question concernée avec une valeur différente, puis redéployez le formulaire. Ce problème affecte généralement les formulaires web même lorsque le formulaire s'ouvre normalement, tandis que KoboCollect peut continuer à fonctionner normalement. Notez que les soumissions déjà enregistrées avec l'ancienne version du formulaire peuvent rester non soumettables. Il est donc important de mettre à jour le formulaire dès que possible si vous collectez des données via des formulaires web. <strong>Testez toujours la soumission du formulaire avant de lancer la collecte de données</strong> afin de détecter les problèmes de nommage le plus tôt possible.
</details>