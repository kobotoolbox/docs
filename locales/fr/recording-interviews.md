# Collecter des données qualitatives avec KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/recording-interviews.md" class="reference">23 avr. 2026</a>

Les données qualitatives vous aident à **comprendre les expériences, les priorités et le contexte** que les questions fermées peuvent manquer. Elles peuvent révéler pourquoi les personnes répondent d'une certaine manière, comment elles décrivent leurs besoins et quels détails sont les plus importants dans un contexte local.

En pratique, les données qualitatives sont souvent plus difficiles à collecter et à analyser à grande échelle. Écrire des réponses ouvertes, examiner des images et transcrire des entretiens audio peut prendre beaucoup de temps. Pour cette raison, les équipes collectent souvent moins de données qualitatives qu'elles ne le souhaiteraient, ou ont du mal à utiliser tout ce qu'elles collectent.

KoboToolbox inclut des fonctionnalités qui **rendent la collecte de données qualitatives plus pratique.** Vous pouvez collecter du texte, des images, de l'audio, de la vidéo et des enregistrements audio d'arrière-plan dans vos formulaires, puis les examiner et les gérer directement dans KoboToolbox. Pour les réponses audio, KoboToolbox inclut également des outils intégrés pour la [transcription, la traduction](https://support.kobotoolbox.org/fr/transcription-translation.html) et l'[analyse](https://support.kobotoolbox.org/fr/qualitative_analysis.html).

Cet article couvre les principales façons de collecter des données qualitatives avec KoboToolbox, y compris les types de questions pertinents, les enregistrements audio d'arrière-plan et les options de gestion et d'analyse des données qualitatives après la collecte.

## Types de questions pour la collecte de données qualitatives

KoboToolbox prend en charge plusieurs types de questions utiles pour la recherche qualitative et la collecte de données ouvertes.

- **Texte :** Les questions de type texte peuvent être utilisées pour des réponses écrites courtes ou longues. Pour des réponses plus longues, vous pouvez utiliser l'[apparence](https://support.kobotoolbox.org/fr/text_questions.html#advanced-appearances) `multiline` (multiligne) pour offrir aux répondants une zone de texte plus grande.
- **Image :** Les questions de type image peuvent être utilisées pour collecter des photos, des croquis ou des images annotées. Cela peut être utile pour la documentation visuelle, la cartographie participative, les observations de sites ou la collecte de preuves photographiques. Utilisez l'[apparence](https://support.kobotoolbox.org/fr/photo_audio_video_file.html#advanced-appearances) `draw` (dessin) avec les questions de type image pour créer un dessin, et utilisez l'apparence `annotate` (annotation) pour annoter une image.
- **Vidéo :** Les questions de type vidéo peuvent être utilisées pour collecter des fichiers vidéo. Cela peut être utile lorsque le contexte visuel, le mouvement ou les démonstrations sont importants.
- **Audio :** Les questions de type audio permettent aux répondants ou aux enquêteurs d'enregistrer des réponses orales ou d'importer des fichiers audio. Elles sont utiles pour les entretiens ouverts et d'autres cas où le ton et la formulation exacte sont importants, et elles réduisent le besoin pour les enquêteurs de résumer les réponses sur le moment.
- **Enregistrement audio d'arrière-plan :** L'enregistrement audio d'arrière-plan capture l'audio en continu pendant que le formulaire est ouvert. Cela peut être utile pour enregistrer un entretien complet au lieu d'enregistrer des réponses séparées question par question.

<p class="note">
Pour en savoir plus sur les types de questions qualitatives, consultez <a href="https://support.kobotoolbox.org/fr/text_questions.html">Questions de type texte dans KoboToolbox</a>, <a href="https://support.kobotoolbox.org/fr/photo_audio_video_file.html#">Questions multimédias dans KoboToolbox</a> et <a href="https://support.kobotoolbox.org/fr/form_meta.html#enabling-background-audio-recording">Activer l'enregistrement audio d'arrière-plan</a>.
</p>

## Collecter des données qualitatives avec KoboCollect ou des formulaires web

Les types de questions qualitatives peuvent se comporter différemment selon que les données sont collectées dans [KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html) ou dans des [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html), et selon que les répondants utilisent un ordinateur ou un appareil mobile.

Le tableau suivant décrit le comportement de chaque type de question qualitative dans KoboCollect et dans les formulaires web.

| Type de question | Comportement dans KoboCollect | Comportement dans les formulaires web |
|:---|:---|:---|
| Texte | Les répondants peuvent saisir leur réponse dans une zone de texte. | Les répondants peuvent saisir leur réponse dans une zone de texte. |
| Image | Les répondants peuvent prendre des photos depuis l'appareil ou importer un fichier image. | Sur un ordinateur, les répondants peuvent **uniquement importer** un fichier image.<br><br>Lors de l'utilisation d'appareils mobiles, les répondants peuvent également avoir la possibilité de prendre une photo depuis l'appareil. |
| Vidéo | Les répondants peuvent enregistrer une vidéo depuis l'appareil ou importer un fichier vidéo. | Sur un ordinateur, les répondants peuvent **uniquement importer** un fichier vidéo.<br><br>Lors de l'utilisation d'appareils mobiles, les répondants peuvent également avoir la possibilité d'enregistrer une vidéo depuis l'appareil. |
| Audio | Les répondants peuvent enregistrer une réponse audio ou importer un fichier audio. | Les répondants peuvent enregistrer une réponse audio (même depuis un ordinateur) ou importer un fichier audio. |
| Enregistrement audio d'arrière-plan | Enregistre en continu pendant que le formulaire est ouvert, tant que l'autorisation d'enregistrer a été accordée. | Enregistre en continu pendant que le formulaire est ouvert (même depuis un ordinateur), tant que l'autorisation d'enregistrer a été accordée. |

<p class="note">
<strong>Remarque :</strong>
Lorsque l'enregistrement audio d'arrière-plan est actif sur un formulaire, les questions de type <strong>Audio</strong> dans <strong>KoboCollect</strong> sont désactivées, car il n'est pas possible d'enregistrer de l'audio en utilisant les deux fonctionnalités simultanément.
</p>

## Enregistrer des entretiens avec des enregistrements audio d'arrière-plan

L'enregistrement audio d'arrière-plan est utile lorsque vous souhaitez **capturer un entretien complet** plutôt que des clips audio séparés pour des questions individuelles. Il commence lorsque le formulaire s'ouvre et continue jusqu'à ce que le formulaire soit fermé.

L'audio d'arrière-plan peut être enregistré dans l'application KoboCollect et dans les formulaires web.

- Dans les formulaires web, un avertissement apparaît au début du formulaire pour informer les répondants que l'audio d'arrière-plan est en cours d'enregistrement.
- Dans les formulaires web et dans KoboCollect, une icône de microphone apparaît en haut du formulaire pendant que l'enregistrement est actif et affiche la durée de l'enregistrement.

<p class="note">
<strong>Remarque :</strong>
L'enregistrement audio d'arrière-plan est collecté en tant que métadonnées de formulaire. Pour plus d'informations sur la configuration des enregistrements audio d'arrière-plan dans votre formulaire, consultez <a href="https://support.kobotoolbox.org/fr/form_meta.html#enabling-background-audio-recording">Ajouter des métadonnées dans le Formbuilder</a> ou <a href="https://support.kobotoolbox.org/fr/metadata_xls.html">Métadonnées de formulaires dans XLSForm</a>.
</p>

### Considérations éthiques pour l'enregistrement audio

Avant d'enregistrer de l'audio, **assurez-vous que les répondants donnent leur consentement éclairé.** Ils doivent comprendre que l'audio est enregistré, pourquoi il est collecté, comment il sera utilisé, qui y aura accès et combien de temps il sera conservé.

Les données audio peuvent être particulièrement sensibles. Avant d'utiliser l'enregistrement audio d'arrière-plan, déterminez si les enregistrements d'entretiens complets sont nécessaires pour votre projet et s'ils créent des **risques supplémentaires en matière de confidentialité ou de protection.** Kobo encourage fortement le respect de toutes les exigences applicables en matière de protection des données et de confidentialité dans le lieu où la collecte de données a lieu.

## Gérer et analyser les données qualitatives

KoboToolbox inclut des fonctionnalités intégrées pour vous aider à examiner les données qualitatives après la collecte.

- **Texte :** Vous pouvez examiner toutes les réponses à une question de type texte dans **DONNÉES > Rapports.** Cela est utile pour lire rapidement les réponses ouvertes ensemble et repérer les thèmes communs.
- **Images :** Vous pouvez examiner les images collectées dans **DONNÉES > Galerie Photo.** Cela facilite la navigation parmi les réponses visuelles dans les soumissions.
- **Vidéo :** Les fichiers vidéo peuvent être visualisés dans les soumissions individuelles. Cela est utile lorsque vous devez examiner le contexte visuel parallèlement à d'autres réponses du même formulaire.
- **Audio :** Les réponses audio, y compris les enregistrements audio d'arrière-plan, peuvent être ouvertes dans leur propre vue pour examen, transcription, traduction et analyse.

<p class="note">
Pour en savoir plus sur la transcription, la traduction et l'analyse des réponses audio, consultez <a href="https://support.kobotoolbox.org/fr/transcription-translation.html">Transcription et traduction de réponses audio</a> et <a href="https://support.kobotoolbox.org/fr/qualitative_analysis.html">Analyse qualitative des réponses audio</a>.
</p>

Les données qualitatives sont incluses dans votre base de données lorsque vous l'[exportez](https://support.kobotoolbox.org/fr/export_download.html), y compris les liens vers les fichiers multimédias pour chaque soumission, toutes les données de transcription, de traduction et d'analyse, et toutes les réponses textuelles. Les fichiers multimédias peuvent également être [téléchargés séparément](https://support.kobotoolbox.org/fr/managing_media_responses.html#downloading-media-files), individuellement ou en masse.

## Résolution de problèmes

<details>
  <summary><strong>Pas assez de stockage sur l'appareil</strong></summary>
Avant de collecter des données qualitatives (par exemple, des images ou des enregistrements audio d'arrière-plan), assurez-vous que votre appareil dispose de suffisamment d'espace de stockage pour enregistrer les fichiers.
</details>

<br>

<details>
  <summary><strong>Pas assez de stockage sur le serveur KoboToolbox</strong></summary>
Les fichiers multimédias peuvent être volumineux et peuvent entraîner le dépassement de la limite de stockage de votre compte (1 Go pour les comptes gratuits). Si vous avez besoin de plus d'espace, vous pouvez <a href="https://support.kobotoolbox.org/fr/managing_media_responses.html#deleting-media-files">supprimer les fichiers multimédias</a> des soumissions, <a href="https://www.kobotoolbox.org/pricing/">passer à une offre supérieure</a> ou acheter un <strong>supplément de stockage</strong> dans <strong>Paramètres du compte > Suppléments.</strong>
</details>

<br>

<details>
  <summary><strong>L'enregistrement audio d'arrière-plan ne fonctionne pas</strong></summary>
  Votre appareil doit disposer d'un enregistreur audio intégré pour que cette fonctionnalité fonctionne. Si votre appareil n'en possède pas, vous pouvez télécharger <a href="https://play.google.com/store/apps/details?id=com.media.bestrecorder.audiorecorder&pcampaignid=web_share">Voice Recorder</a> ou toute autre application d'enregistrement audio sur votre appareil.
</details>

<br>

<details>
  <summary><strong>Modification de soumissions avec enregistrement audio d'arrière-plan</strong></summary>
Si vous modifiez un formulaire qui inclut de l'audio d'arrière-plan depuis la plateforme KoboToolbox, l'enregistrement initial ne sera pas remplacé. Un message en haut du formulaire indiquera « Cette soumission contient un enregistrement audio d'arrière-plan. »
</details>

<br>

<details>
  <summary><strong>Formulaires avec enregistrement audio d'arrière-plan enregistrés comme brouillons</strong></summary>
Si un formulaire avec enregistrement audio d'arrière-plan est enregistré comme brouillon dans les <strong>formulaires web</strong>, seul l'enregistrement initial sera conservé. L'enregistrement ne reprendra pas et ne sera pas remplacé lorsque le brouillon sera rouvert. <br><br>
Si un formulaire avec enregistrement audio d'arrière-plan est enregistré comme brouillon dans <strong>KoboCollect</strong>, l'enregistrement reprendra lorsque le brouillon sera rouvert. Les deux enregistrements seront stockés ensemble dans un seul fichier.
</details>

<br>