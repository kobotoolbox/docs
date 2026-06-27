# Gérer les réponses média soumises par les répondants
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/b0d195136b7fb3fe51b687cc03a5e8dcde946309/source/managing_media_responses.md" class="reference">22 Jun 2026</a>

Les fichiers multimédias collectés auprès des répondants contiennent souvent des informations contextuelles importantes, telles que des photos, des enregistrements ou des documents qui viennent enrichir les données d'enquête. Une fois la collecte de données commencée, **ces fichiers font partie des données de votre projet** et doivent être gérés avec soin.

Cet article explique comment visualiser, télécharger et supprimer les fichiers multimédias soumis par les répondants, notamment les images, les enregistrements audio, les vidéos et autres types de fichiers.

## Visualiser les fichiers multimédias

Tous les fichiers multimédias soumis par les répondants peuvent être visualisés depuis le tableau de données de votre projet. Pour ouvrir les fichiers multimédias dans des soumissions individuelles :

1. Ouvrez votre projet et accédez à la page **DONNÉES**.
2. Dans le tableau de données, localisez la cellule contenant le fichier.
3. Cliquez sur l'icône <i class="k-icon-qt-photo"></i> **image**, <i class="k-icon-qt-video"></i> **vidéo** ou <i class="k-icon-qt-file"></i> **fichier**. Pour les enregistrements audio, cliquez sur **Open**. <i class="k-icon-arrow-up-right"></i>

![Vue galerie pour les images](images/managing_media_responses/table.png)

Les images peuvent également être visualisées dans le mode **Galerie Photo** de votre projet. Pour afficher toutes les images collectées dans un seul projet :

1. Ouvrez votre projet et accédez à la page **DONNÉES**.
2. Ouvrez l'onglet <i class="k-icon-file-image"></i> **Galerie Photo** depuis le menu de gauche.
3. Le mode **Galerie Photo** affiche toutes les images collectées dans le projet. Vous pouvez filtrer les images par question ou par plage de dates.

## Télécharger les fichiers multimédias

Vous pouvez télécharger les fichiers multimédias individuellement depuis le tableau de données, ou en masse depuis la page **Téléchargements**.

### Télécharger des fichiers multimédias individuels

Pour télécharger un seul fichier :

1. Accédez à la page **DONNÉES**.
2. Dans le tableau de données, localisez la cellule contenant le fichier.
3. Cliquez sur l'icône <i class="k-icon-qt-photo"></i> **image**, <i class="k-icon-qt-video"></i> **vidéo** ou <i class="k-icon-qt-file"></i> **fichier**. Pour les enregistrements audio, cliquez sur **Open.** <i class="k-icon-arrow-up-right"></i>
4. Cliquez sur les <i class="k-icon k-icon-more"></i> trois points en haut de l'aperçu.
5. Cliquez sur <i class="k-icon-download"></i> **Télécharger**.

![Télécharger un fichier multimédia](images/managing_media_responses/download.png)

### Télécharger des fichiers multimédias en masse

Pour télécharger des fichiers multimédias en masse :

1. Accédez à la page **DONNÉES**.
2. Ouvrez l'onglet <i class="k-icon-download"></i> **Téléchargements** depuis le menu de gauche.
3. Sous **Sélectionner le type d'exportation**, choisissez **Fichier média (ZIP)**.
4. Cliquez sur **Nouvel export** et attendez que l'exportation soit terminée.
5. Téléchargez le fichier `.zip` généré depuis le tableau.

Dans le dossier téléchargé, les pièces jointes sont regroupées par soumission. Chaque nom de dossier correspond au `_uuid` de la soumission, qui apparaît également comme colonne dans la base de données.

<p class="note">
<strong>Remarque :</strong> Les exports multimédias n'incluent que les questions présentes dans la version la plus récente du formulaire.
</p>

Lorsque vous exportez vos données au format CSV ou XLS, le fichier exporté inclut également des hyperliens permettant d'ouvrir les fichiers multimédias associés dans un navigateur web, à condition que l'option par défaut **Inclure les URL des médias** soit sélectionnée.

