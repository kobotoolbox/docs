# Ajouter des métadonnées dans le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/form_meta.md" class="reference">23 avr. 2026</a>

Les questions de métadonnées collectent automatiquement des informations sur le processus de collecte de données, telles que la date, l'heure et l'appareil utilisé, sans nécessiter de saisie de la part du répondant. Vous pouvez également enregistrer de l'audio en arrière-plan pendant la collecte de données.

Les questions de métadonnées sont **masquées aux répondants**, et **les champs de métadonnées ne peuvent pas être modifiés** dans le tableau de données KoboToolbox. Ces informations de contexte facilitent l'audit, contribuent à l'intégrité des données et peuvent être utilisées dans l'analyse des données.

Cet article explique comment ajouter et gérer des questions de métadonnées dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, présente les options de métadonnées disponibles, et décrit comment le suivi d'activité et l'enregistrement audio en arrière-plan peuvent contribuer à la qualité des données et au suivi pendant la collecte de données.

## Ajouter des questions de métadonnées dans le Formbuilder

Pour ajouter des questions de métadonnées dans le Formbuilder :

1. Cliquez sur <i class="k-icon-settings"></i> **Mise en page & Paramètres** en haut à droite de l'écran.
2. Dans la section **Métadonnées**, sélectionnez les questions de métadonnées que vous souhaitez inclure dans votre formulaire.

![Métadonnées du formulaire](images/question_types/access.png)

Les questions de métadonnées disponibles dans le Formbuilder sont les suivantes :

