# Ajouter des traductions dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/55b3ab6258a25c2b16c1d954b282f02918937598/source/language_dashboard.md" class="reference">5 juin 2026</a>

<iframe src="https://www.youtube.com/embed/3O2K78F7DCA?si=lt-ZlSRoAjFuSMl1&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Ajouter des traductions à un formulaire permet aux utilisateurs de **choisir leur langue préférée** lors de la collecte de données, sans avoir à créer des formulaires distincts. Vous pouvez ajouter autant de traductions que nécessaire. [KoboCollect](../fr/data_collection_kobocollect.md) et les [formulaires web](../fr/data_through_webforms.md) sont tous deux compatibles avec les traductions de formulaires.

Vous pouvez ajouter des traductions à votre formulaire directement dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** ou en utilisant [XLSForm](../fr/language_xls.md). KoboToolbox propose une **interface intuitive** qui ne nécessite aucune expertise technique et vous permet d'ajouter facilement plusieurs traductions à vos formulaires. Cette approche est utile lorsque vous travaillez avec un petit nombre de questions ou lorsque vous souhaitez effectuer des ajustements rapides.

<p class="note">
   <strong>Note :</strong> Pour les formulaires multilingues plus volumineux ou plus complexes, XLSForm est souvent l'option la plus efficace. Il vous permet de gérer les traductions en masse, ce qui peut faire gagner du temps lorsque vous travaillez avec de nombreuses questions ou plusieurs langues. Pour en savoir plus sur la configuration des traductions dans XLSForm, consultez l'article <a href="../fr/language_xls.md">Ajouter des traductions dans XLSForm</a>.
</p>

Cet article porte sur l'ajout de traductions depuis la plateforme KoboToolbox et couvre les sujets suivants :
- Définir la langue par défaut de votre formulaire
- Ajouter des langues et des traductions
- Modifier la langue par défaut

<p class="note">
    Pour en savoir plus sur la collecte et la gestion des données issues de formulaires traduits, consultez l'article <a href="../fr/collecting_data_multiple_languages.md">Collecter des données dans plusieurs langues</a>.
</p>

## Définir la langue par défaut

La langue par défaut d'un formulaire est généralement la langue dans laquelle le questionnaire a été conçu, et la langue dans laquelle le formulaire s'ouvre par défaut lors de la collecte de données. La langue par défaut ne doit être définie que si des traductions supplémentaires sont ajoutées ; elle n'est pas requise lorsque le formulaire n'est disponible que dans une seule langue.

Pour définir la langue par défaut :

1. Créez votre formulaire dans la langue par défaut.
2. Une fois votre formulaire créé, accédez à la page **FORMULAIRE** de votre projet.
3. Sous le bouton **DÉPLOYER** ou **REDÉPLOYER**, cliquez sur <i class="k-icon-language"></i> **Gérer**.
4. Saisissez le nom de la langue (par exemple, « Français ») et le code de la langue (par exemple, « fr ») pour votre langue par défaut.

![Gérer les langues](images/language_dashboard/manage_languages.png)

<p class="note">
    <strong>Note :</strong> Les codes de langue sont disponibles dans le <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">registre IANA des sous-étiquettes de langue</a>. Sur le site de l'IANA, le champ <strong>Description</strong> correspond au nom de la langue et le champ <strong>Subtag</strong> correspond au code de la langue (par exemple, <strong>Description</strong> : French, <strong>Subtag</strong> : fr).
</p>

## Ajouter des langues et des traductions

Une fois la langue par défaut définie, vous pouvez ajouter d'autres langues et traduire le contenu de votre formulaire :

1. Dans la fenêtre <i class="k-icon-language"></i> **Gestion des langues**, cliquez sur **Ajouter une langue**.
2. Saisissez le nom et le code de la langue, puis cliquez sur **Ajouter**.
3. En regard de la langue ajoutée, cliquez sur <i class="k-icon-language-settings"></i> **Mettre à jour les traductions**.
    - Un tableau s'affiche avec tous les éléments traduisibles de votre formulaire, notamment les libellés de questions, les libellés de groupes, les indices, les instructions supplémentaires (guidance hint), les messages de contrainte, les fichiers médias et les libellés de choix.
    - Chaque langue dispose de son propre tableau de traductions.
4. Saisissez les traductions, puis cliquez sur **Sauvegarder les modifications**.
    - Si vous omettez le texte d'un élément traduit, celui-ci apparaîtra comme un champ vide dans le formulaire.
5. Fermez la fenêtre et prévisualisez votre formulaire pour vérifier les traductions.
6. Déployez ou redéployez votre formulaire pour appliquer les modifications.

Vous pouvez revenir à cette fenêtre à tout moment pour mettre à jour les traductions existantes ou en ajouter de nouvelles. N'oubliez pas de mettre à jour les traductions chaque fois que vous ajoutez de nouvelles questions ou de nouveaux choix de réponse.

![Ajouter une nouvelle langue](images/language_dashboard/add_language.png)


## Modifier la langue par défaut

Pour modifier la langue par défaut du formulaire :

1. Sur la page **FORMULAIRE**, cliquez sur <i class="k-icon-language"></i> **Gérer**.
2. Cliquez sur <i class="k-icon-language-default"></i> **Définir par défaut** en regard de la langue que vous souhaitez définir comme langue par défaut.

![Modifier la langue par défaut](images/language_dashboard/change_default.png)

## Résolution de problèmes

<details>
  <summary><strong>Error loading survey: There is an unnamed translation in your form definition</strong></summary>
  Cette erreur signifie qu'au moins un élément de votre formulaire (par exemple, un indice ou un message) n'est associé à aucune langue.
<br><br>
Pour résoudre ce problème :

<ol>
<li>Téléchargez votre formulaire en tant que <a href="../fr/xlsform_with_kobotoolbox.md">XLSForm</a>.</li>
<li>Recherchez dans votre formulaire une colonne <code>label</code>, <code>hint</code>, <code>guidance_hint</code>, média, <code>constraint_message</code> ou <code>required_message</code> qui n'est associée à aucune langue (par exemple, <code>label</code> au lieu de <code>label::French (fr)</code>).</li>
<li>Selon le problème rencontré, ajoutez un <a href="../fr/language_xls.md">nom et un code de langue</a> au nom de la colonne non associée, ou copiez son contenu dans la colonne existante correspondant à cette langue, puis supprimez la colonne non associée.</li>
</ol>

</details>

<br>

<details>
  <summary><strong>Issue displaying right-to-left scripts</strong></summary>
  Lorsque vous ajoutez une langue utilisant un script de droite à gauche (RTL), comme l'arabe, l'hébreu ou l'ourdou, il est important d'utiliser le <strong>code de langue correct</strong> et de vous assurer que le <strong>premier texte visible dans la traduction</strong> (par exemple, un libellé de question, un indice ou une note) est rédigé dans la langue RTL. Cela garantit que la mise en page du formulaire ne revient pas par défaut à un formatage de gauche à droite (LTR).
</details>