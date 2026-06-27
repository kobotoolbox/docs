# Analyse qualitative des réponses audio
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/8ef3e7ec90848285916af99c022046fd2c56a447/source/qualitative_analysis.md" class="reference">22 juin 2026</a>

<iframe src="https://www.youtube.com/embed/Ud65hNS_cuo?si=aFfCfExpyn3MZVAs&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

L'analyse qualitative permet de transformer des réponses ouvertes en résultats clairs et exploitables. Elle est particulièrement utile dans le cadre de la recherche et des interventions d'urgence, où des informations contextuelles importantes peuvent être manquées si l'on se limite aux données quantitatives.

Avec KoboToolbox, vous pouvez analyser les réponses aux questions audio ouvertes directement dans l'interface utilisateur. Grâce aux questions d'analyse qualitative, vous pouvez résumer, catégoriser et décrire chaque réponse, puis enregistrer ces résultats sous forme de nouvelles colonnes dans votre base de données. Vous pouvez soit **analyser les données manuellement**, soit **utiliser l'intelligence artificielle (IA)**.

Cet article explique comment créer des questions d'analyse, analyser les réponses manuellement ou avec l'IA, examiner et vérifier les résultats, personnaliser les paramètres d'affichage et naviguer entre les réponses lors de l'analyse.

## Prérequis pour l'analyse qualitative

