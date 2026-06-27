# Introduction à XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/485fe4fed42cbb765b4838cb7f8c9665a561d091/source/edit_forms_excel.md" class="reference">25 Nov 2025</a>

KoboToolbox utilise [XLSForm](http://xlsform.org/en/), un format standardisé pour concevoir des formulaires électroniques dans Excel ou d'autres logiciels de tableur. XLSForm facilite la gestion de formulaires complexes, tels que ceux comportant de longues listes de choix ou plusieurs traductions. Bien que l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** offre une interface intuitive et facile à utiliser, XLSForm est recommandé pour travailler avec des fonctionnalités avancées ou des formulaires complexes.

Tous les formulaires KoboToolbox sont entièrement compatibles avec XLSForm. Vous pouvez ainsi importer et exporter facilement vos formulaires entre KoboToolbox et d'autres plateformes de collecte de données. XLSForm fournit un format standardisé pour le développement de formulaires à l'aide de logiciels de tableur courants, ce qui en fait une option pratique pour la collaboration et le partage.

Cet article couvre les sujets suivants :

- Avantages de l'utilisation de XLSForm pour le développement de formulaires
- Aperçu de l'utilisation de XLSForm avec KoboToolbox
- Ressources supplémentaires pour apprendre XLSForm

![image](/images/edit_forms_excel/sample_xlsform.png)

<p class="note">
  Cet article présente une introduction à XLSForm. Pour commencer à créer des XLSForms, consultez l'article <a class="reference" href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">Créer un XLSForm</a>.
  <br><br>
  Pour un apprentissage pratique du développement de formulaires avec XLSForm, consultez le <a class="reference" href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals de la KoboToolbox Academy</a>.
</p>

## Avantages de l'utilisation de XLSForm

XLSForm offre de nombreux avantages pour créer des formulaires de collecte de données, qu'ils soient simples ou complexes.

### Création et modification efficaces de formulaires

XLSForm tire parti des fonctionnalités familières des tableurs pour créer et modifier des formulaires efficacement. Vous pouvez utiliser des formules et des fonctionnalités Excel telles que le copier-coller, le glisser-déposer, Rechercher et remplacer, le tri et le filtrage pour créer et gérer rapidement des formulaires volumineux.

### Gestion des listes de choix pour les questions à choix multiple

XLSForm facilite la création et la gestion des [listes de choix](https://support.kobotoolbox.org/fr/option_choices_xls.html). Vous pouvez copier de longues listes directement depuis des sources externes, réutiliser les mêmes options dans plusieurs questions ou les dupliquer d'un formulaire à l'autre, ce qui permet de gagner du temps, d'assurer la cohérence et de réduire les erreurs manuelles.

### Gestion de versions et collaboration

XLSForm simplifie le partage et la gestion des versions de formulaires. Les formulaires étant des fichiers Excel ou Google Sheets, les équipes peuvent collaborer dessus en temps réel, les partager pour révision et conserver un historique des versions.

### Personnalisation des formulaires

XLSForm vous permet d'adapter entièrement vos formulaires à différents besoins. Vous pouvez ajouter et gérer [plusieurs traductions](https://support.kobotoolbox.org/fr/language_xls.html) directement dans votre XLSForm pour prendre en charge la collecte de données multilingue. Vous pouvez facilement mettre en place des structures de formulaires complexes, telles que des [groupes de questions](https://support.kobotoolbox.org/fr/grouping_questions_xls.html) ou des [sections répétées](https://support.kobotoolbox.org/fr/repeat_groups_xls.html). Vous pouvez également connecter votre formulaire à des [sources de données externes](https://support.kobotoolbox.org/fr/pull_data_kobotoolbox.html) et à [d'autres projets KoboToolbox](https://support.kobotoolbox.org/fr/dynamic_data_attachment.html).

### Fonctionnalités avancées

XLSForm facilite l'utilisation de fonctionnalités avancées de création de formulaires, telles que la [logique de saut](https://support.kobotoolbox.org/fr/skip_logic_xls.html), les [calculs](https://support.kobotoolbox.org/fr/calculations_xls.html) et les [contraintes](https://support.kobotoolbox.org/fr/constraints_xls.html). En tant que standard ouvert, XLSForm donne également accès à des fonctionnalités qui ne sont pas encore disponibles dans le Formbuilder.

## Utiliser XLSForm avec KoboToolbox

XLSForm s'intègre parfaitement à KoboToolbox pour la création, la prévisualisation, la modification et le déploiement de formulaires pour la collecte de données.

Les utilisateurs peuvent commencer dans le Formbuilder en créant un nouveau formulaire et en ajoutant des questions, puis [télécharger leur formulaire](https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox) en tant que XLSForm pour le personnaliser davantage. Cela fournit une base structurée, ce qui peut être utile pour les nouveaux projets ou les utilisateurs ayant moins d'expérience en création de formulaires.

Les formulaires créés dans XLSForm peuvent ensuite être importés dans KoboToolbox pour être prévisualisés, testés, modifiés et déployés. Les formulaires peuvent être vérifiés pour détecter des erreurs et facilement modifiés dans KoboToolbox, par exemple en changeant le titre ou les paramètres.

<p class="note">
  Pour plus d'informations, consultez l'article <a class="reference" href="https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html">Utiliser XLSForm avec KoboToolbox</a>.
</p>

## Ressources supplémentaires sur XLSForm

De nombreuses ressources sont disponibles pour apprendre XLSForm et résoudre des problèmes.

KoboToolbox propose les ressources suivantes :

- [Centre d'aide KoboToolbox](https://support.kobotoolbox.org) : une vaste bibliothèque de documentation avec des articles d'aide sur KoboToolbox et XLSForm.
- [Cours XLSForm Fundamentals de KoboToolbox](https://academy.kobotoolbox.org/courses/xlsform-fundamentals) : un cours en ligne développé par notre équipe d'experts, qui couvre un large éventail de compétences, notamment la création d'un XLSForm à partir de zéro, l'utilisation de la logique de formulaire et des calculs, ainsi que le test et le déploiement de formulaires pour la collecte de données avec KoboToolbox.
- [Forum communautaire KoboToolbox](https://community.kobotoolbox.org) : un espace pour échanger avec notre communauté mondiale d'utilisateurs, obtenir de l'aide pour la création de formulaires personnalisés ou la résolution de problèmes, et partager des ressources KoboToolbox.

Les ressources externes comprennent :

- [Documentation XLSForm](https://xlsform.org/en/) : un site de documentation complet dédié à XLSForm.
- [Référence et modèle XLSForm](https://xlsform.org/en/ref-table/) : une ressource détaillée pour créer et personnaliser des formulaires, incluant les types de questions, les apparences et les colonnes optionnelles.
- [Documentation ODK](https://docs.getodk.org/form-reference/) : un autre site de documentation complet dédié à XLSForm.