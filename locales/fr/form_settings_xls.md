# Paramètres de formulaires dans XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/form_settings_xls.md" class="reference">23 Apr 2026</a>

XLSForm vous permet de configurer les paramètres de vos formulaires à l'aide de l'**onglet settings**. Par exemple, vous pouvez spécifier un titre de formulaire, définir une langue par défaut ou suivre les numéros de version.

Cet article explique comment ajouter et utiliser les paramètres de formulaires disponibles dans XLSForm.

## Ajouter des paramètres de formulaires dans XLSForm

Pour ajouter des paramètres de formulaires dans XLSForm :
1. Ajoutez un **onglet settings** à votre XLSForm.
2. Créez une nouvelle colonne pour chaque paramètre, en utilisant le nom de colonne exact indiqué [dans le tableau ci-dessous](https://support.kobotoolbox.org/fr/form_settings_xls.html#available-form-settings-in-xlsform).
3. Sous chaque paramètre, indiquez la valeur correspondante (voir l'exemple ci-dessous).

**onglet settings**

| form_title            | version | default_language | style |
|:----------------------|:--------|:----------------|:------|
| Form settings in XLSForm | v3     | English (en)    | pages |

## Paramètres de formulaires disponibles dans XLSForm

Les paramètres de formulaires disponibles dans XLSForm sont les suivants :

| Paramètre de formulaire    | Description |
|:----------------------------|:------------|
| <code>form_title</code>     | Spécifie le titre du formulaire affiché aux utilisateurs. Ce paramètre peut également être défini et géré dans KoboToolbox lors de l'envoi du formulaire. |
| <code>version</code>        | Inclut une chaîne de caractères représentant la version actuelle du XLSForm (par exemple, v1 ou AAAAMMJJ). Utile pour suivre les versions d'un formulaire dans le cadre d'une collaboration. |
| <code>instance_name</code>  | Spécifie un nom unique pour chaque soumission de formulaire à partir des champs renseignés par l'utilisateur lors de l'enquête. S'affiche dans le tableau de données pour chaque soumission. Peut être utilisé pour créer des identifiants personnalisés de participants ou de soumissions.<br><br>Par exemple, <code>concat(${lname}, '-', ${fname}, '-', today())</code> renvoie <code>nom-prénom-date</code>. |
| <code>default_language</code> | Définit la langue par défaut dans les <a href="https://support.kobotoolbox.org/fr/language_xls.html">formulaires traduits</a>. Le format <code>langue (code)</code> est utilisé, tel que défini dans le <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">registre IANA des sous-étiquettes de langue</a>. |
| <code>style</code>          | Spécifie un <a href="https://support.kobotoolbox.org/fr/form_style_xls.html">thème alternatif pour les formulaires web</a>. |
| <code>allow_choice_duplicates</code> | Permet à un XLSForm de réutiliser des noms d'options dupliqués **au sein** d'une liste de choix (par exemple, lors de l'utilisation de filtres de choix où les noms de choix sont dupliqués). |
| <code>public_key</code>     | Spécifie la clé publique pour les <a href="https://support.kobotoolbox.org/fr/encrypting_forms.html?highlight=encryption">formulaires avec chiffrement activé</a>. |