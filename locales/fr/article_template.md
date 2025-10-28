# Titre de l'article
<a href="../article_template.html">Read in English</a> | <a href="../es/article_template.html">Leer en español</a> | <a href="../ar/article_template.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/2afa3a0c670fe98b296a79b798f33abf248d0273/source/article_template.md" class="reference">6 Sep 2025</a>

C'est ici que se trouve votre introduction. Notez ci-dessus que le code « Dernière mise à jour » sera automatiquement mis à jour avec le nom et la date corrects de l'article lors de la publication, aucune modification manuelle n'est donc nécessaire. N'oubliez pas de nommer ce fichier en fonction du titre de l'article et de terminer le nom du fichier par `.md`.

Cet article comprend :

-   [Mise en forme du texte en markdown](#ceci-est-un-en-tete)
-   [Ajout de fichiers multimédias](#ajout-de-fichiers-multimedias)
-   [Ajout de tableaux](#ajout-de-tableaux)
-   [Mise en forme HTML](#mise-en-forme-html)
-   [Création d'une section de dépannage](#depannage)
-   [Liste des icônes](#liste-des-icones)

Pour obtenir de l'aide sur la mise en forme markdown ou HTML, consultez [ce guide](https://www.markdownguide.org/basic-syntax/).

Après avoir créé un nouvel article, n'oubliez pas de l'ajouter au fichier [index.rst](https://github.com/kobotoolbox/docs/blob/master/source/index.rst).

<br/> 


## Ceci est un en-tête

- Ceci est une liste non ordonnée
- en markdown

1. Ceci est une liste numérotée.
2. en markdown.
    - Avec une sous-puce.

Ceci est du **texte en gras** en markdown.

Ceci est du *texte en italique* en markdown.

Ceci est du `code à espacement fixe` en markdown.

> Ceci est un bloc de citation (actuellement non utilisé dans la documentation)

Intégrer des liens : Pour transférer la propriété de votre équipe à un autre utilisateur ou une autre utilisatrice, [veuillez contacter notre équipe d'assistance](support@kobotoolbox.org).

En savoir plus sur [nos services de formation](https://www.kobotoolbox.org/services/training/).

**Liens vers d'autres articles :** Pour plus d'informations, consultez [les permissions au niveau des lignes](row_level_permissions.md)

Lien vers [une autre section](#ajout-de-fichiers-multimedias) dans l'article. Remarque : un seul # pour toutes les tailles d'en-tête, pas d'espace entre # et le nom de l'ancre, les noms de balises d'ancrage doivent être en minuscules et délimités par des tirets s'ils comportent plusieurs mots.

Pour transformer rapidement une URL ou une adresse e-mail en lien, placez-la entre crochets angulaires.

<https://www.markdownguide.org>
<fake@example.com>

Ajoutez une ligne pour séparer le contenu :

---

Ajoutez une ligne vide...

...pour commencer un nouveau paragraphe ou un saut de ligne.

Pour ajouter un saut de ligne complet, utilisez :

<br/> 



## Ajout de fichiers multimédias

### Ajout d'images

![image](/images/getting_started_organization_feature/organizations_project_views.gif)

Stockez les images dans le [dossier images](https://github.com/kobotoolbox/docs/tree/master/source/images), dans un dossier portant le nom de l'article d'assistance. Incluez le nom du dossier et le nom du fichier image dans le chemin d'accès ci-dessus.

### Ajout d'icônes
Cliquez sur l'icône <i class="k-icon k-icon-more"></i> **Plus d'actions** pour l'utilisatrice ou l'utilisateur que vous souhaitez supprimer.

Cliquez sur <i class="k-icon k-icon-replace"></i> **Remplacer le formulaire**.

Pour une liste complète de toutes les icônes, consultez [ici](https://support.kobotoolbox.org/fr/article_template.html#liste-des-icones) et également [ici](https://support.kobotoolbox.org/_static/kpi-icons/k-icons.html).

### Ajout d'une vidéo YouTube

Nous recommandons de publier des vidéos sur YouTube et d'intégrer un lien à l'aide d'iframes. 

<iframe src="https://www.youtube.com/embed/oKtMmBAlHho?si=OqS7-rewYMf-Rrw2" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Incluez le lien de la vidéo YouTube à l'intérieur de l'iframe.

Vous pouvez également inclure des vidéos de la manière suivante :

<video controls>
  <source
    src="./_static/files/getting_started_xlsform/getting_started_xlsform_v2.mp4"
    type="video/mp4"
  />
</video>


<br/> 

## Ajout de tableaux

### Tableau normal 

| **Nom de la colonne**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| hint               | Indice de question                                  |
| guidance_hint      | Indice d'orientation                                  |
| required           | Option pour rendre une question obligatoire            |
| relevant           | Conditions de logique de saut pour la question         |
| constraint         | Critères de validation pour la question           |
| constraint_message | Message d'erreur lorsque les critères de validation ne sont pas respectés |
| appearance         | Options d'affichage des questions        |
| choice_filter      | Critères pour la sélection en cascade                  |
| parameters         | Paramètres pour des types de questions spécifiques           |
| calculation        | Expression mathématique pour la question de calcul |
| default            | Réponse par défaut pour une question                |

### Tableau XLSForm

| type | name     | label              |
| :--- | :------- | :----------------- |
| text | yourname | Quel est votre nom ? |
| survey |

Notez le `| survey |` en bas du tableau.


### Fixer la largeur du tableau

Si l'une des colonnes n'est pas assez large, ajoutez des espaces `&emsp;` pour l'élargir, comme ci-dessous :

| **Paramètre d'exportation** | **Description**                                |
| :-------------------- | :------------------------------------ |
| Enregistrer la sélection sous… &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Cochez cette option et saisissez un nom pour vos paramètres d'exportation. Lorsque vous cliquez sur <strong>EXPORTER</strong>, ces paramètres seront enregistrés et le nom apparaîtra dans la zone <strong>Appliquer les paramètres d'exportation enregistrés</strong>. | 


<br/> 

## Mise en forme HTML

À l'intérieur des encadrés de notes et des tableaux, **utilisez HTML** pour mettre en forme votre texte. Par exemple :

<p class="note">
  <b>Remarque importante</b> : Il n'est pas possible de partager des projets et des données entre les deux serveurs. Cela signifie que toutes les utilisatrices et tous les utilisateurs travaillant sur un projet partagé doivent utiliser le même serveur pour accéder au projet. <a href="https://www.kobotoolbox.org/about-us">Ajoutez un lien en HTML comme ceci.</a></li>
</p>

<p class="note">
  <b>Remarque :</b> Pour en savoir plus sur les permissions au niveau des lignes, consultez <a class="reference" href="row_level_permissions.html">l'accès au niveau des lignes</a>.
</p>

<p class="note">
  <b>Remarque :</b> Pour en savoir plus sur les types de questions dans XLSForm, consultez <a class="reference external" href="https://xlsform.org/en/#question-types">Types de questions (XLSForm.org)</a>.
</p>

| Serveur                            | URL                                                                           |
| :-------------------------------- | :---------------------------------------------------------------------------- |
| Le serveur KoboToolbox mondial         | <a href="https://kf.kobotoolbox.org" class="reference">kf.kobotoolbox.org</a> |
| Le serveur KoboToolbox Union européenne | <a href="https://eu.kobotoolbox.org" class="reference">eu.kobotoolbox.org</a> |


<p class='note'>Vous pouvez télécharger les fichiers <a download class='reference'
href='./_static/files/media/xlsform-example.xls'>ici</a> et les fichiers multimédias <a
download class='reference'
href='./_static/files/media/xlsform-example-media.zip'>ici</a>. Les fichiers sont stockés dans ./_static/files/media/.</p>

Sauts de ligne en HTML :
<p>Ceci est la première ligne.<br>
Et ceci est la deuxième ligne.</p>

Mettez votre texte en <strong>gras</strong>, en <em>italique</em>, ou en <code>code à espacement fixe</code>.

Ajoutez une liste numérotée :
<ol>
  <li>Premier élément.</li>
  <li>Deuxième élément.</li>
  <li>Troisième élément.</li>
  <li>Quatrième élément.</li>
</ol>

Ajoutez une liste non numérotée :
<ul>
  <li>Premier élément</li>
  <li>Deuxième élément</li>
  <li>Troisième élément</li>
  <li>Quatrième élément</li>
</ul>

<br/> 

## Dépannage

<details>
<summary><strong>Enketo vs KoboCollect</strong></summary>
<br>
    Utilisez ce format pour configurer des <strong>sections de dépannage</strong> dans vos articles d'assistance. Incluez un titre court qui décrit clairement le problème et proposez des solutions ici.
    <br><br>
    Pour séparer les lignes à l'intérieur d'un élément de dépannage, ajoutez un double saut de ligne.
</details>

<details>
<summary><strong>Enketo vs KoboCollect</strong></summary>
<br>
Utilisez ce format pour configurer des <strong>sections de dépannage</strong> dans vos articles d'assistance. Incluez un titre court qui décrit clairement le problème et proposez des solutions ici.
</details>

<br/> 

## Liste des icônes

<details>
<summary><strong>Flèches</strong></summary>
<br>

k-icon-angle-bar-left	<i class="k-icon k-icon-angle-bar-left"></i>

k-icon-angle-bar-right	<i class="k-icon k-icon-angle-bar-right"></i>

k-icon-angle-down	<i class="k-icon k-icon-angle-down"></i>

k-icon-angle-left	<i class="k-icon k-icon-angle-left"></i>

k-icon-angle-right	<i class="k-icon k-icon-angle-right"></i>

k-icon-angle-up	<i class="k-icon k-icon-angle-up"></i>

k-icon-arrow-down-left	<i class="k-icon k-icon-arrow-down-left"></i>

k-icon-arrow-down-right	<i class="k-icon k-icon-arrow-down-right"></i>

k-icon-arrow-down	<i class="k-icon k-icon-arrow-down"></i>

k-icon-arrow-left	<i class="k-icon k-icon-arrow-left"></i>

k-icon-arrow-right	<i class="k-icon k-icon-arrow-right"></i>

k-icon-arrow-up-left	<i class="k-icon k-icon-arrow-up-left"></i>

k-icon-arrow-up-right	<i class="k-icon k-icon-arrow-up-right"></i>

k-icon-arrow-up	<i class="k-icon k-icon-arrow-up"></i>

k-icon-caret-down	<i class="k-icon k-icon-caret-down"></i>

k-icon-caret-left	<i class="k-icon k-icon-caret-left"></i>

k-icon-caret-right	<i class="k-icon k-icon-caret-right"></i>

k-icon-caret-up	<i class="k-icon k-icon-caret-up"></i>

    
</details>

<details>
<summary><strong>Interface de création de formulaires</strong></summary>
<br>

k-icon-kobo 	<i class="k-icon k-icon-kobo"></i>

k-icon-cascading 	<i class="k-icon k-icon-cascading"></i>

k-icon-drag-handle 	<i class="k-icon k-icon-drag-handle"></i>

k-icon-duplicate 	<i class="k-icon k-icon-duplicate"></i>

k-icon-edit 	<i class="k-icon k-icon-edit"></i>

k-icon-expand-list 	<i class="k-icon k-icon-expand-list"></i>

k-icon-expand 	<i class="k-icon k-icon-expand"></i>

k-icon-file-audio 	<i class="k-icon k-icon-file-audio"></i>

k-icon-file-image 	<i class="k-icon k-icon-file-image"></i>

k-icon-file-video 	<i class="k-icon k-icon-file-video"></i>

k-icon-file-xls 	<i class="k-icon k-icon-file-xls"></i>

k-icon-file-xml 	<i class="k-icon k-icon-file-xml"></i>

k-icon-file	<i class="k-icon k-icon-file"></i>

k-icon-group-split 	<i class="k-icon k-icon-group-split"></i>

k-icon-group 	<i class="k-icon k-icon-group"></i>

k-icon-media-files	<i class="k-icon k-icon-media-files"></i>

k-icon-question 	<i class="k-icon k-icon-question"></i>

k-icon-settings 	<i class="k-icon k-icon-settings"></i>

k-icon-skip-logic 	<i class="k-icon k-icon-skip-logic"></i>

k-icon-view-all 	<i class="k-icon k-icon-view-all"></i>

k-icon-view 	<i class="k-icon k-icon-view"></i>
   
</details>

<details>
<summary><strong>Types de questions</strong></summary>
<br>

k-icon-qt-acknowledge-lock 	<i class="k-icon k-icon-qt-acknowledge-lock"></i>

k-icon-qt-acknowledge 	<i class="k-icon k-icon-qt-acknowledge"></i>

k-icon-qt-area-lock 	<i class="k-icon k-icon-qt-area-lock"></i>

k-icon-qt-area 	<i class="k-icon k-icon-qt-area"></i>

k-icon-qt-audio-lock 	<i class="k-icon k-icon-qt-audio-lock"></i>

k-icon-qt-audio 	<i class="k-icon k-icon-qt-audio"></i>

k-icon-qt-background-audio 	<i class="k-icon k-icon-qt-background-audio"></i>

k-icon-qt-barcode-lock 	<i class="k-icon k-icon-qt-barcode-lock"></i>

k-icon-qt-barcode 	<i class="k-icon k-icon-qt-barcode"></i>

k-icon-qt-calculate-lock 	<i class="k-icon k-icon-qt-calculate-lock"></i>

k-icon-qt-calculate 	<i class="k-icon k-icon-qt-calculate"></i>

k-icon-qt-date-lock 	<i class="k-icon k-icon-qt-date-lock"></i>

k-icon-qt-date-time-lock 	<i class="k-icon k-icon-qt-date-time-lock"></i>

k-icon-qt-date-time 	<i class="k-icon k-icon-qt-date-time"></i>

k-icon-qt-date 	<i class="k-icon k-icon-qt-date"></i>

k-icon-qt-decimal-lock 	<i class="k-icon k-icon-qt-decimal-lock"></i>

k-icon-qt-decimal k-icon-qt-external-xml-lock 	<i class="k-icon k-icon-qt-decimal k-icon-qt-external-xml-lock"></i>

k-icon-qt-external-xml 	<i class="k-icon k-icon-qt-external-xml"></i>

k-icon-qt-file-lock 	<i class="k-icon k-icon-qt-file-lock"></i>

k-icon-qt-file 	<i class="k-icon k-icon-qt-file"></i>

k-icon-qt-hidden-lock 	<i class="k-icon k-icon-qt-hidden-lock"></i>

k-icon-qt-hidden 	<i class="k-icon k-icon-qt-hidden"></i>

k-icon-qt-line-lock 	<i class="k-icon k-icon-qt-line-lock"></i>

k-icon-qt-line 	<i class="k-icon k-icon-qt-line"></i>

k-icon-qt-meta-default 	<i class="k-icon k-icon-qt-meta-default"></i>

k-icon-qt-note-lock 	<i class="k-icon k-icon-qt-note-lock"></i>

k-icon-qt-note 	<i class="k-icon k-icon-qt-note"></i>

k-icon-qt-number-lock 	<i class="k-icon k-icon-qt-number-lock"></i>

k-icon-qt-number 	<i class="k-icon k-icon-qt-number"></i>

k-icon-qt-photo-lock 	<i class="k-icon k-icon-qt-photo-lock"></i>

k-icon-qt-photo 	<i class="k-icon k-icon-qt-photo"></i>

k-icon-qt-point-lock 	<i class="k-icon k-icon-qt-point-lock"></i>

k-icon-qt-point 	<i class="k-icon k-icon-qt-point"></i>

k-icon-qt-question-matrix-lock 	<i class="k-icon k-icon-qt-question-matrix-lock"></i>

k-icon-qt-question-matrix 	<i class="k-icon k-icon-qt-question-matrix"></i>

k-icon-qt-range-lock 	<i class="k-icon k-icon-qt-range-lock"></i>

k-icon-qt-range 	<i class="k-icon k-icon-qt-range"></i>

k-icon-qt-ranking-lock 	<i class="k-icon k-icon-qt-ranking-lock"></i>

k-icon-qt-ranking 	<i class="k-icon k-icon-qt-ranking"></i>

k-icon-qt-rating-lock 	<i class="k-icon k-icon-qt-rating-lock"></i>

k-icon-qt-rating 	<i class="k-icon k-icon-qt-rating"></i>

k-icon-qt-select-many-from-file-lock 	<i class="k-icon k-icon-qt-select-many-from-file-lock"></i>

k-icon-qt-select-many-from-file 	<i class="k-icon k-icon-qt-select-many-from-file"></i>

k-icon-qt-select-many-lock 	<i class="k-icon k-icon-qt-select-many-lock"></i>

k-icon-qt-select-many 	<i class="k-icon k-icon-qt-select-many"></i>

k-icon-qt-select-one-from-file-lock 	<i class="k-icon k-icon-qt-select-one-from-file-lock"></i>

k-icon-qt-select-one-from-file 	<i class="k-icon k-icon-qt-select-one-from-file"></i>

k-icon-qt-select-one-lock 	<i class="k-icon k-icon-qt-select-one-lock"></i>

k-icon-qt-select-one 	<i class="k-icon k-icon-qt-select-one"></i>

k-icon-qt-text-lock 	<i class="k-icon k-icon-qt-text-lock"></i>

k-icon-qt-text 	<i class="k-icon k-icon-qt-text"></i>

k-icon-qt-time-lock 	<i class="k-icon k-icon-qt-time-lock"></i>

k-icon-qt-time 	<i class="k-icon k-icon-qt-time"></i>

k-icon-qt-video-lock 	<i class="k-icon k-icon-qt-video-lock"></i>

k-icon-qt-video	<i class="k-icon k-icon-qt-video"></i>

   
</details>

<details>
<summary><strong>Gestion de projet</strong></summary>
<br>
    
k-icon-archived 	<i class="k-icon k-icon-archived"></i>

k-icon-data-sync 	<i class="k-icon k-icon-data-sync"></i>

k-icon-deploy	<i class="k-icon k-icon-deploy"></i>

k-icon-document 	<i class="k-icon k-icon-document"></i>

k-icon-download 	<i class="k-icon k-icon-download"></i>

k-icon-drafts	<i class="k-icon k-icon-drafts"></i>

k-icon-language-alt 	<i class="k-icon k-icon-language-alt"></i>

k-icon-language-default 	<i class="k-icon k-icon-language-default"></i>

k-icon-language-settings 	<i class="k-icon k-icon-language-settings"></i>

k-icon-language 	<i class="k-icon k-icon-language"></i>

k-icon-logout 	<i class="k-icon k-icon-logout"></i>

k-icon-menu 	<i class="k-icon k-icon-menu"></i>

k-icon-project-archived 	<i class="k-icon k-icon-project-archived"></i>

k-icon-project-deployed 	<i class="k-icon k-icon-project-deployed"></i>

k-icon-project-draft 	<i class="k-icon k-icon-project-draft"></i>

k-icon-project-locked 	<i class="k-icon k-icon-project-locked"></i>

k-icon-project-overview 	<i class="k-icon k-icon-project-overview"></i>

k-icon-project 	<i class="k-icon k-icon-project"></i>

k-icon-projects 	<i class="k-icon k-icon-projects"></i>

k-icon-replace 	<i class="k-icon k-icon-replace"></i>

k-icon-upload 	<i class="k-icon k-icon-upload"></i>

k-icon-user-share 	<i class="k-icon k-icon-user-share"></i>

k-icon-user 	<i class="k-icon k-icon-user"></i>

k-icon-users	<i class="k-icon k-icon-users"></i>

   
</details>

<details>
<summary><strong>Données</strong></summary>
<br>
    
k-icon-filter-arrows 	<i class="k-icon k-icon-filter-arrows"></i>

k-icon-filter 	<i class="k-icon k-icon-filter"></i>

k-icon-map-view 	<i class="k-icon k-icon-map-view"></i>

k-icon-gallery 	<i class="k-icon k-icon-gallery"></i>

k-icon-globe-alt	<i class="k-icon k-icon-globe-alt"></i>

k-icon-layer 	<i class="k-icon k-icon-layer"></i>

k-icon-hide 	<i class="k-icon k-icon-hide"></i>

k-icon-reports 	<i class="k-icon k-icon-reports"></i>

k-icon-sort-ascending 	<i class="k-icon k-icon-sort-ascending"></i>

k-icon-sort-default 	<i class="k-icon k-icon-sort-default"></i>

k-icon-sort-descending 	<i class="k-icon k-icon-sort-descending"></i>

k-icon-table 	<i class="k-icon k-icon-table"></i>

k-icon-unfreeze 	<i class="k-icon k-icon-unfreeze"></i>


 </details>

<details>
<summary><strong>Dossiers et bibliothèque</strong></summary>
<br>

k-icon-folder-in 	<i class="k-icon k-icon-folder-in"></i>

k-icon-folder-out 	<i class="k-icon k-icon-folder-out"></i>

k-icon-folder-plus 	<i class="k-icon k-icon-folder-plus"></i>

k-icon-folder-public 	<i class="k-icon k-icon-folder-public"></i>

k-icon-folder-shared 	<i class="k-icon k-icon-folder-shared"></i>

k-icon-folder-subscribed 	<i class="k-icon k-icon-folder-subscribed"></i>

k-icon-folder 	<i class="k-icon k-icon-folder"></i>

k-icon-freeze 	<i class="k-icon k-icon-freeze"></i>

k-icon-block 	<i class="k-icon k-icon-block"></i>

k-icon-library-public 	<i class="k-icon k-icon-library-public"></i>

k-icon-library 	<i class="k-icon k-icon-library"></i>

k-icon-template-locked 	<i class="k-icon k-icon-template-locked"></i>

k-icon-template 	<i class="k-icon k-icon-template"></i>

 
</details>

<details>
<summary><strong>Symboles</strong></summary>
<br>

k-icon-alert 	<i class="k-icon k-icon-alert"></i>

k-icon-check-circle 	<i class="k-icon k-icon-check-circle"></i>

k-icon-check 	<i class="k-icon k-icon-check"></i>

k-icon-close 	<i class="k-icon k-icon-close"></i>

k-icon-expand-arrow 	<i class="k-icon k-icon-expand-arrow"></i>

k-icon-flows 	<i class="k-icon k-icon-flows"></i>

k-icon-help-articles 	<i class="k-icon k-icon-help-articles"></i>

k-icon-help 	<i class="k-icon k-icon-help"></i>

k-icon-information 	<i class="k-icon k-icon-information"></i>

k-icon-link 	<i class="k-icon k-icon-link"></i>

k-icon-lock-alt 	<i class="k-icon k-icon-lock-alt"></i>

k-icon-lock 	<i class="k-icon k-icon-lock"></i>

k-icon-minus 	<i class="k-icon k-icon-minus"></i>

k-icon-more-vertical 	<i class="k-icon k-icon-more-vertical"></i>

k-icon-more 	<i class="k-icon k-icon-more"></i>

k-icon-notification 	<i class="k-icon k-icon-notification"></i>

k-icon-pause 	<i class="k-icon k-icon-pause"></i>

k-icon-play 	<i class="k-icon k-icon-play"></i>

k-icon-plus	<i class="k-icon k-icon-plus"></i>

k-icon-search 	<i class="k-icon k-icon-search"></i>

k-icon-spinner 	<i class="k-icon k-icon-spinner"></i>

k-icon-stop 	<i class="k-icon k-icon-stop"></i>

k-icon-trash 	<i class="k-icon k-icon-trash"></i>

k-icon-warning 	<i class="k-icon k-icon-warning"></i>

</details>

<details>
<summary><strong>Assistance et réseaux sociaux</strong></summary>
<br>

k-icon-email 	<i class="k-icon k-icon-email"></i>

k-icon-help-academy 	<i class="k-icon k-icon-help-academy"></i>

k-icon-help-forum 	<i class="k-icon k-icon-help-forum"></i>

k-icon-logo-github 	<i class="k-icon k-icon-logo-github"></i>

k-icon-logo-instagram 	<i class="k-icon k-icon-logo-instagram"></i>

k-icon-logo-linkedin 	<i class="k-icon k-icon-logo-linkedin"></i>

k-icon-logo-twitter 	<i class="k-icon k-icon-logo-twitter"></i>

k-icon-mail 	<i class="k-icon k-icon-mail"></i>

k-icon-intercom 	<i class="k-icon k-icon-intercom"></i>

k-icon-subscribe 	<i class="k-icon k-icon-subscribe"></i>

k-icon-unsubscribe 	<i class="k-icon k-icon-unsubscribe"></i>

</details>

<details>
<summary><strong>Autre</strong></summary>
<br>

k-icon-attach 	<i class="k-icon k-icon-attach"></i>

k-icon-editor 	<i class="k-icon k-icon-editor"></i>

k-icon-heatmap 	<i class="k-icon k-icon-heatmap"></i>

k-icon-pdf 	<i class="k-icon k-icon-pdf"></i>

k-icon-pins 	<i class="k-icon k-icon-pins"></i>

k-icon-print 	<i class="k-icon k-icon-print"></i>

k-icon-spreadsheet 	<i class="k-icon k-icon-spreadsheet"></i>

</details>