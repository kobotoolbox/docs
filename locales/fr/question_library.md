# Utiliser La bibliothèque de questions
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/385b471fb227f28575b67a450696cc8e4f4a3779/source/question_library.md" class="reference">2 juil. 2025</a>

## Ajouter des questions à votre bibliothèque

Les questions qui ont été précédemment ajoutées à votre bibliothèque peuvent être ajoutées à n'importe quel autre formulaire en les faisant glisser-déposer depuis la barre latérale La bibliothèque de questions dans l'interface de création de formulaires.

Pour accéder à la barre latérale La bibliothèque de questions, cliquez sur le bouton **Ajouter depuis la bibliothèque** dans le coin supérieur droit de la barre d'outils de l'interface de création de formulaires.

![image](/images/question_library/library.jpg)

Si nécessaire, vous pouvez rechercher la question que vous cherchez en utilisant la fonction de recherche pour rechercher par mot-clé ou par étiquette.

Pour ajouter la question à votre formulaire, **faites-la glisser-déposer** à la position souhaitée. Une question peut être ajoutée plusieurs fois si nécessaire, par exemple lors de la réutilisation d'une échelle spécifique pour différentes questions.

## Gérer les questions dans votre bibliothèque

La bibliothèque de questions vous permet de sauvegarder et de réutiliser les questions fréquemment utilisées.

Pour gérer La bibliothèque de questions, cliquez sur le bouton du menu bibliothèque dans la barre latérale supérieure gauche. Par défaut, la bibliothèque affichera toutes vos questions. Vous pouvez **consulter** ou modifier chaque question individuelle en cliquant sur le libellé de la collection.

Pour **cloner** ou **télécharger** la collection, passez la souris sur le libellé de la collection et les icônes apparaîtront sur le côté droit.

Vous pouvez également **ajouter de nouvelles questions** depuis la bibliothèque. Il suffit de cliquer sur **Nouveau** et vous pourrez créer une nouvelle question qui sera sauvegardée dans la bibliothèque.

Pour **supprimer des questions** dans votre bibliothèque, cliquez simplement sur **Supprimer** après avoir cliqué sur l'icône **Plus d'actions**.

![image](/images/question_library/delete.jpg)

## Importer des collections

En plus de créer des collections dans l'interface, vous pouvez également importer de grands ensembles de questions et de blocs depuis Excel, basés sur le format XLSForm. Les utilisatrices et utilisateurs avancés trouveront plus pratique de partir de XLSForms existants plutôt que de copier le contenu des questions existantes dans l'outil un par un.

![image](/images/question_library/import_collection.png)

Par défaut, chaque fichier XLS sera importé en tant que nouvelle collection. Si votre fichier ne contient qu'une seule question ou un seul bloc, il importera uniquement cette question ou ce bloc au lieu de créer une collection. Le nom de la collection est tiré du nom du fichier (les doublons de collections existantes sont autorisés). Mais il est facile de renommer la collection après l'avoir importée - il suffit de cliquer sur le nom de la collection dans la barre latérale gauche, puis de cliquer sur l'icône des paramètres.

Utilisez <a download class="reference" href="./_static/files/question_library/collection_import_sample.xlsx">ce fichier Excel comme modèle</a>.
Le fichier suit généralement le format XLSForm. Il y a quelques différences :

* La feuille principale contenant les questions doit être nommée **library** lors de l'importation de plusieurs blocs.
* (Facultatif) Les blocs de questions doivent être définis dans la colonne supplémentaire appelée **block**, en écrivant le même titre de bloc dans chaque ligne du tableau qui doit être incluse dans le bloc. Le libellé du bloc n'a aucune limitation en termes de caractères, mais il doit avoir exactement la même orthographe pour éviter de diviser le bloc (« Questions sur le ménage » est différent de « questions sur le ménage »). Utilisez un titre de bloc qui facilite l'identification du contenu ultérieurement.
* Toute ligne de la feuille de modèle qui n'a pas de valeur dans la colonne bloc sera importée en tant que question distincte.
* (Facultatif) Définissez toutes les étiquettes pour la question ou le bloc en ajoutant une colonne **tag:[nom de votre étiquette]** pour chaque étiquette, puis en écrivant « 1 » dans chaque ligne qui doit utiliser l'étiquette. Dans le cas des blocs, il suffit d'écrire « 1 » dans l'une des lignes du bloc, peu importe laquelle. Il suffit de marquer l'une des questions du bloc, même si cela n'a pas d'importance si plusieurs questions sont étiquetées.

Quelques autres suggestions :

* Vous pouvez inclure des groupes dans les blocs. Assurez-vous simplement que la ligne « begin group » a un identifiant « name » unique (comme dans tous les XLSForms) et que l'ouverture (begin group) et la fermeture (end group) sont incluses dans le bloc. Ajouter le nom du bloc comme libellé de groupe pourrait être une bonne idée afin que vous voyiez le libellé du bloc après l'avoir importé dans l'interface de création de formulaires.
* Vous pouvez inclure une logique de saut et des règles de validation dans les blocs que vous importez. C'est très utile lors de l'importation de blocs entiers de questions dans de nouveaux brouillons de formulaires sans avoir à reconstruire ces paramètres avancés.
* Vous pouvez ajouter plusieurs langues aux libellés de questions et de réponses avec la syntaxe XLSForm habituelle (label::English (en), label::Español (es), etc.)