Avant d'utiliser les fonctionnalités d'analyse qualitative, assurez-vous que les conditions suivantes sont remplies :
- Votre formulaire doit inclure au moins une [question Audio](https://support.kobotoolbox.org/fr/photo_audio_video_file.html) ou avoir activé l'[enregistrement audio d'arrière-plan](https://support.kobotoolbox.org/fr/recording-interviews.html#recording-interviews-with-background-audio-recordings).
- Votre projet doit contenir au moins une soumission avec des fichiers audio.
- Pour l'**analyse automatisée**, les fichiers audio doivent d'abord être [transcrits](https://support.kobotoolbox.org/fr/transcription-translation.html), car l'analyse est générée à partir de la transcription originale de l'audio.
    - Pour l'**analyse manuelle**, il est recommandé, mais non obligatoire, de transcrire vos fichiers audio avant de commencer.

<p class="note">
<strong>Note :</strong>
   L'analyse qualitative est actuellement disponible uniquement pour les réponses audio, y compris les enregistrements audio d'arrière-plan. Elle n'est pas encore disponible pour les réponses de type texte ou autres.
</p>

## Créer des questions d'analyse

Pour créer des questions d'analyse qualitative, ouvrez l'interface d'analyse audio de votre projet :

1. Ouvrez votre projet et accédez à **DONNÉES > Tableau.**
2. Cliquez sur **Ouvrir** dans la cellule de la réponse audio que vous souhaitez analyser.
3. Ouvrez l'onglet **ANALYSE**.

![Ouvrir un fichier audio](images/qualitative_analysis/open.png)

Une fois dans l'onglet **ANALYSE**, vous pouvez ajouter des questions d'analyse pour générer des résultats à partir de chaque réponse audio :

1. Cliquez sur **Ajouter une question.**
2. Sélectionnez le [type de question](https://support.kobotoolbox.org/fr/qualitative_analysis.html#analysis-question-types) que vous souhaitez utiliser (par exemple, **Texte** ou **Choix unique**).
3. Saisissez un libellé pour la question d'analyse (par exemple, « Résumer la réponse » ou « Sélectionner les thèmes mentionnés dans la réponse »).
    - Ce libellé devient le nom du champ dans votre base de données.
4. Ajoutez des choix de réponse si nécessaire.

![Ajouter une question](images/qualitative_analysis/add_question.png)

Chaque question d'analyse que vous créez apparaîtra dans l'onglet **ANALYSE** pour les autres réponses à la même question audio.

<p class="note">
<strong>Note :</strong>
Vous pouvez également <a href="https://support.kobotoolbox.org/fr/qualitative_analysis.html#adding-hints-to-analysis-questions">ajouter des indices</a> aux questions d'analyse ou aux choix de réponse, par exemple pour inclure des informations issues d'un livre de codes ou des instructions destinées aux codeurs.
</p>

### Types de questions d'analyse

Les types de questions suivants sont disponibles pour les questions d'analyse :

| Type de question | Description |
|:----|:----|
| <i class="k-icon k-icon-tag"></i> Tags | Ajoutez des mots-clés ou des thèmes pour décrire la réponse audio. |
| <i class="k-icon-qt-text"></i> Texte | Ajoutez une réponse textuelle libre, telle qu'un résumé, des notes ou une impression générale. |
| <i class="k-icon-qt-number "></i> Chiffre | Enregistrez un nombre, par exemple le nombre de fois qu'un thème est mentionné. |
| <i class="k-icon-qt-select-one"></i> Choix unique | Sélectionnez une option dans une liste, par exemple le thème principal ou le niveau de satisfaction perçu. |
| <i class="k-icon-qt-select-many"></i> Choix multiple | Sélectionnez une ou plusieurs options dans une liste, par exemple les thèmes ou les obstacles mentionnés dans la réponse. |
| <i class="k-icon-qt-note"></i> Note | Ajoutez des instructions ou des intitulés de section pour organiser l'espace de travail d'analyse. |

Chaque champ que vous ajoutez devient une nouvelle colonne dans votre base de données lors du téléchargement de vos données, à l'exception des champs **Note**.

<p class="note">
<strong>Note :</strong>
   L'analyse automatisée ne peut pas être utilisée avec les questions d'analyse de type <strong>Tags</strong>. Les tags ne peuvent être générés que manuellement.
</p>

### Ajouter des indices aux questions d'analyse

Les indices peuvent contribuer à rendre votre analyse plus cohérente, que les réponses soient examinées par des codeurs humains ou générées avec l'IA. Lors de la création des questions d'analyse, utilisez les indices pour expliquer comment chaque question doit être traitée.

Vous pouvez ajouter des indices aux questions d'analyse ainsi qu'aux choix de réponse.

Par exemple, vous pouvez utiliser les indices pour inclure :

- Un livre de codes ou un cadre de codage complet
- Des définitions pour les tags, catégories ou thèmes
- Des exemples d'application de chaque choix de réponse
- Des instructions pour traiter les réponses peu claires ou incomplètes
- Toute consigne que vous donneriez normalement à un codeur humain
- Des instructions de type invite pour l'analyse générée par l'IA

![Ajouter des indices](images/qualitative_analysis/hints.png)

Les indices peuvent être **particulièrement utiles lors de l'utilisation de l'IA**, car ils fournissent à l'IA davantage de contexte sur la manière d'interpréter la réponse audio et sur la façon dont l'analyse doit être structurée.

Les indices n'ont pas de limite de longueur, vous pouvez donc inclure des instructions détaillées si nécessaire. Nous recommandons de rédiger des indices clairs et précis afin qu'ils soient faciles à suivre, tant pour les membres de l'équipe que pour les outils d'IA.

<p class="note">
<strong>Note :</strong>
    Si vos indices sont très longs, par exemple des instructions détaillées pour des réponses générées par l'IA, vous pouvez désactiver le bouton <strong>Afficher les indices</strong> en haut de la fenêtre <strong>ANALYSE</strong> pour les masquer.
</p>

## Analyser vos données

Une fois les questions d'analyse créées, vous pouvez commencer à analyser les réponses manuellement ou utiliser l'IA pour générer une réponse :

- **Pour l'analyse manuelle :** Saisissez manuellement une réponse pour chaque question d'analyse.
- **Pour l'analyse automatisée :** Cliquez sur <i class="k-icon k-icon-sparkles"></i> **Générer avec l'IA** sous chaque question d'analyse.

Après avoir généré des réponses d'analyse automatisées, vous pouvez les examiner et les modifier si nécessaire.

![Générer une analyse avec l'IA](images/qualitative_analysis/generate.png)

<p class="note">
<strong>Note :</strong>
Une réponse générée par l'IA sera accompagnée de la mention <i class="k-icon k-icon-sparkles"></i> <strong>Généré par l'IA</strong> sous la question.
</p>

### Examiner et vérifier les réponses

Pour l'analyse manuelle comme pour l'analyse générée par l'IA, vous pouvez examiner chaque réponse et la marquer comme vérifiée. Cela peut faciliter le contrôle qualité, que vous vérifiiez le codage au sein d'une équipe ou que vous confirmiez l'exactitude d'une réponse générée par l'IA.

Pour vérifier une réponse, cochez la case **Vérifié** en dessous. Si vous laissez la case décochée, le résultat de l'analyse sera tout de même enregistré, mais votre équipe pourra voir qu'il n'a pas encore été examiné.

![Vérifier l'analyse](images/qualitative_analysis/verify.png)

### Consulter et exporter les données d'analyse

Lorsque vous avez terminé l'analyse de vos fichiers audio, chaque champ d'analyse est enregistré sous forme de nouvelle colonne dans votre base de données. Votre base de données inclura également une colonne **Vérifié** avec les valeurs **Oui** ou **Non**.

![Tableau de données](images/qualitative_analysis/data_table.png)

Vous pouvez [exporter](https://support.kobotoolbox.org/fr/export_download.html) vos données avec ces champs d'analyse pour un examen approfondi, une synthèse ou la production de rapports. Par exemple, vous pouvez les utiliser pour suivre la fréquence d'apparition de thèmes spécifiques dans vos transcriptions, ou pour créer un livre de codes basé sur les **Tags** les plus récurrents.

<p class="note">
<strong>Note :</strong>
Lors de l'export de vos données, une colonne supplémentaire est incluse pour indiquer la <strong>source de l'analyse</strong>, précisant si l'analyse a été effectuée manuellement ou générée par l'IA.
</p>

### Personnaliser les paramètres d'affichage

Par défaut, le panneau d'affichage situé à droite de l'écran **ANALYSE** affiche l'enregistrement audio, la transcription originale et les réponses aux autres questions.

Vous pouvez modifier l'affichage pour inclure les informations qui correspondent le mieux à votre analyse. Par exemple, si vous travaillez dans plusieurs langues, vous pouvez afficher une [traduction](https://support.kobotoolbox.org/fr/transcription-translation.html) ou masquer la transcription originale.

Pour modifier l'affichage :

1. Cliquez sur **Paramètres d'affichage** en haut à droite.
2. Sélectionnez les informations que vous souhaitez afficher.

![Paramètres d'affichage](images/qualitative_analysis/display.png)

Vous pouvez choisir d'afficher ou de masquer :

- L'enregistrement audio
- Les réponses aux autres questions du formulaire
- La transcription originale
- Les traductions de la transcription

Si l'enregistrement n'a pas été transcrit, seuls l'enregistrement audio et les données de soumission seront disponibles.

<p class="note">
<strong>Note :</strong>
Pour en savoir plus sur la transcription et la traduction des réponses audio dans KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/transcription-translation.html#">Transcription et traduction de réponses audio</a>.
</p>

### Passer à une autre question ou transcription

Vous ne pouvez analyser qu'une seule réponse audio à la fois, mais vous pouvez naviguer facilement entre les réponses et les questions.

Pour passer à la soumission suivante ou précédente, utilisez les flèches situées à gauche du bouton **TERMINÉ**.

![Changer de soumission](images/qualitative_analysis/switch_submission.png)

Pour passer à une autre question audio au sein de la même soumission, utilisez le menu déroulant en haut de l'écran et sélectionnez la question que vous souhaitez analyser. Vous pourrez ajouter de **nouvelles questions d'analyse** pour cette question audio.

![Changer de question](images/qualitative_analysis/switch_question.png)

## Limites d'utilisation pour l'analyse générée par l'IA

Les utilisateurs du plan Community peuvent effectuer jusqu'à 25 demandes d'analyse générée par l'IA gratuitement. Chaque fois que vous cliquez sur <i class="k-icon k-icon-sparkles"></i> **Générer avec l'IA**, cela compte comme une demande. Les limites suivantes s'appliquent aux plans KoboToolbox payants :

| Plan | Limites |
|:---|:---|
| Professional | 1 000 demandes d'analyse |
| Teams | 2 000 demandes d'analyse |
| Enterprise | 30 000 demandes d'analyse |

Si vous avez besoin de davantage de demandes d'analyse générée par l'IA, vous pouvez [passer à une offre supérieure](https://www.kobotoolbox.org/pricing/) avec un quota plus élevé ou [acheter](https://support.kobotoolbox.org/fr/account_settings.html#add-ons) un **module complémentaire de demandes d'analyse automatique**. Les modules complémentaires sont disponibles selon vos besoins en analyse de données, à partir de 15 $ pour 2 000 demandes supplémentaires. Vous pouvez toujours continuer à utiliser les fonctionnalités d'analyse manuelle sans limite d'utilisation.

## Confidentialité des données et entraînement des modèles

Afin de garantir la confidentialité et la fiabilité lors de l'analyse de transcriptions d'entretiens ouverts, KoboToolbox héberge de manière sécurisée un modèle d'IA open source (**gpt-oss-120b**) dans son propre environnement serveur, plutôt que d'envoyer les données à un fournisseur d'IA commercial. Vos données ne sont **jamais partagées avec une entreprise d'IA tierce externe**, et vous conservez un contrôle total sur vos informations.

Les modèles open source offrent une plus grande transparence sur la façon dont les données sont traitées. Les transcriptions soumises à l'analyse ne sont **jamais utilisées pour entraîner, conserver ou améliorer** le modèle d'IA sous-jacent.

Par rapport aux fournisseurs d'IA commerciaux, qui mettent fréquemment à jour leurs modèles en arrière-plan et peuvent appliquer des filtres susceptibles d'affecter l'analyse de sujets complexes ou sensibles, **les modèles open source offrent une plus grande stabilité et cohérence** tout au long du cycle de vie d'un projet. Cela contribue à fournir une base plus neutre et prévisible pour la recherche qualitative.

Nos fonctionnalités d'analyse par IA ont été largement testées en comparaison avec des codeurs humains et plus de 40 modèles d'IA commerciaux et open-weight, afin de garantir des résultats de haute qualité et fiables.