<p class="note">
  Pour en savoir plus sur l'exportation de vos données, consultez l'article <a href="https://support.kobotoolbox.org/fr/export_download.html">Exporter et télécharger vos données</a>.
</p>

## Supprimer les fichiers multimédias

<iframe src="https://www.youtube.com/embed/J0-mh1R6dEs?si=9t0JFhEVdVcf21lk&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Il peut être nécessaire de supprimer des fichiers multimédias de votre projet KoboToolbox pour diverses raisons, notamment pour préserver la confidentialité, gérer l'espace de stockage ou corriger des erreurs de soumission. Vous pouvez supprimer des fichiers multimédias individuellement ou en masse.

### Supprimer des fichiers multimédias individuels

Il existe deux façons de supprimer des fichiers multimédias individuels : directement depuis le tableau de données ou en ouvrant la soumission. Une fois un fichier supprimé, il est marqué comme _Supprimé_ dans le tableau de données et ne peut pas être récupéré.

**Supprimer des fichiers multimédias individuels depuis le tableau de données**

Vous pouvez supprimer des images, vidéos et fichiers individuels directement depuis le tableau de données en suivant les étapes ci-dessous :

1. Dans le tableau de données, localisez la cellule contenant le fichier multimédia que vous souhaitez supprimer.
2. Cliquez sur l'icône <i class="k-icon k-icon-qt-photo"></i> **image**, <i class="k-icon k-icon-qt-video"></i> **vidéo** ou <i class="k-icon k-icon-qt-file"></i> **fichier**.
3. Cliquez sur les <i class="k-icon k-icon-more"></i> **trois points** en haut de l'aperçu du fichier.
4. Cliquez sur <i class="k-icon k-icon-trash"></i> **Supprimer**, puis à nouveau sur **Supprimer** pour confirmer.

![Supprimer un fichier multimédia depuis le tableau](images/managing_media_responses/delete_from_table.png)

**Supprimer des fichiers multimédias individuels depuis la vue de soumission**

Vous pouvez également supprimer des fichiers multimédias en ouvrant la vue de soumission :

1. Dans le tableau de données, localisez la soumission contenant les fichiers multimédias que vous souhaitez supprimer.
2. Sur le côté gauche de la soumission, cliquez sur <i class="k-icon k-icon-view"></i> **Open**.
3. Faites défiler jusqu'au fichier multimédia que vous souhaitez supprimer.
4. Cliquez sur les <i class="k-icon k-icon-more"></i> **trois points** à droite du fichier multimédia.
5. Cliquez sur <i class="k-icon k-icon-trash"></i> **Supprimer**, puis à nouveau sur **Supprimer** pour confirmer.

![Ouvrir la vue de soumission](images/managing_media_responses/open_submission_view.png)

**Supprimer des fichiers audio depuis la vue de question audio**

Vous pouvez supprimer des fichiers audio en ouvrant la vue de question audio pour la transcription, la traduction et l'analyse des questions audio :

1. Dans le tableau de données, cliquez sur **Open** <i class="k-icon k-icon-arrow-up-right"></i> pour ouvrir la vue de question audio.
2. Dans l'onglet **TRANSCRIPT**, **TRANSLATIONS** ou **ANALYSIS**, localisez le fichier audio en haut à droite.
3. Cliquez sur les <i class="k-icon k-icon-more"></i> **trois points** à droite du fichier audio.
4. Cliquez sur <i class="k-icon k-icon-trash"></i> **Supprimer**, puis à nouveau sur **Supprimer** pour confirmer.

![Supprimer un fichier audio](images/managing_media_responses/delete_audio.png)

### Supprimer des fichiers multimédias en masse

Il peut être nécessaire de supprimer des fichiers multimédias en masse, par exemple pour gérer l'espace de stockage après leur exportation. Vous pouvez supprimer tous les fichiers multimédias des soumissions sélectionnées en suivant les étapes ci-dessous :

1. Sélectionnez les soumissions pour lesquelles vous souhaitez supprimer les fichiers multimédias.
2. Cliquez sur **Delete media files only** au-dessus du tableau de données.
   * Cette action ouvre une fenêtre modale indiquant le nombre et les types de fichiers multimédias qui seront supprimés pour cette sélection.
