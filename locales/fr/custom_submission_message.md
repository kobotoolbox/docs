# Message de soumission personnalisé
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/22959ee8b91c5f4cb42545d225dec591a0d409c0/source/custom_submission_message.md" class="reference">29 Jul 2026</a>

Les messages de soumission personnalisés vous permettent d'afficher un message adapté après qu'un répondant a soumis un formulaire avec succès.

Les messages de soumission personnalisés peuvent être utilisés pour :

- **Confirmer des inscriptions à un événement :** Par exemple, pour confirmer une inscription, fournir les détails de l'événement et inclure un lien de téléchargement vers un calendrier.
- **Proposer des incentives conditionnels :** Pour afficher un message en fonction de l'éligibilité d'un répondant, comme un code de réduction ou un message de remerciement.
- **Faciliter les workflows de suivi :** Pour afficher un numéro de ticket, un récapitulatif des données soumises ou un lien vers l'étape suivante d'un processus.

Cette fonctionnalité doit être configurée dans [XLSForm](https://support.kobotoolbox.org/fr/getting_started_xlsform.html).

## Configurer un message de soumission personnalisé

Pour configurer un message de soumission personnalisé dans un XLSForm :

1. Dans l'**onglet settings**, ajoutez trois colonnes : `name`, `namespaces` et `attribute::kobo:submitMessage`
    - Dans la colonne `name`, saisissez `data`
    - Dans la colonne `namespaces`, saisissez `kobo="http://kobotoolbox.org/xforms"`
    - Dans la colonne `attribute::kobo:submitMessage`, saisissez `/data/submitMessage`.

**onglet settings**

| name | namespaces     | attribute::kobo:submitMessage              |
| :--- | :------- | :----------------- |
| text | kobo="http://kobotoolbox.org/xforms" | /data/submitMessage |
| settings |

2. Dans l'**onglet survey**, créez une question de type `calculate`.
    - Dans la colonne `name`, saisissez `submitMessage`
    - Dans la colonne `calculation`, saisissez le message de confirmation que vous souhaitez utiliser.

**onglet survey**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- |:------------|
| calculate | submitMessage |  | `"Thank you for registering. Click [here](http://kobotoolbox.org) for more information about the event."` |
| survey |

<p class="note">
  Pour un exemple de cette fonctionnalité en pratique, téléchargez un XLSForm type <a href="https://docs.google.com/spreadsheets/d/1CgjrpJcDX1pLmf-B-PUZ4-KFs2pPuntD/edit?usp=sharing&ouid=104272235398180261217&rtpof=true&sd=true">ici</a>.
</p>

## Personnaliser le message de soumission

Vous pouvez utiliser des fonctions et le format Markdown dans la colonne `calculation` pour personnaliser le message.

### Utiliser des instructions conditionnelles

Utilisez `if()` pour afficher différents messages en fonction des réponses au formulaire.

Par exemple : `if(${eligible} = 'yes', 'You are eligible.', 'You are not eligible.')`

### Afficher les libellés des choix

Utilisez `jr:choice-name()` pour afficher le [libellé](https://support.kobotoolbox.org/fr/glossary.html#label) d'un choix sélectionné plutôt que son [nom de choix](https://support.kobotoolbox.org/fr/glossary.html#choice-name).

Par exemple : `concat('You are registered for ', jr:choice-name(${event}, '${event}'))`

### Mettre en forme le message de soumission

Utilisez le format Markdown pour mettre en forme le message de soumission, par exemple avec des hyperliens, du texte en gras, du texte en italique ou des listes.

Par exemple : `'**Congratulations!** You are eligible. Click [here](http://kobotoolbox.org) for more information.'`

<p class="note">
  Pour plus d'informations sur la mise en forme du texte avec Markdown, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_style_xls.html#styling-text">Personnaliser vos formulaires à l'aide de XLSForm</a>.
</p>

## Créer des messages de soumission en plusieurs langues

Pour les formulaires multilingues, vous pouvez afficher le message de soumission dans la langue sélectionnée par le répondant.

Pour configurer des messages de soumission multilingues :

1. Dans l'**onglet survey**, créez une question de type `select_one` pour stocker le message.
2. Saisissez `false` dans la colonne `relevant` pour masquer la question dans le formulaire.
3. Dans l'**onglet choices**, ajoutez le message de soumission en tant que choix.
4. [Traduisez](https://support.kobotoolbox.org/fr/language_xls.html) le libellé du choix dans chaque langue du formulaire.
5. Dans la colonne `calculation` de la ligne `submitMessage`, saisissez : `jr:choice-name('choice_name', '${question_name}')`
    - `choice_name` est le nom du choix dans lequel votre message est stocké
    - `question_name` est le nom de la question `select_one` créée ci-dessus

Le message de soumission s'affichera dans la langue sélectionnée en haut du formulaire.

<p class="note">
  Pour un exemple de formulaire affichant un message de soumission en plusieurs langues, téléchargez un XLSForm type <a href="https://docs.google.com/spreadsheets/d/1NXwXbG6PaSFX1HZGEDMdji6XiUIHfkHG/edit?usp=sharing&rtpof=true&sd=true">ici</a>.
</p>

## Compatibilité

Les messages de soumission personnalisés sont destinés à être utilisés avec les [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html). Ils fonctionnent uniquement avec les [modes de collecte de données](https://support.kobotoolbox.org/fr/data_through_webforms.html#data-collection-modes) suivants :

- En ligne uniquement (soumission unique)
- En ligne uniquement (une fois par répondant)

Ils peuvent également apparaître dans [KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html), mais KoboCollect traite le message comme du texte brut, de sorte que la mise en forme Markdown et les liens ne sont pas affichés. Tenez compte de votre méthode de collecte de données et testez le message avant de commencer la collecte avec votre formulaire.