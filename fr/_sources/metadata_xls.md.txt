# Métadonnées de formulaires dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/metadata_xls.md" class="reference">23 Apr 2026</a>

Les questions de métadonnées collectent automatiquement des informations sur le processus de collecte de données, telles que la date, l'heure et l'appareil utilisé, sans nécessiter de saisie de la part du répondant. Vous pouvez également enregistrer de l'audio en arrière-plan pendant la collecte de données.

Les questions de métadonnées sont masquées pour les répondants, et les champs de métadonnées ne peuvent pas être modifiés dans le tableau de données KoboToolbox. Ces informations de contexte facilitent l'audit, contribuent à maintenir l'intégrité des données et peuvent être utilisées dans l'analyse des données.

<p class="note">
<strong>Note :</strong> Cet article porte sur l'ajout de questions de métadonnées dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de questions de métadonnées dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_meta.html">Ajouter des métadonnées dans le Formbuilder</a>.
</p>

## Ajouter des questions de métadonnées dans XLSForm

Les questions de métadonnées sont ajoutées dans XLSForm de la même manière que tout autre type de question :

1. Saisissez le `type` de la question de métadonnées dans une nouvelle ligne, en utilisant le nom exact indiqué [dans le tableau ci-dessous](https://support.kobotoolbox.org/fr/metadata_xls.html#available-metadata-questions-in-xlsform).
2. Indiquez un `name` pour la question.
3. Les libellés de questions ne sont pas obligatoires, car ils ne sont pas affichés dans le formulaire.

**onglet survey**

| type | name       | label        |
|:-----|:-----------|:-------------|
| start | start_time |              |
| end   | end_time   |              |
| survey |

## Questions de métadonnées disponibles dans XLSForm

Les questions de métadonnées disponibles dans XLSForm sont les suivantes :

| Type       | Description |
|:--------------------|:-------------|
| `start` | Enregistre la date et l'heure exactes auxquelles une soumission est démarrée. |
| `end` | Enregistre la date et l'heure auxquelles une soumission est finalisée. |
| `today` | Enregistre la date de la soumission. |
| `deviceid` | Enregistre l'identifiant unique de l'appareil ou du navigateur utilisé pour collecter les données. Le <code>deviceid</code> est généré automatiquement et ne peut pas être modifié par les utilisateurs.<br><br>**Note :** Dans KoboCollect, le <code>deviceid</code> est mis à jour chaque fois que l'application est réinstallée sur un appareil. Lors de l'utilisation de formulaires web, le <code>deviceid</code> est réinitialisé à chaque fois qu'une nouvelle fenêtre de navigateur est utilisée. |
| `username` | Dans KoboCollect, enregistre le nom d'utilisateur sauvegardé dans les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#user-and-device-identity-settings">paramètres de l'application KoboCollect</a>. Si aucun nom d'utilisateur n'est défini, le nom utilisé pour se connecter au serveur est enregistré.<br>Lors de l'utilisation de formulaires web, le nom d'utilisateur du compte n'est enregistré que si <a href="https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication">l'authentification est requise</a>.<br><br>**Note :** Le champ `username` pouvant être modifié dans KoboCollect, il peut ne pas correspondre au compte utilisé pour s'authentifier auprès du serveur. Pour savoir quel compte a soumis les données, référez-vous au champ `_submitted_by` généré automatiquement. |
| `phonenumber` | Enregistre le numéro de téléphone sauvegardé dans les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#user-and-device-identity-settings">paramètres de l'application KoboCollect</a>. Cette question de métadonnées n'est pas disponible dans les formulaires web. |
| `email` | Enregistre l'adresse email définie dans les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#user-and-device-identity-settings">paramètres de l'application KoboCollect</a>. Cette question de métadonnées n'est pas disponible dans les formulaires web. |
| `start-geopoint` | Capture les coordonnées GPS à la première ouverture du formulaire. Peut être utilisé pour initialiser le GPS de l'appareil afin que les questions GPS ultérieures puissent atteindre des relevés précis plus rapidement. |
| `background-geopoint` | Capture les coordonnées GPS lorsqu'une question spécifique reçoit une réponse. La question doit être spécifiée dans la colonne `trigger` de la question <code>background-geopoint</code>. |
| `background-audio` | Enregistre de l'audio en arrière-plan pendant qu'un formulaire est ouvert. Pour en savoir plus sur cette fonctionnalité, consultez l'article <a href="https://support.kobotoolbox.org/fr/recording-interviews.html#recording-interviews-with-background-audio-recordings">Collecter des données qualitatives avec KoboToolbox</a>. |
| `audit` | Capture un journal détaillé du processus d'entretien, incluant l'heure de début, l'heure de fin, la localisation et les actions de l'utilisateur pendant l'ensemble du processus de collecte de données. Cette question de métadonnées n'est pas prise en charge dans les formulaires web.<br><br>Pour en savoir plus sur l'utilisation de la question audit pour les journaux d'audit et la configuration des paramètres, consultez <a href="https://docs.getodk.org/form-audit-log/">Form Audit Log (ODK)</a>. |

<p class="note">
<strong>Note :</strong>
    Les métadonnées de formulaire sont différentes des <a href="https://support.kobotoolbox.org/fr/viewing_validating_data.html#system-generated-submission-fields">champs de soumission générés par le système</a>. Les métadonnées de formulaire doivent être activées lors du développement du formulaire pour être collectées, tandis que les champs de soumission générés par le système sont ajoutés automatiquement pour chaque soumission.
</p>

## Configurer les métadonnées dans KoboCollect

L'adresse email, le numéro de téléphone et le nom d'utilisateur par défaut peuvent être [configurés](https://support.kobotoolbox.org/fr/kobocollect_settings.html#user-and-device-identity-settings) et modifiés dans l'application KoboCollect :

1. Ouvrez l'application KoboCollect.
2. Appuyez sur l'**icône Projet** en haut à droite de votre écran.
3. Appuyez sur **Paramètres**.
4. Faites défiler jusqu'à **User and device identity**, puis **Form metadata**.
5. Saisissez le nom d'utilisateur, le numéro de téléphone et/ou l'adresse email. Vous pouvez également consulter l'identifiant de l'appareil actuel.

## Configurer la qualité audio des enregistrements audio en arrière-plan

Lors de l'enregistrement d'entretiens en arrière-plan, la qualité audio influe sur la taille du fichier stocké sur le serveur. Les utilisateurs du [plan Community](https://www.kobotoolbox.org/pricing/) disposent de 1 Go de stockage de fichiers gratuit. Il est donc conseillé de gérer la taille des fichiers audio collectés en choisissant un paramètre de qualité approprié.

Pour ajuster la qualité audio de votre enregistrement audio en arrière-plan :

1. Ajoutez une colonne `parameters` à votre XLSForm.
2. Dans la ligne `background-audio`, saisissez l'une des valeurs suivantes :
    - `quality=normal`
    - `quality=low`
    - `quality=voice-only`

**onglet survey**

| type             | name       | label | parameters       |
|:-----------------|:-----------|:------|:----------------|
| background-audio | recording  |       | quality=normal  |
| survey |

Le tableau ci-dessous présente un aperçu des paramètres de qualité audio et des tailles de fichiers correspondantes.

| Paramètre XLSForm   | Extension | Encodage | Débit binaire | Fréquence d'échantillonnage | Taille du fichier |
|:------------------  |:---------|:--------|:-------------|:---------------------------|:-----------------|
| quality=normal      | .m4a     | AAC     | 64 kbps      | 32 kHz                     | ~ 30 Mo/heure    |
| quality=low         | .m4a     | AAC     | 24 kbps      | 32 kHz                     | ~ 11 Mo/heure    |
| quality=voice-only  | .amr     | AMR     | 12,2 kbps    | 8 kHz                      | ~ 5 Mo/heure     |

Le paramètre par défaut `voice-only` convient aux entretiens dans des environnements calmes. Pour les enregistrements avec plusieurs interlocuteurs ou un certain bruit de fond, le paramètre de qualité `low` est plus approprié. Le paramètre `normal` offre la meilleure qualité audio, mais utilise le plus d'espace de stockage.