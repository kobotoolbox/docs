# Ajouter une autre langue à votre XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/language_xls.md" class="reference">29 juil. 2025</a>

Il existe deux méthodes pour ajouter plusieurs langues à votre formulaire. Vous pouvez soit les ajouter et les gérer directement via le [Tableau de bord du projet](language_dashboard.md) en ligne, soit les ajouter dans un XLSForm et l'importer dans Kobo.

Voici des instructions détaillées sur la façon d'ajouter une autre langue à votre formulaire :

-   Créez votre formulaire dans la langue par défaut. Il doit s'agir de la langue avec laquelle la personne responsable de la conception du questionnaire est la plus à l'aise. Lorsque vous avez terminé, ou lorsqu'une partie du formulaire a été créée, enregistrez-le. Vous serez redirigé vers le tableau de bord du projet de votre formulaire brouillon.

-   Exportez le formulaire au format XLS.

-   Ouvrez le fichier dans Excel (Google Spreadsheet, Open Office Calc, etc. fonctionneront tous) (Si vous êtes dans Excel, il est possible que vous deviez d'abord retirer le fichier du mode Affichage protégé.
    [Voir ici](https://support.office.com/en-us/article/what-is-protected-view-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653?ocmsassetID=HA010355931&CorrelationId=04b441d5-5c7c-441a-bbac-8f34b3071869&ui=en-US&rs=en-US&ad=US).)
    Votre feuille de calcul comportera trois feuilles (voir les petits onglets en bas) : **survey**, **choices**, **settings**. Restez dans la feuille **survey** pour le moment.

-   Trouvez la colonne appelée `label`. C'est là que sont stockés les intitulés de vos questions d'origine. Insérez une autre colonne à droite de label. Dans l'en-tête (première ligne) de cette nouvelle colonne, écrivez `label::langue (code)`, par exemple `label::Français (fr)` ou `label::English (en)`.

<p class="note">Vous pouvez modifier la taille de vos colonnes, ajouter des couleurs ou changer la taille de la police, rien de tout cela n'affectera votre formulaire.</p>

-   Ensuite, si vous avez des indices dans votre formulaire, la même chose doit s'appliquer à la colonne `hint`, par exemple `hint::Français (fr)` ou `hint::English (en)`.

**feuille survey**

| type             | name           | label                          | relevant                  |
| :--------------- | :------------- | :----------------------------- | :------------------------ |
| text             | full_name      | What is your name?             |                           |
| select_one yesno | children_yesno | Do you have any children?      |                           |
| integer          | children_count | How many children do you have? | ${children_yesno} = 'yes' |
| survey |

-   Maintenant, ajoutez vos traductions pour chaque ligne dans la colonne `label::langue (code)`. Lorsque vous avez terminé, assurez-vous de n'avoir oublié aucune question (pour chaque champ qui contient du texte dans la colonne label, il doit y avoir du texte dans la colonne `label::langue (code)`). Vous pouvez trouver les codes de langue officiels à 2 caractères (sous-étiquettes)
    [ici](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

<p class="note">Astuce : Copiez-collez la colonne label d'origine, puis apportez des modifications aux traductions afin de ne rien laisser vide par accident : Il vaut mieux avoir quelque chose qui s'affiche dans la mauvaise langue que d'avoir une question vide dans une langue. <em>Vous pouvez répéter cette étape et ajouter autant de langues que vous le souhaitez, chacune dans sa colonne distincte et avec un nom différent dans <code>label::langue (code)</code>.</em></p>

**feuille survey**

| type             | name           | label:English (en)             | label::Français (fr)           | relevant                  |
| :--------------- | :------------- | :----------------------------- | :----------------------------- | :------------------------ |
| text             | full_name      | What is your name?             | Quel est votre nom?            |                           |
| select_one yesno | children_yesno | Do you have any children?      | Avez-vous des enfants?         |                           |
| integer          | children_count | How many children do you have? | Combien des enfants avez-vous? | ${children_yesno} = 'yes' |
| survey |

-   Maintenant, passez à la feuille **choices** de votre fichier, si vous en avez une.

-   Dans la feuille **choices**, vous avez une autre colonne appelée `label`. Répétez les étapes 5 et 6. Assurez-vous d'utiliser exactement la même orthographe pour `label::langue (code)`. Par exemple, `label::Francais (fr)` et `label::Français (fr)` ne sont pas identiques.

**feuille choices**

| list_name | name | label::English (en) | label::Français (fr) |
| :-------- | :--- | :------------------ | :------------------- |
| yesno     | yes  | Yes                 | Oui                  |
| yesno     | no   | No                  | Non                  |
| choices |

-   Dans la feuille **settings**, sous `form_title`, modifiez le texte du titre de votre formulaire en quelque chose comme « Mon formulaire (anglais et français) » afin de pouvoir l'identifier facilement plus tard.

**feuille settings**

| form_title                      |
| :------------------------------ |
| Mon formulaire (anglais et français) |
| settings |

-   Enregistrez votre fichier et fermez Excel.

-   Retournez dans KoboToolbox et cliquez sur **Remplacer par XLS**, puis importez votre XLSForm mis à jour. Choisissez le fichier que vous venez de terminer de modifier et cliquez sur **OK**.

-   Ouvrez le formulaire que vous venez d'importer et cliquez sur **Prévisualiser le formulaire**. En haut, à côté de **Choisir la langue**, cliquez sur le menu déroulant. Il affichera une langue par défaut (votre langue d'origine) ainsi que les nouvelles langues que vous venez d'ajouter.

## Traduire vers les scripts tamoul, népalais, hindi, etc.

Lors de la traduction vers des scripts non latins, tels que le tamoul, le népalais, l'hindi, etc., assurez-vous de ne pas utiliser une police dite pseudo. Lorsque vous écrivez dans ces langues, assurez-vous d'utiliser uniquement les caractères Unicode appropriés. Pour écrire des caractères Unicode appropriés, vous n'avez pas besoin d'installer de polices particulières. Au lieu de cela, vous (ou votre traducteur) devez configurer votre clavier pour utiliser le script respectif (tamoul, népalais, etc.) et ensuite écrire normalement. Le paramètre de clavier correct produira les lettres réelles du script en Unicode au lieu d'équivalents phonétiques latins. (Ce serait également la même façon d'écrire ces langues dans un e-mail, KoboToolbox ou toute autre application Web.)

Pour obtenir de l'aide sur l'ajout du clavier système correct,
[consultez ce lien](https://support.microsoft.com/en-us/help/17424/windows-change-keyboard-layout)
(Windows uniquement).

Les polices pseudo permettent d'écrire dans ces scripts et sont couramment utilisées dans de nombreux pays, en particulier en Asie du Sud. Mais bien qu'elles fonctionnent sur l'ordinateur sur lequel une police spécifique est installée, elles ne fonctionneront pas sur un autre ordinateur qui n'utilise pas cette police particulière. C'est parce que ces polices ne font que déguiser des caractères et symboles latins ordinaires et les font apparaître sous une forme différente. Par exemple, lorsque vous écrivez « Hello » avec la police pseudo népalaise « Preeti », cela ressemblera à ceci : हेल्लो. Mais ce qui est réellement écrit là reste les lettres H e l l o. Pour certaines personnes, l'utilisation de ces polices qui utilisent souvent des équivalents phonétiques de l'anglais peut être plus facile. Une autre raison pour laquelle elles sont largement utilisées est que de nombreux ordinateurs n'avaient pas de support pour ces scripts et avaient donc besoin de polices pseudo comme « solution de contournement ». Quoi qu'il en soit, les caractères Unicode sont la meilleure solution - et la seule pour une utilisation dans KoboToolbox.

## Traduire des scripts de droite à gauche

Lors de l'ajout d'une langue qui utilise un script de droite à gauche, il est important d'utiliser le code de langue correct. Cependant, même si le code correct est utilisé, si la première question, indice ou note est écrit dans un script de gauche à droite, le formulaire formatera automatiquement le reste de la traduction dans un format de gauche à droite.