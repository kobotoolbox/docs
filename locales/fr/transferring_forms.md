# Transférer manuellement des formulaires et des données d'un appareil Android à un autre
<a href="../transferring_forms.html">Read in English</a> | <a href="../es/transferring_forms.html">Leer en español</a> | <a href="../ar/transferring_forms.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/7def5f54e2441b05b4a2163e682bdd146fa781e1/source/transferring_forms.md" class="reference">24 Sep 2025</a>

Il peut arriver que vous soyez sur le terrain sans connexion Internet, mais que vous ayez quand même besoin d'importer la dernière version des formulaires (c'est-à-dire les derniers formulaires déployés sur le serveur) sur votre appareil. Il se peut également que vous ne puissiez pas importer les soumissions de formulaires sur le serveur en raison d'un écran cassé. Dans les deux scénarios, vous devrez transférer manuellement les formulaires et/ou les soumissions en utilisant un autre appareil. Cet article d'assistance vous montrera comment procéder.

Vous aurez besoin des éléments suivants pour suivre les instructions décrites ci-dessous :

-   Un appareil Android équipé de [l'application Android KoboCollect](kobocollect_on_android_latest.md) avec la dernière version du formulaire déployé. (Il est recommandé d'[obtenir la dernière version](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html#downloading-forms) du formulaire déployé sur l'appareil en cliquant sur **Télécharger formulaire** depuis votre **application Android KoboCollect**.)
-   Un appareil Android qui n'a pas la dernière version du formulaire (ou même aucun formulaire du tout).
-   Les deux appareils Android doivent avoir l'application Android KoboCollect déjà installée.
-   Un ordinateur personnel (de bureau ou portable).
-   Un câble USB qui connecte l'appareil et l'ordinateur personnel.

**Étape 1 :** Ouvrez votre ordinateur personnel (aucune connexion Internet n'est nécessaire ici). Un PC est nécessaire à cette étape pour copier les formulaires et les données d'un appareil Android avec la dernière version du formulaire vers un autre.

**Étape 2 :** Maintenant, connectez l'appareil Android (avec le dernier formulaire et les données que vous souhaitez transférer) au PC à l'aide du câble USB.

**Étape 3 :** Ensuite, suivez le chemin illustré ci-dessous pour extraire les dossiers requis contenant les formulaires et les données (selon la version de l'application installée) :

<p class="note">
  Dans cet exemple, nous connectons un Galaxy S10+ (un appareil Android) à Windows 11, c'est pourquoi vous voyez <strong>Ce PC</strong> et <strong>Galaxy S10+</strong>. Ceux-ci peuvent différer si vous utilisez un autre système d'exploitation et un autre appareil Android.
</p>

-   Pour l'application Android KoboCollect version 2021.2 et supérieure :
    -   Si l'application Android KoboCollect est installée dans la mémoire du téléphone :
        `Ce PC\Galaxy S10+\Phone\Android\data\org.koboc.collect.android\files\projects`
    -   Si l'application Android KoboCollect est installée dans la mémoire externe :
        `Ce PC\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files\projects`
-   Pour l'application Android KoboCollect (version supérieure à v1.26.0) :
    -   Si l'application Android KoboCollect est installée dans la mémoire du téléphone :
        `Ce PC\Galaxy S10+\Phone\Android\data\org.koboc.collect.android\files`
    -   Si l'application Android KoboCollect est installée dans la mémoire externe :
        `Ce PC\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files`
-   Pour l'application Android KoboCollect (version inférieure à v1.26.0) :
    -   Si l'application Android KoboCollect est installée dans la mémoire du téléphone :
        `Ce PC\Galaxy S10+\Phone\odk`
    -   Si l'application Android KoboCollect est installée dans la mémoire externe :
        `Ce PC\Galaxy S10+\sdcard\odk`

**Étape 4 :** Une fois que vous êtes dans le dossier **projects**, le dossier **files** ou le dossier **odk** _(selon la version de l'application Android KoboCollect que vous utilisez)_, vous devriez voir un dossier avec un nom similaire (comme indiqué ci-dessous) :

![Exemple d'image](images/transferring_forms/sample_1_folder.png)

**Étape 5 :** Entrez dans ce dossier et **COPIEZ** tous les éléments (comme indiqué dans l'image ci-dessous) :

![Exemple d'image des sous-dossiers](images/transferring_forms/sub_folders.png)

**Étape 6 :** Maintenant, connectez l'autre appareil Android sur lequel vous souhaitez copier les données au PC à l'aide du câble USB.

**Étape 7 :** Une fois de plus, suivez le chemin illustré ci-dessous (selon la version de l'application installée) :

-   Pour l'application Android KoboCollect version 2021.2 et supérieure :
    -   Si l'application Android KoboCollect est installée dans la mémoire du téléphone :
        `Ce PC\Galaxy S10+\Phone\Android\data\org.koboc.collect.android\files\projects`
    -   Si l'application Android KoboCollect est installée dans la mémoire externe :
        `Ce PC\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files\projects`
-   Pour l'application Android KoboCollect (version supérieure à v1.26.0) :
    -   Si l'application Android KoboCollect est installée dans la mémoire du téléphone :
        `Ce PC\Galaxy S10+\Phone\Android\data\org.koboc.collect.android\files`
    -   Si l'application Android KoboCollect est installée dans la mémoire externe :
        `Ce PC\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files`
-   Pour l'application Android KoboCollect (version inférieure à v1.26.0) :
    -   Si l'application Android KoboCollect est installée dans la mémoire du téléphone :
        `Ce PC\Galaxy S10+\Phone\odk`
    -   Si l'application Android KoboCollect est installée dans la mémoire externe :
        `Ce PC\Galaxy S10+\sdcard\odk`

**Étape 8 :** Une fois que vous êtes dans le dossier **projects**, le dossier **files** ou le dossier **odk** _(selon la version de l'application Android KoboCollect que vous utilisez)_, vous devriez voir un dossier avec un nom similaire (comme indiqué ci-dessous) :

![Exemple d'image](images/transferring_forms/sample_2_folder.png)

**Étape 9 :** Entrez dans ce dossier et **COLLEZ** les éléments copiés :

![Exemple d'image des sous-dossiers](images/transferring_forms/sub_folders.png)

Une fois cette opération terminée, ouvrez l'**application Android KoboCollect** depuis l'appareil (où vous avez collé les formulaires et les données). Vous pouvez maintenant utiliser cet appareil pour continuer la collecte de données et importer les soumissions sur le serveur.

<p class="note">
  Si les formulaires et les données ne sont pas visibles, vous pouvez essayer de redémarrer votre appareil. Cela pourrait rendre les formulaires et les données visibles dans l'application.
</p>

## Dépannage :

-   Lors de la connexion de l'appareil Android d'origine avec le formulaire et les données que vous souhaitez copier sur le PC, vous pouvez parfois voir non pas un seul dossier, mais plusieurs dossiers (comme indiqué dans l'image ci-dessous) :
    ![Exemple d'image de plusieurs dossiers](images/transferring_forms/sample_many_folders.png)
    Cela est déroutant et rend difficile la sélection du projet correct que vous souhaitez copier. Bien que cela prenne du temps, vous devrez parcourir tous les dossiers pour identifier le dossier correct contenant le projet que vous recherchez. Vous pouvez également supprimer tous les autres dossiers qui ne sont plus nécessaires. Par exemple, si un projet a été supprimé de l'application, il peut toujours apparaître comme un dossier lorsque l'appareil est accessible via l'ordinateur. Si vous êtes sûr qu'un projet n'est plus pertinent, la suppression du dossier le supprimera complètement.

-   De même, lors de la connexion du téléphone mobile Android sans la dernière version du formulaire (ou même sans aucun formulaire du tout) au PC, vous verrez parfois non pas un seul dossier mais plusieurs dossiers (comme indiqué dans l'image ci-dessous) :
    ![Exemple d'image de plusieurs dossiers](images/transferring_forms/sample_many_folders.png)
    _Si l'appareil a déjà une ancienne version du formulaire :_ Vous devrez identifier le dossier correct qui contient le projet que vous recherchez. Après avoir identifié le dossier correct, vous devez coller tous les sous-dossiers que vous avez copiés ici.

    _Si l'appareil n'a aucune version du formulaire du tout :_ Si votre appareil n'a aucune version du formulaire, mais que vous voyez toujours plusieurs dossiers, cela pourrait provenir de projets précédents qui ont été supprimés auparavant dans l'application. Comme décrit précédemment, la suppression d'un projet de l'application ne supprime pas nécessairement ces dossiers. Vous pouvez supprimer tous les dossiers inutiles pour libérer de l'espace. Actualisez votre affichage en quittant le dossier et en y retournant (c'est-à-dire le dossier projects, ou le dossier files, ou le dossier odk selon la version de l'application Android KoboCollect que vous utilisez). Vous devriez maintenant voir un seul dossier. Une fois que vous avez cliqué sur ce dossier, vous pouvez maintenant coller tous les sous-dossiers que vous avez copiés précédemment (c'est-à-dire forms, instances, etc.).

    _Si l'application Android KoboCollect est fraîchement installée sur l'appareil :_ Si vous avez fraîchement installé l'application Android KoboCollect sur votre appareil, vous ne verrez peut-être aucun dossier sans avoir d'abord configuré les paramètres du serveur, comme indiqué dans l'article d'assistance [Collecte de données sur l'application Android KoboCollect](kobocollect_on_android_latest).

-   Si vous avez copié les formulaires et les données d'un appareil Android à un autre et que vous êtes prêt à soumettre les soumissions de l'appareil au serveur, mais que vous avez toujours des problèmes pour les soumettre, vous pouvez vous référer aux suggestions de configuration du serveur qui ont été décrites dans l'article d'assistance [« Collecte de données sur l'application Android KoboCollect »](kobocollect_on_android_latest).