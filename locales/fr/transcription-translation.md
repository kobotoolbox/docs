# Transcription et traduction des réponses audio
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/81ea68d620feb190d5829be9521d3f913e88de91/source/transcription-translation.md" class="reference">13 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/vefmH9JzJTU?si=8aF_U8M6BAft9kRr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Les outils de traitement du langage naturel de KoboToolbox vous aident à collecter, gérer et analyser les données qualitatives plus efficacement. Ces outils incluent la transcription automatique de la parole en texte et la traduction automatique, avec une analyse qualitative automatisée à venir prochainement. La transcription originale de vos fichiers audio et tout le texte traduit sont ajoutés comme nouvelles colonnes de données dans le tableau de données et peuvent être [téléchargés](export_download.md) avec vos données d'enquête.

Pour utiliser ces fonctionnalités, collectez d'abord des réponses audio dans votre formulaire en utilisant le [type de question Audio](photo_audio_video_file.md) ou les [enregistrements audio en arrière-plan](recording-interviews.md).


<p class="note">
    <strong>Remarque</strong> : La transcription et la traduction automatiques peuvent ne pas être disponibles pour <a href="#language-list">toutes les langues</a>. Pour ces langues, seules la transcription et la traduction manuelles sont possibles.
</p>

## Ajouter des transcriptions automatiques

![Exemple d'ajout de transcriptions automatiques](images/transcription_translation/transcription.png)

Pour commencer à transcrire vos réponses audio :

1. Ouvrez votre projet et accédez à **DONNÉES > Tableau**.
2. Cliquez sur le bouton **Ouvrir** à côté de la réponse audio que vous souhaitez transcrire.
3. Dans l'onglet **TRANSCRIPTION**, cliquez sur **commencer**.
    - Sélectionnez la langue originale du fichier audio et l'option **automatique** (l'option **manuelle** vous permettra de transcrire manuellement l'enregistrement audio).
    - Cliquez sur **créer une transcription** pour commencer la transcription automatique.
4. Une fois la transcription terminée, vous pouvez la modifier manuellement. Vous pouvez lire l'enregistrement audio dans le coin supérieur droit pour vérifier l'exactitude de la transcription.
    - Après avoir modifié la transcription, cliquez sur le bouton **Enregistrer** pour vous assurer que votre travail est stocké en toute sécurité.
5. Une fois terminé, cliquez sur **TERMINÉ** pour quitter, accédez à la soumission suivante en cliquant sur les flèches à côté du bouton **TERMINÉ**, ou passez à l'onglet **TRADUCTIONS**.
    - Si vous cliquez sur **TERMINÉ**, vous serez redirigé vers la vue du tableau de données, où une nouvelle colonne contenant la transcription aura été ajoutée.

<p class="note">
    <strong>Remarque</strong> : Les transcriptions et traductions générées automatiquement doivent être enregistrées pour éviter la perte de données. Quitter la page sans enregistrer entraînera la perte des données.
</p>

## Ajouter des traductions automatiques

![Exemple d'ajout de traductions automatiques](images/transcription_translation/translation.png)

Une fois que vous avez une transcription complète de votre réponse audio, vous pouvez ajouter des traductions dans plusieurs langues :

1. Passez à l'onglet **TRADUCTIONS**.
    - L'option de traduction n'est disponible qu'une fois qu'une transcription a été complétée.
2. Cliquez sur **commencer** et choisissez la langue de la traduction.
    - Cliquez sur **automatique** pour la traduction automatique (l'option **manuelle** vous permettra de traduire manuellement la transcription)
    - Cliquez sur **créer une traduction** pour commencer la traduction automatique
3. Une fois la traduction terminée, vous pouvez la modifier manuellement. La transcription originale apparaît à droite de l'écran, et l'audio original apparaît en dessous.
    - Après avoir modifié la traduction, cliquez sur le bouton **Enregistrer** pour vous assurer que votre travail est stocké en toute sécurité.
4. Lorsque la traduction est terminée, vous pouvez ajouter une autre traduction en cliquant sur <i class="k-icon-plus"></i> **nouvelle traduction**, passer à la soumission suivante en cliquant sur les flèches à côté du numéro d'élément dans le coin supérieur droit, ou cliquer sur **TERMINÉ** pour revenir au tableau de données.

<p class="note">
    <strong>Remarque</strong> : Les fichiers audio ne peuvent contenir qu'une seule transcription, mais chaque transcription peut avoir plusieurs traductions.
</p>

## Liste des langues

Ces fonctionnalités de traitement du langage naturel intègrent les capacités de reconnaissance vocale automatique (ASR) et de traduction automatique (MT) fournies par Google Cloud Compute, qui offre actuellement la transcription automatique dans 72 langues (avec 138 variantes régionales) et la traduction automatique dans 106 langues. Pour la transcription ou la traduction manuelle, vous pouvez sélectionner parmi environ 7 000 langues basées sur la liste complète ISO 639-3, maintenue par SIL International (filtrée pour les « langues vivantes »). Si une langue prend en charge l'ASR ou la MT, vous pouvez choisir entre les méthodes **manuelle** et **automatique**. Pour les autres langues, seule la méthode **manuelle** est disponible.

Si vous ne trouvez pas une langue dans la liste, envisagez des orthographes ou des noms alternatifs. Tous les noms de langues sont actuellement répertoriés en utilisant leurs noms et orthographes anglais (par exemple, Spanish au lieu de Español). Pour les langues avec moins de locuteurs, il peut y avoir des noms alternatifs. Par exemple, la langue Bura du nord du Nigeria est répertoriée comme Bura-Pabir mais est également connue sous le nom de Bourrah ou Babir.

<p class="note">
    <strong>Remarque</strong> : Lors de la transcription manuelle de réponses audio, il est important de sélectionner la langue correcte. Si la transcription générée manuellement ne correspond pas exactement à la langue ou à la région choisie, les traductions automatiques ultérieures utilisant cette transcription peuvent être incorrectes et produire des inexactitudes.
</p>

## Dépannage

<details>
    <summary><strong>La traduction ne se charge pas</strong></summary>
    Parfois, la deuxième traduction peut rester bloquée avec une icône de chargement. Si cela se produit, actualisez la page et la traduction devrait apparaître. C'est un problème que nous travaillons à résoudre.
</details>