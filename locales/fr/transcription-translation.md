# Transcription et traduction de réponses audio
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/eaaa0a122cb15511b64a66babaa5dad10f6aa7a9/source/transcription-translation.md" class="reference">6 oct. 2026</a>


<iframe src="https://www.youtube.com/embed/vefmH9JzJTU?si=8aF_U8M6BAft9kRr&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Les outils de traitement automatique du langage naturel de KoboToolbox vous aident à collecter, gérer et analyser plus efficacement des données qualitatives. Ces outils comprennent la transcription automatique de la parole en texte et la traduction automatique, qui peuvent préparer les réponses audio pour l'[analyse qualitative automatisée](https://support.kobotoolbox.org/qualitative_analysis.html).

Vous pouvez transcrire et traduire des réponses individuellement, ou traiter plusieurs soumissions en masse depuis le tableau de données. Cet article explique comment transcrire des réponses audio et traduire des transcriptions, individuellement ou en masse, et présente les langues disponibles ainsi que les limites d'utilisation des options automatiques.

<p class="note">
    <strong>Note</strong> : la transcription et la traduction automatiques ne sont pas forcément disponibles pour <a href="#supported-languages-for-transcription-and-translation">toutes les langues</a>. Pour ces langues, seules la transcription et la traduction manuelles sont possibles.
</p>

## Collecter des réponses audio
Avant de transcrire ou de traduire des réponses audio, vous devez collecter des données audio dans votre projet.

