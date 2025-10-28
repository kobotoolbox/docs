# Enregistrer une interview complète avec l'enregistrement audio en arrière-plan
<a href="../recording-interviews.html">Read in English</a> | <a href="../es/recording-interviews.html">Leer en español</a> | <a href="../ar/recording-interviews.html">اقرأ باللغة العربية</a>

**Dernière mise à jour :**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/recording-interviews.md" class="reference">15
fév. 2022</a>

**L'enregistrement audio en arrière-plan** est une fonctionnalité puissante qui permet aux utilisatrices et utilisateurs d'enregistrer une interview en arrière-plan (lorsque le formulaire est ouvert) et de stocker l'enregistrement sous forme de données audio. Cette fonctionnalité améliore la collecte de données qualitatives en permettant de collecter des informations nuancées dans leur intégralité.

L'enregistrement audio en arrière-plan permet également aux superviseurs et aux chefs de projet de savoir comment leurs enquêteurs ont mené l'interview en termes d'assurance qualité des données ou s'ils souhaitent avoir un enregistrement de sauvegarde de l'interview transcrite.

Actuellement, les utilisatrices et utilisateurs peuvent enregistrer l'interview complète avec **l'application Android Collect** `v1.30` et versions ultérieures. **Enketo** ne prend pas encore en charge cette fonctionnalité.

<p class="note">
  Si vous avez besoin d'un enregistrement audio au lieu de l'<strong>enregistrement audio en arrière-plan</strong> complet, consultez notre article d'aide,
  <a class="reference" href="media.html"
    >Ajouter différents types de médias (image, audio, vidéo) à un formulaire</a
  >.
</p>

## Activer l'enregistrement audio en arrière-plan dans l'interface de création de formulaires

Si vous concevez votre formulaire d'enquête via l'interface de création de formulaires et souhaitez activer **l'enregistrement audio en arrière-plan**, suivez les étapes présentées dans la vidéo ci-dessous :

<video controls>
  <source
    src="./_static/files/recording_interviews/activating_background_audio_recording_UI.mp4"
    type="video/mp4"
  />
</video>

