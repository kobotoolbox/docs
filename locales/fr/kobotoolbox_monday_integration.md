# Intégration de KoboToolbox avec monday.com
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/3d800e00d14000ecaa30ed97fcbf03a9feee65eb/source/kobotoolbox_monday_integration.md" class="reference">3 mai 2024</a>


<p class="note">
Cet article présente la version initiale de l'intégration entre KoboToolbox
et Monday.com. Comme pour toute nouvelle version, des bugs inattendus peuvent
survenir. Si vous rencontrez des problèmes, veuillez <a
href="https://www.kobotoolbox.org/contact/?contact_reason=Monday.com%20integration"
class="reference">nous contacter</a> immédiatement afin que nous puissions y remédier.
</br>
⚠️ Nous recommandons de procéder à des tests rigoureux avant de déployer cette intégration pour des projets critiques. ⚠️
</p>


L'intégration KoboToolbox permet aux utilisateurs de synchroniser facilement les données de leur projet KoboToolbox avec un tableau monday.com.

En quelques étapes seulement, vous pouvez configurer l'intégration pour copier automatiquement les soumissions reçues dans KoboToolbox vers n'importe lequel de vos tableaux monday.com. Cette intégration réduit considérablement le travail manuel de copier-coller des données de projet entre KoboToolbox et monday.com.

## Fonctionnalités

- Processus simplifié pour connecter des projets KoboToolbox à des tableaux monday.com.
- Mappage facile des champs monday.com aux questions KoboToolbox, dans n'importe quelle langue de libellé définie dans le formulaire.
- Synchronisation en temps réel des nouvelles soumissions pour créer de nouveaux éléments.

## Installation et première utilisation

### Avant d'installer l'intégration

1.  Créez un compte KoboToolbox si vous n'en avez pas encore. Pour en savoir plus, consultez l'article [Créer un compte KoboToolbox](creating_account.md).
2.  Préparez un tableau monday.com reflétant la structure de votre projet KoboToolbox, de sorte que tous les champs de votre projet KoboToolbox soient représentés sur le tableau monday.com.
3.  Lors de la configuration de l'intégration, vous devrez authentifier l'accès à votre compte en fournissant votre clé API KoboToolbox. Découvrez comment obtenir votre [clé API](api.md).

<p class="note">
  **Note :** La clé API est un identifiant unique utilisé pour l'authentification. Dans KoboToolbox, elle est désignée sous le nom de **clé API** (API Key). Dans monday.com, elle est désignée sous le nom de **jeton API** (API token).
</p>

### Installation