3. Cochez la case indiquant « You are about to permanently remove the following media files from the selected submissions: ».
   * Cette étape confirme que les fichiers seront supprimés définitivement et ne pourront pas être récupérés.
4. Cliquez sur **Supprimer**.

<p class="note">
  <strong>Remarque :</strong> Avec cette approche, tous les fichiers multimédias de chaque soumission sélectionnée seront supprimés ; il n'est actuellement pas possible de choisir uniquement les fichiers d'une question donnée.
</p>

![Suppression en masse de fichiers multimédias](images/managing_media_responses/bulk_delete.png)

## Résolution de problèmes

<details>
  <summary><strong>Le téléchargement Fichier média (ZIP) reste bloqué en attente</strong></summary>
  Si un export <strong>Fichier média (ZIP)</strong> reste à l'état <strong>Pending ... Click to refresh</strong> pendant une période prolongée, actualisez la page ou quittez la page <strong>Téléchargements</strong> puis revenez-y. N'appuyez pas plusieurs fois sur <strong>Click to refresh.</strong>
</details>

<br>

<details>
  <summary><strong>L'export ZIP des pièces jointes multimédias échoue</strong></summary>
Si votre projet contient de nombreux fichiers multimédias ou si votre connexion internet est lente, l'exportation de toutes les pièces jointes multimédias sous forme de fichier ZIP peut échouer ou prendre trop de temps. Deux alternatives sont disponibles : télécharger les fichiers multimédias à l'aide de l'extension <a href="https://www.downthemall.net">DownThemAll</a>, ou utiliser le script de téléchargement <a href="https://github.com/joshuaberetta/kobomedia">Kobo media</a> disponible sur GitHub.
<br> <br>
Pour télécharger des fichiers multimédias à l'aide de l'extension DownThemAll :
<ol>
  <li><a href="https://www.downthemall.net">Installez</a> l'extension DownThemAll dans Firefox, Chrome ou Edge.</li>
  <li><a href="https://support.kobotoolbox.org/fr/export_download.html">Exportez vos données</a> au format XLS. Veillez à <a href="https://support.kobotoolbox.org/fr/advanced_export.html#additional-data-format-options">inclure les URL des médias</a>.</li>
  <li>Ouvrez le fichier téléchargé dans Excel, puis cliquez sur <strong>Fichier > Enregistrer sous</strong> et choisissez <strong>Page Web (.htm ou .html)</strong> comme type de fichier.</li>
  <li>Ouvrez le fichier HTML enregistré dans Firefox, Chrome ou Edge, en étant connecté au compte KoboToolbox où les fichiers multimédias sont stockés.</li>
  <li>Ouvrez l'extension DownThemAll depuis la page HTML et lancez le téléchargement.</li>
</ol>

Vous pouvez ajuster les paramètres de l'extension pour limiter la vitesse de téléchargement ou relancer les téléchargements échoués. Cette méthode permet de télécharger tous les fichiers multimédias, ou uniquement des fichiers sélectionnés, sans dépendre de l'export ZIP.
</details>

<br>

<details>
  <summary><strong>Les URL des médias issues d'anciens exports ne fonctionnent plus</strong></summary>
Les utilisateurs qui s'appuient sur les URL des médias issues d'anciens exports Excel ou CSV peuvent constater que ces liens ne fonctionnent plus depuis la <a href="https://support.kobotoolbox.org/fr/migrating_api.html">dépréciation de l'API v1</a>.
<br><br>
Les URL concernées utilisent l'ancien format :
<code>https://kc.kobotoolbox.org/media/original?media_file=...</code>
<br><br>
Pour résoudre ce problème, réexportez vos données en sélectionnant l'option <strong>Inclure les URL des médias</strong>. Le nouvel export inclura des URL de médias mises à jour.
<br><br>
Les utilisateurs avancés peuvent également recréer l'export via les <a href="https://support.kobotoolbox.org/fr/synchronous_exports.html">exports synchronisés</a> ou reconstruire les URL manuellement en utilisant le format actuel de l'API v2 :
<code>https://kf.kobotoolbox.org/api/v2/assets/{asset_uid}/data/{submission_id}/attachments/{attachment_uid}/</code>
</details>