-   Sous **FORMULAIRE**, sélectionnez le bouton **Modifier**. _(Cette étape peut ne pas être nécessaire si vous êtes déjà dans l'interface de création de formulaires)_
-   Dans le coin supérieur droit, sélectionnez **Mise en page et paramètres**, puis **Audio en arrière-plan** devrait être visible.
-   Activez le bouton **Activer l'enregistrement audio en arrière-plan**. Une notification devrait apparaître en haut de l'interface de création de formulaires.
-   **Voix uniquement** est la qualité audio par défaut pour **l'audio en arrière-plan**. Vous pouvez modifier la qualité audio en **Faible** ou **Normale** selon vos besoins (voir le tableau ci-dessous pour les différences de taille de fichier).
-   Après avoir effectué toutes les configurations nécessaires, sélectionnez **ENREGISTRER** et **Quitter** dans l'interface de création de formulaires.
-   **DÉPLOYEZ** le formulaire pour le mettre en ligne.

## Inclure le type de question audio en arrière-plan dans XLSForm

Si vous concevez votre formulaire d'enquête via XLSForm et souhaitez inclure un type de question `background-audio`, suivez les étapes présentées dans la vidéo ci-dessous :

<video controls>
  <source
    src="./_static/files/recording_interviews/including_background_audio_question_type_xlsform.mp4"
    type="video/mp4"
  />
</video>

Dans votre XLSForm, ajoutez `background-audio` sous la colonne `type` de la feuille **survey**. Il s'agit du type de question qui enregistrera l'audio en arrière-plan.

## Définir une qualité audio appropriée

La colonne `parameters` est facultative, mais il est important de choisir le paramètre approprié. La qualité audio est directement liée à la taille du fichier qui sera stocké sur le serveur. Gardez à l'esprit la part de votre espace de stockage total que vous souhaitez consacrer à vos fichiers audio. Référez-vous au tableau ci-dessous lors du choix du paramètre approprié :

| Qualité    | Paramètres         | Extension | Encodage | Débit binaire | Taux d'échantillonnage | Taille du fichier |
| :--------- | :----------------- | :-------- | :------- | :------------ | :--------------------- | :---------------- |
| normal     | quality=normal     | .m4a      | AAC      | 64 kbps       | 32 kHz                 | ~ 30 Mo/heure     |
| low        | quality=low        | .m4a      | AAC      | 24 kbps       | 32 kHz                 | ~ 11 Mo/heure     |
| voice-only | quality=voice-only | .amr      | AMR      | 12.2 kbps     | 8 kHz                  | ~ 5 Mo/heure      |

Vous pouvez laisser la colonne vide pour que le paramètre soit défini sur `voice-only`, ce qui capturera bien l'audio dans un cadre d'interview silencieux. Si vous enregistrez de l'audio où plusieurs personnes pourraient parler simultanément, `low` serait plus approprié. `normal` est l'option de la plus haute qualité et utilisera le plus d'espace de stockage.

## Collecter de l'audio en arrière-plan avec l'application Android Collect

Consultez notre article d'aide,
[Collecte de données sur l'application KoboCollect](kobocollect_on_android_latest.md), pour en savoir plus en détail sur la collecte de données avec **l'application Android Collect**.

<video controls>
  <source
    src="./_static/files/recording_interviews/collecting_data_with_background_audio_in_collect_app.mp4"
    type="video/mp4"
  />
</video>

Lors de l'enregistrement actif d'audio en arrière-plan avec **l'application Android Collect**, vous devriez pouvoir voir un microphone en haut de votre formulaire.

![Écran audio en arrière-plan](/images/recording_interviews/background_audio_screen.jpg)

## Visualiser les fichiers audio enregistrés en arrière-plan

Lorsque vous avez configuré `background-audio` pour votre projet, vous pouvez visualiser le fichier audio enregistré sous **DONNÉES>Tableau** comme indiqué dans l'image ci-dessous.

![Vue du tableau de données](/images/recording_interviews/data_table_view.png)

## Télécharger les fichiers audio

Vous pouvez télécharger tous les fichiers audio en arrière-plan sous forme de fichier ZIP depuis
**DONNÉES>Téléchargements>Pièces jointes multimédias (ZIP)** comme indiqué dans la vidéo ci-dessous.

<video controls>
  <source
    src="./_static/files/recording_interviews/downloading_audio_files_that_were_recorded_as_background_audio.mp4"
    type="video/mp4"
  />
</video>

## Considérations éthiques

Lors de la collecte de données, il est éthique d'obtenir le consentement éclairé des répondants à l'enquête avant la collecte de données, dans ce cas en enregistrant de l'audio en arrière-plan.

<p class="note">
  Nous encourageons toutes les utilisatrices et tous les utilisateurs à considérer les implications éthiques de leur collecte de données et à se conformer à la législation applicable en matière de protection des données dans la juridiction de leur travail.
</p>

## Dépannage

-   Cette fonctionnalité est prise en charge avec **l'application Android Collect** `v1.30` et versions ultérieures.
-   Cette fonctionnalité n'est actuellement pas prise en charge dans les **formulaires web Enketo**.
-   Votre appareil doit disposer d'un enregistreur audio intégré pour que cette fonctionnalité fonctionne correctement. Vous pouvez télécharger
    [Audio Recorder](https://play.google.com/store/apps/details?id=com.github.axet.audiorecorder)
    depuis Google Play Store si nécessaire.
-   Avant de commencer la collecte de données, assurez-vous que votre appareil dispose d'un espace suffisant pour stocker les enregistrements audio en arrière-plan.
-   Si vous modifiez votre fichier audio sous **Modifier le formulaire enregistré**, vous aurez les deux versions (le fichier audio original et le fichier modifié) dans un seul fichier. Par exemple, si vous avez un audio en arrière-plan de _'Test d'échantillon'_ et que vous avez modifié l'enregistrement en le changeant en _'Échantillon pour re-test'_, lorsque vous téléchargerez votre fichier audio en arrière-plan, il consistera en l'audio en arrière-plan combiné de _'Test d'échantillon'_ et _'Échantillon pour re-test'_.
-   Si vos fichiers audio en arrière-plan occupent suffisamment d'espace de stockage pour faire passer votre stockage total au-delà de votre quota alloué (5 Go pour tous les comptes gratuits), vous pouvez demander de l'espace supplémentaire (moyennant des frais) en contactant
    [info@kobotoolbox.org](mailto:info@kobotoolbox.org). Le paiement est utilisé pour couvrir les coûts supplémentaires associés aux grands projets de collecte de données et garantit que le serveur continue de bien fonctionner pour nos utilisatrices et utilisateurs.
-   Lorsque vous avez des fichiers audio en arrière-plan volumineux et/ou longs dans votre compte, vous pouvez rencontrer des problèmes pour les télécharger en tant que **Pièces jointes multimédias (ZIP)**. Dans ce cas, suivez notre article d'aide
    [Télécharger des photos et autres médias](photo_download.md), qui devrait vous aider à télécharger de gros fichiers multimédias depuis le système.