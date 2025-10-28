# Utilisation de styles alternatifs pour les formulaires web Enketo
<a href="../alternative_enketo.html">Read in English</a> | <a href="../es/alternative_enketo.html">Leer en español</a> | <a href="../ar/alternative_enketo.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/347a1280aadb22c9aebf88650fd6efa1bcadbcdf/source/alternative_enketo.md" class="reference">24 Sep 2025</a>

Les formulaires web Enketo peuvent être personnalisés dans la manière dont vos questions sont présentées.
Deux styles alternatifs peuvent être sélectionnés et même combinés :
**Pages multiples** et **Thème grille**.

Le mode **Pages multiples** affiche une question à la fois par écran, ou un [groupe
de questions](group_repeat.md) configuré pour s'afficher sur le même écran. C'est la même façon dont
KoboCollect fonctionne.

Le **Thème grille** est un affichage alternatif des questions conçu pour être plus compact
et plus proche des formulaires papier où l'espace est souvent une préoccupation majeure. theme-grid
permet d'afficher plusieurs questions par ligne et s'adapte de manière flexible en cas de logique de saut
faisant apparaître ou disparaître une nouvelle question. Pour afficher plusieurs questions
sur une ligne, elles doivent faire partie d'un groupe, qui par défaut affiche jusqu'à quatre
questions côte à côte. Ce thème peut être personnalisé en définissant le
nombre de questions à inclure dans chaque ligne via le champ d'apparence des
paramètres de chaque question. Pour plus de détails,
[consultez cet article](https://blog.enketo.org/gorgeous-grid).

Il est également possible d'utiliser à la fois **Pages multiples** et **Thème grille** ensemble.
Vous pouvez définir ces styles via l'interface utilisateur de l'interface de création de formulaires KoboToolbox :

![image](/images/alternative_enketo/multiple_grid.gif)

Si vous construisez votre projet d'enquête via XLSForm, vous pouvez faire de même
en définissant le thème sous la colonne `style` dans la feuille `settings` :

**feuille settings**

| form_title  | style |
| :---------- | :---- |
| Themed form | pages |
| settings |

## Styles disponibles dans XLSForm :

| Thème XLSForm                        | Description                                        |
| :----------------------------------- | :------------------------------------------------- |
| (laisser vide)                       | Par défaut – page unique                           |
| `theme-grid no-text-transform`       | Thème grille                                       |
| `theme-grid`                         | Thème grille avec titres en MAJUSCULES             |
| `pages`                              | Pages multiples                                    |
| `theme-grid pages no-text-transform` | Thème grille + Pages multiples                     |
| `theme-grid pages`                   | Thème grille + Pages multiples + titres en MAJUSCULES |