1. Ajoutez une [question de type Audio](https://support.kobotoolbox.org/photo_audio_video_file.html) à votre formulaire ou activez les [enregistrements audio d'arrière-plan](https://support.kobotoolbox.org/qualitative_data.html#recording-interviews-with-background-audio-recordings).
2. Déployez le formulaire et collectez des soumissions contenant des enregistrements audio.

<p class="note">
    <strong>Note</strong> : pour certaines langues disponibles, la transcription automatique peut ne pas fonctionner avec des fichiers audio de plus de 50 minutes. Pour les entretiens longs, envisagez d'utiliser plusieurs questions audio individuelles plutôt qu'un seul enregistrement audio d'arrière-plan.
</p>

Une fois les réponses audio transcrites et traduites, la transcription originale de vos fichiers audio et tous les textes traduits sont ajoutés sous forme de nouvelles colonnes dans le tableau de données. Vous pouvez les [télécharger](https://support.kobotoolbox.org/export_download.html) avec les données de votre enquête.


## Transcrire des fichiers audio individuellement

![Exemple d'ajout de transcriptions automatiques](images/transcription_translation/transcription.png)

Pour commencer à transcrire des réponses audio individuellement :

1. Ouvrez votre projet et accédez à **DONNÉES > Tableau**.
2. Cliquez sur le bouton <i class="ti-outline ti-pencil-star"></i> **Ouvrir** à côté de la réponse audio que vous souhaitez transcrire.
3. Dans l'onglet **TRANSCRIPTION**, cliquez sur **commencer** (**begin**).
- Sélectionnez la langue d'origine du fichier audio.
    - Si elle est disponible, sélectionnez l'option **automatique** (**automatic**). L'option **manuelle** (**manual**) vous permet de transcrire manuellement l'enregistrement audio dans n'importe quelle langue.
    - Cliquez sur **créer la transcription** (**create transcript**) pour lancer la transcription automatique.
4. Une fois la transcription terminée, vous pouvez la modifier manuellement. Vous pouvez écouter l'enregistrement audio en haut à droite pour vérifier l'exactitude de la transcription.
    - Après avoir modifié la transcription, cliquez sur le bouton **Sauvegarder** pour vous assurer que votre travail est bien enregistré.
5. Lorsque vous avez terminé, cliquez sur **TERMINÉ** pour quitter, passez à la soumission suivante en cliquant sur les flèches à côté du bouton **TERMINÉ**, ou accédez à l'onglet **TRADUCTIONS**.
    - Si vous cliquez sur **TERMINÉ**, vous revenez à l'affichage du tableau de données, où une nouvelle colonne contenant la transcription a été ajoutée.

<p class="note">
    <strong>Note</strong> : les transcriptions et traductions générées automatiquement doivent être sauvegardées pour éviter toute perte de données. Quitter la page sans sauvegarder peut entraîner la perte des données.
</p>

## Transcrire des fichiers audio en masse

Vous pouvez transcrire automatiquement les enregistrements audio de plusieurs soumissions à la fois depuis le tableau de données.

Pour transcrire des réponses audio en masse :

1. Ouvrez votre projet et accédez à **DONNÉES > Tableau.**
2. Sélectionnez les soumissions que vous souhaitez transcrire à l'aide des cases à cocher à gauche.
3. Dans la colonne contenant les enregistrements audio à transcrire, cliquez sur la flèche dans l'en-tête de la colonne.
4. Cliquez sur **Transcrire les fichiers audio sélectionnés** (**Transcribe selected audio files**).
5. Sélectionnez la langue et la région, puis cliquez sur **Démarrer la transcription** (**Start transcription**).

![Transcrire des fichiers audio en masse](images/transcription_translation/bulk_transcribe_files.png)

Les transcriptions terminées sont ajoutées à une nouvelle colonne du tableau de données et marquées comme prêtes à être relues.

### Relire et approuver les transcriptions

Relire les transcriptions automatiques pour confirmer qu'elles reflètent fidèlement les enregistrements audio permet de s'assurer que les données sont fiables et prêtes pour l'analyse ou la traduction.

Pour relire et approuver une transcription individuelle :

1. Cliquez sur **Relire** (**Review**).
2. Effectuez les modifications nécessaires.
3. Sauvegardez la transcription et passez à la suivante.

Pour approuver plusieurs transcriptions à la fois :

1. Sélectionnez les soumissions concernées à l'aide des cases à cocher à gauche.
2. Dans la colonne de transcription, cliquez sur la flèche dans l'en-tête de la colonne.
3. Cliquez sur **Approuver toutes les transcriptions sélectionnées** (**Approve all selected**).

![Approuver des transcriptions en masse](images/transcription_translation/bulk_approve_transcripts.png)

## Traduire des transcriptions individuellement

![Exemple d'ajout de traductions automatiques](images/transcription_translation/translation.png)

Une fois la transcription de votre réponse audio terminée, vous pouvez ajouter des traductions dans plusieurs langues :

1. Depuis l'onglet **TRANSCRIPTION**, accédez à l'onglet **TRADUCTIONS**.
    - L'option de traduction n'est disponible qu'une fois la transcription terminée.
2. Cliquez sur **commencer** (**begin**) et choisissez la langue de la traduction.
    - Si elle est disponible, sélectionnez **automatique** (**automatic**) pour la traduction automatique. L'option **manuelle** (**manual**) vous permet de traduire manuellement la transcription dans n'importe quelle langue.
    - Cliquez sur **créer la traduction** (**create translation**) pour lancer la traduction automatique.
3. Une fois la traduction terminée, vous pouvez la modifier manuellement. La transcription originale s'affiche à droite de l'écran et l'audio original en dessous.
    - Après avoir modifié la traduction, cliquez sur le bouton **Sauvegarder** pour vous assurer que votre travail est bien enregistré.
4. Lorsque la traduction est terminée, vous pouvez ajouter une autre traduction en cliquant sur <i class="k-icon-plus"></i> **nouvelle traduction** (**new translation**), passer à la soumission suivante en cliquant sur les flèches à côté du numéro d'élément dans le coin supérieur droit, ou cliquer sur **TERMINÉ** pour revenir au tableau de données.

<p class="note">
    <strong>Note</strong> : un fichier audio ne peut contenir qu'une seule transcription, mais chaque transcription peut avoir plusieurs traductions.
</p>

## Traduire des transcriptions en masse

Vous pouvez également traduire automatiquement plusieurs transcriptions à la fois depuis le tableau de données.

Pour traduire des transcriptions en masse :

1. Assurez-vous que votre projet contient des transcriptions audio terminées.
2. Ouvrez votre projet et accédez à **DONNÉES > Tableau.**
3. Sélectionnez les soumissions contenant les transcriptions à traduire à l'aide des cases à cocher à gauche.
4. Dans la colonne de transcription que vous souhaitez traduire, cliquez sur la flèche dans l'en-tête de la colonne.
5. Cliquez sur **Traduire les transcriptions sélectionnées** (**Translate selected transcriptions**).
6. Recherchez et sélectionnez la langue cible, puis cliquez sur **Créer les traductions** (**Create translations**).

![Traduire des transcriptions en masse](images/transcription_translation/bulk_translate_transcriptions.png)

Les traductions terminées sont ajoutées à une nouvelle colonne du tableau de données et marquées comme prêtes à être relues.

### Relire et approuver les traductions

Pour relire et approuver une traduction individuelle :

1. Cliquez sur **Relire** (**Review**).
2. Effectuez les modifications nécessaires.
3. Sauvegardez la traduction et passez à la suivante.

Pour approuver plusieurs traductions à la fois :

1. Sélectionnez les soumissions concernées à l'aide des cases à cocher à gauche.
2. Dans la colonne de traduction, cliquez sur la flèche dans l'en-tête de la colonne.
3. Cliquez sur **Approuver toutes les traductions sélectionnées** (**Approve all selected**).


## Langues disponibles pour la transcription et la traduction

Les fonctionnalités de traitement du langage naturel de KoboToolbox intègrent des capacités de reconnaissance automatique de la parole (ASR) et de traduction automatique (MT) fournies par Google Cloud Compute, qui propose actuellement la **transcription automatique dans 112 langues** (avec 142 variantes régionales) et la **traduction automatique dans 129 langues**.

<p class="note">
<strong>Note :</strong> les fichiers audio et les transcriptions ne sont envoyés à Google Cloud Compute que le temps nécessaire pour réaliser la transcription et la traduction. Ils ne sont pas conservés par le service externe après le traitement ni utilisés pour améliorer ce service.
</p>

Pour la transcription ou la traduction manuelle, vous pouvez choisir parmi environ 7 000 langues, d'après la liste exhaustive ISO 639-3 maintenue par SIL International (filtrée sur les « langues vivantes »). Si une langue est disponible pour l'ASR ou la MT, vous pouvez choisir entre les méthodes **manuelle** et **automatique**. Pour les autres langues, seule la méthode **manuelle** est disponible.

<p class="note">
    Pour consulter la liste complète des langues disponibles, voir <a href="https://docs.google.com/spreadsheets/d/1_QDcORZd9qXgfq1OBb61U6ondYfjwmHXOv4XZPjxVVw/edit?usp=sharing">Langues disponibles pour la transcription et la traduction automatiques</a>.
</p>

Si vous ne trouvez pas une langue dans la liste, essayez d'autres orthographes ou d'autres noms. Tous les noms de langues sont actuellement indiqués avec leur nom et leur orthographe en anglais (par exemple, Spanish au lieu de Español). Pour les langues comptant moins de locuteurs, il peut exister d'autres noms. Par exemple, la langue bura du nord du Nigéria figure sous le nom Bura-Pabir, mais elle est également connue sous les noms Bourrah ou Babir.

<p class="note">
    <strong>Note</strong> : lors de la transcription manuelle de réponses audio, il est important de sélectionner la bonne langue. Si la transcription générée manuellement ne correspond pas à la langue ou à la région choisie, les traductions automatiques effectuées ensuite à partir de cette transcription risquent d'être incorrectes et de contenir des erreurs.
</p>

## Limites d'utilisation de la transcription et de la traduction automatiques
Les utilisateurs du plan Community peuvent utiliser jusqu'à **10 minutes de transcription automatique de la parole en texte** par mois et jusqu'à **6 000 caractères de traduction automatique de transcriptions** par mois.

<p class="note">
<strong>Note :</strong> le traitement automatique est comptabilisé dans ces limites, que les fichiers soient traités individuellement ou en masse.
</p>

Si vous avez besoin d'une capacité de transcription ou de traduction supplémentaire, vous pouvez [passer à une offre supérieure](https://www.kobotoolbox.org/pricing/) offrant un quota plus élevé ou [acheter](https://support.kobotoolbox.org/account_settings.html#add-ons) un supplément **pack de traitement du langage naturel (NLP)**. Les suppléments sont proposés selon vos besoins de traitement des données, à partir de 9,95 $ pour 100 minutes de transcription supplémentaires et 60 000 caractères de traduction supplémentaires. Vous pouvez toujours continuer à transcrire et à traduire des réponses audio manuellement, sans limite d'utilisation.


## Résolution de problèmes

<details>
    <summary><strong>La traduction ne se charge pas</strong></summary>
    Il arrive que la deuxième traduction reste bloquée avec une icône de chargement. Si cela se produit, actualisez la page : la traduction devrait apparaître. Nous travaillons à la correction de ce problème.
</details>

<br>

<details>
<summary><strong>Les fichiers audio longs ne sont pas transcrits</strong></summary>
Pour certaines langues disponibles, la transcription automatique peut ne pas fonctionner avec des fichiers audio de plus de 50 minutes.<br><br>
Pour les entretiens longs, envisagez d'utiliser plusieurs questions Audio individuelles plutôt qu'un seul enregistrement audio d'arrière-plan. Découper un entretien en enregistrements plus courts facilite l'importation et la gestion des fichiers, ainsi que la localisation et la transcription de sections précises de l'entretien.<br><br>
Si vous disposez déjà d'un long enregistrement, vous pouvez également télécharger le fichier audio, le diviser en fichiers plus courts, puis importer ces fichiers dans KoboToolbox pour les transcrire.
</details>