| Métadonnées | Description |
|:---|:---|
| start time | Enregistre la date et l'heure exactes auxquelles une soumission est démarrée. |
| end time | Enregistre la date et l'heure auxquelles une soumission est finalisée. |
| today | Enregistre la date de la soumission. |
| audit | Capture un [journal détaillé](https://support.kobotoolbox.org/fr/form_meta.html#audit-metadata-question) du processus d'entretien, incluant l'heure de début, l'heure de fin, la localisation et les actions de l'utilisateur pendant l'ensemble du processus de collecte de données. Cette question de métadonnées n'est pas disponible dans les formulaires web. |
| username | Dans KoboCollect, enregistre le nom d'utilisateur sauvegardé dans les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#user-and-device-identity-settings">paramètres de l'application KoboCollect</a>. Si aucun nom d'utilisateur n'est défini, c'est celui utilisé pour se connecter au serveur qui est enregistré.<br>Lors de l'utilisation de formulaires web, le nom d'utilisateur du compte n'est enregistré que si <a href="https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication">l'authentification est requise</a>.<br><br><strong>Note :</strong> Étant donné que le champ <code>username</code> peut être modifié dans KoboCollect, il peut ne pas correspondre au compte utilisé pour s'authentifier auprès du serveur. Pour savoir quel compte a soumis les données, consultez le champ généré automatiquement <code>_submitted_by</code>. |
| phone number | Enregistre le numéro de téléphone sauvegardé dans les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#user-and-device-identity-settings">paramètres de l'application KoboCollect</a>. Cette question de métadonnées n'est pas disponible dans les formulaires web. |
| device id | Enregistre l'identifiant unique de l'appareil ou du navigateur utilisé pour collecter les données. L'identifiant de l'appareil est généré automatiquement et ne peut pas être modifié par les utilisateurs.<br><br><strong>Note :</strong> Dans KoboCollect, l'identifiant de l'appareil est mis à jour chaque fois que l'application est réinstallée sur un appareil. Dans les formulaires web, le <code>deviceid</code> est réinitialisé à chaque fois qu'une nouvelle fenêtre de navigateur est utilisée. |
| start geopoint early | Capture les coordonnées GPS lorsque le formulaire est ouvert pour la première fois. Peut être utilisé pour activer le GPS de l'appareil en avance afin que les questions GPS ultérieures puissent obtenir des relevés précis plus rapidement. |

<p class="note">
<strong>Note :</strong> Les métadonnées du formulaire sont différentes des <a href="https://support.kobotoolbox.org/fr/viewing_validating_data.html#system-generated-submission-fields">champs de soumission générés automatiquement</a>. Les métadonnées du formulaire doivent être activées lors du développement du formulaire pour être collectées, tandis que les champs de soumission générés automatiquement sont ajoutés automatiquement pour chaque soumission.
</p>

## La question de métadonnées audit

La question de métadonnées audit enregistre un journal détaillé du processus d'entretien pendant qu'un formulaire est rempli dans l'[application Android KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html). Elle capture des informations telles que le moment où le formulaire a été ouvert et sauvegardé, les questions qui ont été consultées, le temps passé par les répondants sur chaque écran, et d'autres actions de l'utilisateur pendant la collecte de données.

Le suivi d'activité peut aider à :

- Surveiller le comportement des enquêteurs
- Identifier les questions qui prennent plus de temps à répondre
- Comprendre comment les enquêteurs naviguent dans un formulaire
- Soutenir les processus d'assurance qualité et de validation des données

Les journaux d'audit sont sauvegardés sous forme de fichiers CSV et importés avec chaque soumission. Ces fichiers peuvent être téléchargés en tant que pièces jointes multimédias et analysés séparément. Étant donné que les journaux utilisent des données d'horodatage, un traitement supplémentaire est généralement nécessaire pour l'analyse.

<p class="note">
    Pour plus d'informations sur les fichiers CSV exportés, consultez la <a href="https://docs.getodk.org/form-audit-log/">documentation complète sur le suivi d'activité ODK</a>.
</p>

La question de métadonnées audit n'est pas disponible dans les [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html).

### Paramètres d'audit

Des paramètres optionnels supplémentaires peuvent être configurés pour la question de métadonnées audit. Ceux-ci incluent :

- L'ajout de la localisation GPS des événements
- L'activation du suivi des modifications pour enregistrer les réponses modifiées après la sauvegarde d'un formulaire et avant sa soumission
- L'invitation des enquêteurs à indiquer la raison de la modification d'un formulaire sauvegardé
- L'obligation pour les enquêteurs de saisir leur nom d'utilisateur avant de remplir ou de modifier un formulaire

Les paramètres disponibles sont répertoriés dans la [documentation sur le suivi d'activité ODK](https://docs.getodk.org/form-audit-log/) sous forme de paramètres. Dans le Formbuilder, saisissez les paramètres optionnels directement dans la zone de texte **Paramètres d'audit**.

![Paramètres d'audit](images/question_types/audit_settings.png)

## Activer l'enregistrement audio en arrière-plan

L'enregistrement audio en arrière-plan vous permet de capturer un enregistrement audio pendant qu'un formulaire est ouvert et en cours de remplissage. L'enregistrement est sauvegardé dans le cadre de la soumission du formulaire et peut ensuite être [téléchargé sous forme de fichier audio](https://support.kobotoolbox.org/fr/managing_media_responses.html#downloading-media-files).

<p class="note">
<strong>Note :</strong> Avant d'utiliser cette fonctionnalité, assurez-vous que votre appareil dispose d'un espace de stockage suffisant pour les fichiers audio. Vous devez également obtenir le <strong>consentement éclairé</strong> des répondants avant d'effectuer un enregistrement. Tenez toujours compte des implications éthiques et respectez les lois applicables en matière de protection des données dans votre domaine de travail.
</p>

Pour activer l'enregistrement audio en arrière-plan dans le Formbuilder :

1. Ouvrez le panneau **Mise en page & Paramètres**.
3. Dans la section **Audio d'arrière-plan**, cliquez sur « Activer l'enregistrement audio en arrière-plan ».
    - Une fois activé, le texte du bouton deviendra « L'enquête sera enregistrée ».
4. Si nécessaire, modifiez la qualité audio dans le menu déroulant **Qualité sonore**.
    - Pour un aperçu des paramètres de qualité audio, consultez [Configurer la qualité audio](#configuring-audio-quality). **Voix uniquement** est la qualité audio par défaut et la plus basse.
5. Une fois activé, l'audio sera enregistré en arrière-plan dans KoboCollect et dans les formulaires web pendant que le formulaire est rempli.

![Activation de l'enregistrement audio en arrière-plan](images/recording_interviews/background_audio.png)

<p class="note">
Pour plus d'informations, consultez <a href="https://support.kobotoolbox.org/fr/recording-interviews.html#recording-interviews-with-background-audio-recordings">Collecter des données qualitatives avec KoboToolbox</a>.
</p>

### Configurer la qualité audio

La qualité audio influe sur la taille du fichier stocké sur le serveur. Les utilisateurs du [plan Community](https://www.kobotoolbox.org/pricing/) disposent d'1 Go de stockage de fichiers gratuit. Il est donc conseillé de gérer la taille des fichiers audio collectés en choisissant un paramètre de qualité approprié. Le tableau ci-dessous présente un aperçu des paramètres de qualité audio et des tailles de fichiers correspondantes.

| Qualité      | Extension | Encodage | Débit binaire | Fréquence d'échantillonnage | Taille du fichier |
|:------------ |:---------|:--------|:-----------|:------------|:---------------|
| Normale       | .m4a     | AAC     | 64 kbps    | 32 kHz      | ~ 30 Mo/heure    |
| Basse          | .m4a     | AAC     | 24 kbps    | 32 kHz      | ~ 11 Mo/heure    |
| Voix uniquement   | .amr     | AMR     | 12,2 kbps  | 8 kHz       | ~ 5 Mo/heure     |

Le paramètre par défaut **Voix uniquement** convient aux entretiens dans des environnements calmes. Pour les enregistrements avec plusieurs interlocuteurs ou un certain bruit de fond, le paramètre de qualité **Basse** est plus approprié. Le paramètre **Normale** offre la meilleure qualité audio mais utilise le plus d'espace de stockage.

## Configurer les métadonnées dans KoboCollect

Le numéro de téléphone et le nom d'utilisateur par défaut peuvent être [configurés](https://support.kobotoolbox.org/fr/kobocollect_settings.html#user-and-device-identity-settings) et modifiés dans l'application KoboCollect.

Pour configurer les métadonnées utilisateur dans KoboCollect :

1. Ouvrez l'application KoboCollect.
2. Appuyez sur l'**icône du projet** en haut à droite de votre écran.
3. Appuyez sur **Paramètres**.
4. Faites défiler jusqu'à **Identité de l'utilisateur et de l'appareil**, puis **Métadonnées du formulaire**.
5. Saisissez le nom d'utilisateur et/ou le numéro de téléphone. Vous pouvez également consulter l'identifiant actuel de l'appareil.