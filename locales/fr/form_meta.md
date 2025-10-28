# Paramètres et métadonnées du formulaire
<a href="../form_meta.html">Read in English</a> | <a href="../es/form_meta.html">Leer en español</a> | <a href="../ar/form_meta.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/86f7750dca7b9470d220501253fb365b38924706/source/form_meta.md" class="reference">24 Sep 2025</a>

Dans l'interface de création de formulaires, vous pouvez définir un certain nombre de configurations optionnelles pour votre projet. Vous pouvez y accéder en cliquant sur le bouton **Mise en page et paramètres**.

![Form meta](/images/form_meta/form_meta.png)

## Style de formulaire

Vous pouvez modifier l'apparence du formulaire dans les formulaires Web Enketo, par exemple en plusieurs pages, avec un thème de grille, etc., dans le menu déroulant **Styles de formulaire**. Pour en savoir plus sur les différents styles de formulaire, consultez [cette page](alternative_enketo.md).

## Métadonnées du formulaire

Les métadonnées sont des questions cachées qui peuvent faciliter l'analyse des données et être utilisées à des fins d'audit et d'intégrité des données. Les métadonnées sont capturées en arrière-plan pendant le processus normal de collecte de données :

| Métadonnées      | Description                                                                                                                                                                    |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Start Time       | Date et heure d'ouverture du formulaire (horodatage)                                                                                                                           |
| End Time         | Date et heure de finalisation du formulaire (bouton « Soumettre » pressé)                                                                                                      |
| Today            | La date de soumission du formulaire                                                                                                                                            |
| Username         | Le nom d'utilisateur de l'enquêtrice ou enquêteur si [l'authentification est utilisée](managing_permissions.md#requiring-passwords-for-accessing-enketo-web-forms) pour la collecte de données |
| Audit            | Enregistrer un journal d'audit pendant que le formulaire est en cours de remplissage. Pour en savoir plus sur la journalisation d'audit, consultez [cette page](audit_logging.md) |
| Background Audio | Enregistrer l'audio en arrière-plan                                                                                                                                            |
| Device ID        | IMEI (International Mobile Equipment Identity)                                                                                                                                 |
| Phone Number\*   | Le numéro de téléphone portable de l'appareil de collecte de données                                                                                                           |

<p class="note">
  La métadonnée Phone Number n'est capturée que sur les appareils mobiles équipés d'une carte SIM.
</p>

### Ajouter des métadonnées de formulaire dans XLSForm

Si vous créez votre formulaire dans XLSForm, vous pouvez ajouter des métadonnées comme suit :

| type             | name             |
| :--------------- | :--------------- |
| start            | start            |
| end              | end              |
| today            | today            |
| username         | username         |
| audit            | audit            |
| background-audio | background_audio |
| deviceid         | deviceid         |
| phonenumber      | phonenumber      |
| survey           |                  |

<p class="note">
  Aucune étiquette n'est requise car les questions ne sont pas visibles dans le formulaire lui-même pendant la collecte de données
</p>

## Audio en arrière-plan

Lorsque le paramètre « Audio en arrière-plan » est activé, l'audio sera enregistré pendant que le formulaire est ouvert. Pour en savoir plus sur l'enregistrement audio en arrière-plan, consultez [cette page](recording-interviews.md).

## Détails

Lors de la création d'un nouveau projet, vous avez la possibilité de définir la _description_, le _secteur_ et le _pays_ de votre projet. Vous pouvez également choisir de partager **anonymement** les informations sur le pays et le secteur avec KoboToolbox dans le but d'améliorer la plateforme. Vous pouvez ajouter ou modifier ces détails dans le volet **Mise en page et paramètres** de l'interface de création de formulaires ou dans l'onglet **PARAMÈTRES>Général**.

## Paramètres supplémentaires

Outre les options disponibles dans l'onglet **Mise en page et paramètres** de l'interface de création de formulaires, vous pouvez également modifier d'autres paramètres au niveau du projet, tels que le [partage](managing_permissions.md), les [projets connectés](dynamic_data_attachment.md), les [services REST](rest_services.md) et les [médias](media.md), et plus encore.

<p class="note">
  Vous pouvez télécharger un XLSForm avec des exemples de cet article
  <a
    download
    class="reference"
    href="./_static/files/form_meta/form_meta.xlsx"
    >ici</a
  >.
</p>