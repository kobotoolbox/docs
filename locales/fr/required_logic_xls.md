# Ajouter une logique d’obligation conditionnelle dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/required_logic_xls.md" class="reference">20 Mar 2026</a>

La logique d'obligation conditionnelle vous permet de rendre une question obligatoire si certaines conditions sont remplies. Par exemple, vous pouvez rendre obligatoire une question sur le numéro de téléphone uniquement si les répondants acceptent d'être recontactés à l'avenir. Cette option offre plus de contrôle que le simple fait de marquer une question comme toujours obligatoire ou toujours facultative.

<p class="note">
  Pour en savoir plus sur les questions obligatoires et sur la façon de personnaliser le message affiché aux répondants lorsqu'ils laissent une question obligatoire sans réponse, consultez l'article <a href="https://support.kobotoolbox.org/fr/question_options_xls.html#required-questions">Options de questions dans XLSForm</a>.
</p>

Cet article explique comment ajouter des conditions de logique d'obligation conditionnelle dans XLSForm, notamment comment rendre une question obligatoire selon qu'une autre question a reçu une réponse ou non.

<p class="note">
  <strong>Note :</strong> Cet article porte sur l'ajout d'une logique d'obligation conditionnelle dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout d'une logique d'obligation conditionnelle dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/question_options.html?highlight=custom+logic#mandatory-response">Options de questions dans le Formbuilder</a>.
  <br><br>
  Pour vous exercer à utiliser la logique d'obligation conditionnelle dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Ajouter des conditions de logique d'obligation conditionnelle

La logique d'obligation conditionnelle utilise le <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html#question-referencing">référencement de questions</a> pour rendre des questions obligatoires en fonction des réponses précédentes. La question utilisée pour définir la logique d'obligation conditionnelle est appelée la **question de référence**.

Pour ajouter une logique d'obligation conditionnelle dans XLSForm :
1. Ajoutez une colonne `required` à l'**onglet survey**.
2. Dans la ligne de la question pour laquelle vous souhaitez définir la logique d'obligation conditionnelle, saisissez la condition qui doit être remplie **pour que la question soit obligatoire**.

**onglet survey**

| type         | name      | label                                                                     | required           |
|:--------------|:-----------|:--------------------------------------------------------------------------|:------------------|
| select_one yn | recontact  | Do you agree to being contacted again for another study in the future?    |                    |
| text          | email      | What is your email address?                                               | ${recontact} = 'yes' |
| survey | 

Si un répondant ne répond pas à une question obligatoire, il ne pourra pas passer à la page suivante du formulaire ni le soumettre.

### Mettre en forme les conditions de logique d'obligation conditionnelle

Le format de la condition de logique d'obligation conditionnelle varie selon le **type de la question de référence**, comme indiqué dans le tableau ci-dessous.

| Type de la question de référence | Condition de logique d'obligation conditionnelle | Exemple |
|:-------------------------|:--------------------|:---------|
| select_one | `${reference_question} = 'choice_name'` | `${consent} = 'yes'` |
| select_multiple | `selected(${reference_question}, 'choice_name')` | `selected(${reasons}, 'other')` |
| integer | `${reference_question}` suivi d'un opérateur logique (>, <, =) et d'un nombre (ou d'une référence à une autre question) | `${age} >= 18` |
| date | `${reference_question}` suivi d'un opérateur logique (>, <, =) et de `date('YYYY-MM-DD')` | `${dob} >= date('1975-01-01')` |

<p class="note">
Pour en savoir plus sur la création d'expressions de logique de formulaire dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

## Ajouter une logique d'obligation conditionnelle selon qu'une question a reçu une réponse ou non

En plus de définir une logique d'obligation conditionnelle pour une réponse spécifique, vous pouvez également la baser sur le fait qu'une question a reçu une réponse ou a été laissée sans réponse. Cela est utile lorsque vous souhaitez vous assurer qu'au moins l'une de deux questions est obligatoire.

Les questions sans réponse sont traitées comme des chaînes vides, représentées par deux apostrophes simples `''`. Les conditions de logique d'obligation conditionnelle suivantes peuvent être utilisées :

| Condition de logique d'obligation conditionnelle | Description |
|:---------------------------|:-------------|
| `${reference_question} != ''` | Obligatoire uniquement si `reference_question` a reçu une réponse (non vide). |
| `${reference_question} = ''`  | Obligatoire uniquement si `reference_question` n'a pas reçu de réponse (vide). |

**onglet survey**

| type  | name    | label                                               | required     |
|:------|:--------|:----------------------------------------------------|:-------------|
| note  | contact | Please provide your phone number or email address below. |              |
| text  | phone   | Phone number                                        |              |
| text  | email   | Email address                                       | ${phone} = '' |
| survey | 