1.  Installez l'intégration KoboToolbox depuis le
    [marketplace d'applications monday.com](https://monday.com/marketplace).
2.  Une fois l'installation effectuée, accédez au tableau que vous avez préparé pour configurer l'intégration.

<p class="note">
    **Note 1 :** Une seule recette d'intégration KoboToolbox peut être établie par tableau monday.
    **Note 2 :** Seule la personne qui a installé la recette peut la modifier ; tous les autres membres du tableau ne peuvent l'ouvrir qu'en mode lecture seule.
</p>

### Première utilisation

1.  Accédez au menu **Integration** en haut à droite.
    ![monday-board-integrate](/images/kobotoolbox_monday_integration/monday-board-integrate.png)
2.  Recherchez **KoboToolbox** dans le Centre des intégrations.
    ![app-marketplace](/images/kobotoolbox_monday_integration/find-integration.png)
3.  Cliquez sur l'intégration KoboToolbox et choisissez la recette incluse.
    ![kobo-integration](/images/kobotoolbox_monday_integration/choose-recipe.png)
4.  Autorisez l'application KoboToolbox :
    - Saisissez l'URL du serveur KoboToolbox sur lequel vous avez créé votre compte. Pour le serveur KoboToolbox mondial, utilisez l'URL [https://kf.kobotoolbox.org](https://kf.kobotoolbox.org). Pour le serveur KoboToolbox Union européenne, utilisez l'URL [https://eu.kobotoolbox.org](https://eu.kobotoolbox.org).
    - Saisissez votre clé API KoboToolbox dans le champ « Kobo API token ».
    ![provide-api-key](/images/kobotoolbox_monday_integration/provide-api-key.png)

<p class="note">
    **Note :** Pour modifier la clé API après la configuration de la recette d'intégration, l'application d'intégration KoboToolbox doit être complètement réinstallée.
    </p>

5. Pour la configuration de la recette, définissez les paramètres suivants :
    - Choisissez dans le menu déroulant le projet KoboToolbox que vous souhaitez connecter à votre tableau monday.com. Seuls les projets déployés sont disponibles à la sélection.
    - Choisissez la langue des libellés dans le menu déroulant. Si votre formulaire contient plusieurs langues, sélectionnez la langue à utiliser pour mapper les questions aux colonnes. La langue sélectionnée s'affichera uniquement lors du mappage des questions KoboToolbox avec les colonnes monday.com. Les données affichées dans le tableau monday.com utiliseront toujours la structure de données XML sous-jacente plutôt que les libellés traduits des questions à choix unique ou à choix multiple.
    - Cliquez sur **Item** pour configurer le mappage des questions aux colonnes.
        ![dynamic-linking](/images/kobotoolbox_monday_integration/item-mapping.png)
6.  Une fois la configuration de la recette terminée, cliquez sur le bouton **Add to Board**.
    ![recipe](/images/kobotoolbox_monday_integration/recipe-config.png)
7.  Après avoir terminé la configuration de l'intégration, vous devez configurer les services REST sur KoboToolbox afin de synchroniser automatiquement les données de votre projet avec le tableau monday.com. Pour configurer les services REST sur KoboToolbox :
    - Copiez le lien d'intégration depuis la notification de configuration de l'intégration ou depuis la description de votre tableau monday.com.\
        ![webhook-url](/images/kobotoolbox_monday_integration/description-link.png)
    - Connectez-vous à votre compte KoboToolbox.
    - Accédez au projet que vous souhaitez connecter. Ouvrez l'onglet PARAMÈTRES, puis choisissez Services REST et cliquez sur le bouton **REGISTER A NEW SERVICE**.\
        ![create-rest-service](/images/kobotoolbox_monday_integration/create-rest-service.png)
    - Saisissez « monday.com integration » comme nom de service et entrez le lien d'intégration dans le champ « Endpoint URL ».
    - Dans la section « Custom HTTP Headers », insérez la valeur « webhook-auth » dans le champ « Name » et saisissez votre clé API KoboToolbox dans le champ « Value ».\
        ![rest-service-modal](/images/kobotoolbox_monday_integration/rest-service-modal.png)
    - Cliquez sur le bouton **SAVE**.
8.  Tout est prêt ! Chaque nouvelle soumission à votre projet KoboToolbox sera automatiquement ajoutée à votre tableau monday.com conformément à la configuration de votre recette.\

    ![kobo-monday-data](/images/kobotoolbox_monday_integration/kobo-monday-data.png)

    ### Remarques importantes
    1. Toute mise à jour apportée à un formulaire ou à une soumission individuelle dans un projet KoboToolbox déjà ajouté à votre tableau monday.com ne sera pas automatiquement répercutée sur ce tableau. Les modifications telles que la suppression ou le renommage d'une question, la modification d'une hiérarchie de groupes, la transformation d'un groupe en groupe répété, ou la modification des libellés dans le formulaire KoboToolbox n'affecteront pas les éléments de votre tableau monday.com.
    2. La localisation n'est pas automatiquement prise en charge dans le mappage dynamique des champs. Pour transférer une localisation ou des coordonnées de KoboToolbox vers une colonne monday.com :
      - Créez deux colonnes sur votre tableau monday.com pour accueillir les données de localisation : une colonne de type Texte et une colonne de type Localisation. Il est important de leur donner des noms identiques.
      - Dans le mappage dynamique des champs, mappez la localisation KoboToolbox vers la colonne de type Texte de monday.com. La colonne de type Localisation n'apparaîtra pas dans le mappage dynamique.
      - La soumission de localisation KoboToolbox sera automatiquement renseignée dans la colonne de type Localisation de monday.com.
    3. La colonne Fichier n'est pas automatiquement prise en charge dans le mappage dynamique des champs. Pour transférer des fichiers de KoboToolbox vers monday.com :
      - Ajoutez une colonne Fichier au tableau monday.com et donnez-lui le même nom que celui utilisé pour le champ Fichier dans votre projet KoboToolbox. Le même nom de colonne de fichier doit être utilisé dans monday.com et dans KoboToolbox.
      - Si vous n'avez pas encore installé la recette d'intégration, effectuez le processus d'installation. Une fois l'installation terminée, accédez au Centre des intégrations, ouvrez la recette existante et cliquez sur le bouton **Update automation** pour appliquer les dernières modifications fonctionnelles.
      - Aucune autre modification de configuration n'est nécessaire. Les fichiers seront désormais automatiquement transférés du projet KoboToolbox vers la colonne appropriée de votre tableau monday.com en fonction du nom de la colonne.
    4. Afin de garantir des performances optimales dans les tableaux monday.com, monday.com limite le nombre de colonnes par tableau : 200 colonnes pour les comptes non-entreprise et 300 colonnes pour les comptes entreprise.



## FAQ

**Que sont les services REST ?**

Des informations supplémentaires sur les services REST sont disponibles dans
[cet article d'aide](rest_services.md).

**Qu'est-ce que le mappage dynamique des champs ?**

Le mappage dynamique des champs est une association entre les champs représentés sur le tableau monday.com et les questions correspondantes du projet KoboToolbox.

**Que se passe-t-il si je modifie mes données dans mon compte KoboToolbox ?**

Toute mise à jour apportée à un formulaire ou à une soumission individuelle dans votre projet KoboToolbox déjà envoyé au tableau monday.com ne sera pas automatiquement synchronisée.

**Que se passe-t-il si je modifie mes données dans le tableau monday.com ?**

Les modifications apportées aux données représentées dans le tableau monday.com ne seront pas répercutées dans le projet KoboToolbox.

**Que se passe-t-il si je dois modifier la langue ultérieurement ?**

La sélection de la langue n'affecte que la vue de mappage dynamique des champs dans la configuration de la recette d'intégration. Les données du tableau ne seront pas traduites.

**Que se passe-t-il si je supprime le projet dans KoboToolbox ?**

Si un projet est supprimé dans KoboToolbox, l'intégration ne fonctionnera plus jusqu'à ce que la recette d'intégration soit mise à jour avec un nouveau projet.

**Que sont les « types de colonnes » ?**

Un « type de colonne » dans monday.com correspond à un type de question dans KoboToolbox.

**Quels types de questions KoboToolbox peuvent être transférés vers monday.com ?**

Tous les [types de questions](question_types.md) à l'exception de XML externe sont pris en charge par monday.com. Si vous ne trouvez pas le type de colonne approprié dans le tableau monday.com, utilisez une colonne de type Texte.

Pour transférer les types de questions [Position](gps_questions.md) et [Zone](gps_questions.md) de KoboToolbox vers la colonne de type Localisation du tableau monday.com, utilisez l'approche décrite dans la [Remarque importante n° 2](#remarques-importantes). Si le transfert des données vers la colonne Localisation n'est pas indispensable, une seule colonne de type Texte peut être utilisée sans configuration supplémentaire.

**Comment les questions à choix multiple de KoboToolbox sont-elles transférées vers monday.com ?**

Pour les questions [Choix multiple](select_one_and_select_many.md), une colonne de type Liste déroulante doit être utilisée dans le tableau monday.com afin que toutes les options sélectionnées soient correctement transférées vers le tableau.

**Comment les questions à choix unique de KoboToolbox sont-elles transférées vers monday.com ?**

Pour les questions [Choix unique](select_one_and_select_many.md), utilisez une colonne de type Statut (limitée à 40 options de libellés), Liste déroulante ou Texte afin que l'option sélectionnée soit correctement transférée vers le tableau.

**Puis-je synchroniser plusieurs projets KoboToolbox avec mon tableau monday ?**

Non. Une seule recette d'intégration KoboToolbox peut être établie par tableau. La présence de plusieurs recettes entraînera une erreur serveur.

**Pourquoi ne puis-je pas modifier une recette créée par un autre membre du tableau monday.com ?**

Seul le membre du tableau qui a créé la recette peut la modifier. Tous les autres membres du tableau ne peuvent l'ouvrir qu'en mode lecture seule.