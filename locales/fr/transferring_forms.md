# Importer des formulaires dans KoboCollect
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/7def5f54e2441b05b4a2163e682bdd146fa781e1/source/transferring_forms.md" class="reference">24 Sep 2025</a>


Il peut arriver que vous soyez sur le terrain sans connexion internet, mais que vous ayez tout de même besoin d'importer la dernière version de vos formulaires (c'est-à-dire les derniers formulaires déployés sur le serveur) sur votre appareil. Il se peut également que vous ne puissiez pas envoyer vos soumissions au serveur en raison d'un écran qui ne fonctionne plus. Dans ces deux situations, vous devrez transférer manuellement les formulaires et/ou les soumissions à l'aide d'un autre appareil. Cet article d'aide vous explique comment procéder.

Vous aurez besoin des éléments suivants pour suivre les instructions ci-dessous :

-   Un appareil Android sur lequel est installée [l'application KoboCollect](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html) avec la dernière version du formulaire déployé. (Il est recommandé de [télécharger la dernière version](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html#downloading-forms) du formulaire déployé sur l'appareil en appuyant sur **Download Form** dans **l'application Android KoboCollect**.)
-   Un appareil Android qui ne dispose pas de la dernière version du formulaire (ou qui n'en a aucune).
-   Les deux appareils Android doivent avoir l'application KoboCollect déjà installée.
-   Un ordinateur personnel (de bureau ou portable).
-   Un câble USB permettant de connecter l'appareil à l'ordinateur personnel.

**Étape 1 :** Allumez votre ordinateur personnel (aucune connexion internet n'est nécessaire à cette étape). Un ordinateur est indispensable à cette phase pour copier les formulaires et les données d'un appareil Android disposant de la dernière version du formulaire vers un autre.

**Étape 2 :** Connectez maintenant l'appareil Android (contenant le formulaire et les données les plus récents que vous souhaitez transférer) à l'ordinateur à l'aide du câble USB.

**Étape 3 :** Suivez ensuite le chemin illustré ci-dessous pour extraire les dossiers requis contenant les formulaires et les données (selon la version de l'application installée) :

<p class="note">
  Dans cet exemple, nous connectons un Galaxy S10+ (un appareil Android) à Windows 11, c'est pourquoi vous voyez <strong>Ce PC</strong> et <strong>Galaxy S10+</strong>. Ces éléments peuvent différer si vous utilisez un autre système d'exploitation ou un autre appareil Android.
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

**Étape 4 :** Une fois dans le dossier **projects**, le dossier **files** ou le dossier **odk** _(selon la version de l'application Android KoboCollect que vous utilisez)_, vous devriez voir un dossier portant un nom similaire (comme illustré ci-dessous) :

![Sample image](images/transferring_forms/sample_1_folder.png)

**Étape 5 :** Ouvrez ce dossier et **COPIEZ** tous les éléments qu'il contient (comme illustré ci-dessous) :

![Sample image of sub folders](images/transferring_forms/sub_folders.png)

**Étape 6 :** Connectez maintenant l'autre appareil Android sur lequel vous souhaitez copier les données à l'ordinateur à l'aide du câble USB.

**Étape 7 :** Suivez à nouveau le chemin illustré ci-dessous (selon la version de l'application installée) :

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

**Étape 8 :** Une fois dans le dossier **projects**, le dossier **files** ou le dossier **odk** _(selon la version de l'application Android KoboCollect que vous utilisez)_, vous devriez voir un dossier portant un nom similaire (comme illustré ci-dessous) :

![Sample image](images/transferring_forms/sample_2_folder.png)

**Étape 9 :** Ouvrez ce dossier et **COLLEZ** les éléments copiés :

![Sample image of sub folders](images/transferring_forms/sub_folders.png)

Une fois cette opération terminée, ouvrez **l'application Android KoboCollect** sur l'appareil (sur lequel vous avez collé les formulaires et les données). Vous pouvez maintenant utiliser cet appareil pour poursuivre la collecte de données et envoyer les soumissions au serveur.

<p class="note">
  Si les formulaires et les données ne sont pas visibles, vous pouvez essayer de redémarrer votre appareil. Cela peut rendre les formulaires et les données visibles dans l'application.
</p>

## Résolution de problèmes

-   Lorsque vous connectez l'appareil Android d'origine contenant les formulaires et les données que vous souhaitez copier à l'ordinateur, il peut arriver que vous voyiez non pas un seul dossier, mais plusieurs dossiers (comme illustré ci-dessous) :
    ![Sample image of many folders](images/transferring_forms/sample_many_folders.png)
    Cela peut prêter à confusion et rendre difficile la sélection du bon projet à copier. Bien que cela prenne du temps, vous devrez parcourir tous les dossiers pour identifier le bon dossier contenant le projet recherché. Vous pouvez également supprimer les dossiers dont vous n'avez plus besoin. Par exemple, si un projet a été supprimé de l'application, il peut encore apparaître sous forme de dossier lorsque l'appareil est accessible depuis l'ordinateur. Si vous êtes certain qu'un projet n'est plus utile, la suppression du dossier l'effacera définitivement.

-   De même, lorsque vous connectez l'appareil Android ne disposant pas de la dernière version du formulaire (ou n'en ayant aucune) à l'ordinateur, il peut arriver que vous voyiez non pas un seul dossier, mais plusieurs dossiers (comme illustré ci-dessous) :
    ![Sample image of many folders](images/transferring_forms/sample_many_folders.png)
    _Si l'appareil dispose déjà d'une version antérieure du formulaire :_ Vous devrez identifier le bon dossier contenant le projet recherché. Après avoir identifié le bon dossier, collez-y tous les sous-dossiers que vous avez copiés.

_Si l'appareil ne dispose d'aucune version du formulaire :_ Si votre appareil ne contient aucune version de formulaire, mais que vous voyez tout de même plusieurs dossiers, cela peut provenir de projets précédents qui ont été supprimés de l'application. Comme indiqué précédemment, la suppression d'un projet dans l'application ne supprime pas nécessairement ces dossiers. Vous pouvez supprimer tous les dossiers inutiles pour libérer de l'espace. Actualisez l'affichage en quittant le dossier et en y revenant (c'est-à-dire le dossier projects, le dossier files ou le dossier odk, selon la version de l'application Android KoboCollect que vous utilisez). Vous devriez maintenant voir un seul dossier. Une fois que vous avez ouvert ce dossier, vous pouvez coller tous les sous-dossiers que vous avez copiés précédemment (c'est-à-dire forms, instances, etc.).

    _Si l'application KoboCollect vient d'être installée sur l'appareil :_ Si vous venez d'installer l'application KoboCollect sur votre appareil, il se peut qu'aucun dossier n'apparaisse sans avoir d'abord configuré les paramètres du serveur, comme indiqué dans l'article d'aide [Configurer l'application KoboCollect](kobocollect_on_android_latest).

-   Si vous avez copié les formulaires et les données d'un appareil Android vers un autre et que vous êtes prêt à envoyer les soumissions depuis l'appareil vers le serveur, mais que vous rencontrez toujours des problèmes lors de l'envoi, vous pouvez consulter les suggestions de configuration du serveur présentées dans l'article d'aide [« Configurer l'application KoboCollect »](kobocollect_on_android_latest).