# Supprimer des fichiers multimédias
<a href="../deleting_media.html">Read in English</a> | <a href="../es/deleting_media.html">Leer en español</a> | <a href="../ar/deleting_media.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/32227ed7144b2a84f5774494d8d5ac4935ca0349/source/deleting_media.md" class="reference">4 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/J0-mh1R6dEs?si=I4Oe8NHX7Ks5rFza" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Vous pouvez avoir besoin de supprimer des fichiers multimédias de votre projet KoboToolbox pour diverses raisons, telles que le maintien de la confidentialité, la gestion de l'espace de stockage ou la correction d'erreurs de soumission. Cet article explique comment supprimer des fichiers multimédias individuels ou plusieurs fichiers en masse, y compris des images, des vidéos, des fichiers audio et des fichiers de documents.

## Supprimer des fichiers multimédias individuels

Il existe deux façons de supprimer des fichiers multimédias individuels : directement depuis le tableau de données ou en ouvrant la soumission. Une fois qu'un fichier est supprimé, il est marqué comme _Supprimé_ dans le tableau de données et ne peut pas être récupéré.

### Supprimer des fichiers multimédias individuels depuis le tableau de données

Vous pouvez supprimer des images, des vidéos et des fichiers individuels directement depuis le tableau de données, en suivant les étapes suivantes :

1. Dans le tableau de données, localisez la cellule contenant le fichier multimédia que vous souhaitez supprimer.
2. Cliquez sur l'icône <i class="k-icon k-icon-qt-photo"></i> **image**, <i class="k-icon k-icon-qt-video"></i> **vidéo** ou <i class="k-icon k-icon-qt-file"></i> **fichier**.
3. Cliquez sur les <i class="k-icon k-icon-more"></i> **trois points** en haut de l'aperçu du fichier.
4. Cliquez sur <i class="k-icon k-icon-trash"></i> **Supprimer**, puis sur **Supprimer** à nouveau pour confirmer.

![image](/images/deleting_media/delete_from_table.png)

### Supprimer des fichiers multimédias individuels dans la vue de soumission

Vous pouvez également supprimer des fichiers multimédias en ouvrant la vue de soumission :

1. Dans le tableau de données, localisez la soumission contenant les fichiers multimédias que vous souhaitez supprimer.
2. Sur le côté gauche de la soumission, cliquez sur <i class="k-icon k-icon-view"></i> **Ouvrir**.
3. Faites défiler jusqu'au fichier multimédia que vous souhaitez supprimer.
4. Cliquez sur les <i class="k-icon k-icon-more"></i> **trois points** à droite du fichier multimédia.
5. Cliquez sur <i class="k-icon k-icon-trash"></i> **Supprimer**, puis sur **Supprimer** à nouveau pour confirmer.

![image](/images/deleting_media/open_submission_view.png)

### Supprimer des fichiers audio dans la vue de question audio
Vous pouvez supprimer des fichiers audio en ouvrant la vue de question audio pour la transcription, la traduction et l'analyse des questions audio :

1. Dans le tableau de données, cliquez sur **Ouvrir** <i class="k-icon k-icon-arrow-up-right"></i> pour ouvrir la vue de question audio.
2. Dans l'onglet **TRANSCRIPTION**, **TRADUCTIONS** ou **ANALYSE**, localisez le fichier audio dans le coin supérieur droit.
3. Cliquez sur les <i class="k-icon k-icon-more"></i> **trois points** à droite du fichier audio.
4. Cliquez sur <i class="k-icon k-icon-trash"></i> **Supprimer**, puis sur **Supprimer** à nouveau pour confirmer.

![image](/images/deleting_media/delete_audio.png)

## Supprimer des fichiers multimédias en masse

Vous pouvez avoir besoin de supprimer des fichiers multimédias en masse, par exemple, pour gérer l'espace de stockage après leur exportation. Vous pouvez supprimer tous les fichiers multimédias pour les soumissions sélectionnées en suivant les étapes suivantes :

1. Sélectionnez les soumissions pour lesquelles vous souhaitez supprimer des fichiers multimédias.
2. Cliquez sur **Supprimer uniquement les fichiers multimédias** au-dessus du tableau de données.
   * Cette action ouvre une fenêtre modale indiquant le nombre et les types de fichiers multimédias à supprimer avec cette sélection.
3. Cochez la case indiquant « Vous êtes sur le point de supprimer définitivement les fichiers multimédias suivants des soumissions sélectionnées : ».
   * Cette étape reconnaît que les fichiers seront supprimés définitivement et ne sont pas récupérables.
4. Cliquez sur **Supprimer**.

<p class="note">
  <b>Note :</b> Avec cette approche, tous les fichiers multimédias de chaque soumission sélectionnée seront supprimés ; il n'est actuellement pas possible de choisir uniquement les fichiers pour une question donnée.
</p>

![image](/images/deleting_media/bulk_delete.png)