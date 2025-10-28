# Ajouter une autre langue dans le tableau de bord du projet
<a href="../language_dashboard.html">Read in English</a> | <a href="../es/language_dashboard.html">Leer en español</a> | <a href="../ar/language_dashboard.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/a412eff1342fa59da1fe2ffe1e10c1829b2e5e94/source/language_dashboard.md" class="reference">1 nov. 2022</a>

Il existe deux méthodes pour ajouter plusieurs langues à votre formulaire. Vous pouvez soit
les ajouter et les gérer directement via le tableau de bord du projet en ligne, soit les ajouter
dans un [formulaire XLS et l'importer dans Kobo](language_xls.md).

Voici des instructions détaillées sur la façon d'ajouter et de gérer une autre langue dans
votre formulaire via le tableau de bord du projet en ligne :

1. Créez votre formulaire dans la langue par défaut en utilisant l'interface de création de formulaires ou
   en configurant le formulaire sous forme de fichier XLS, puis importez-le directement dans
   KoboToolbox. La langue par défaut doit être la langue avec laquelle la personne
   responsable de la conception du questionnaire est la plus à l'aise.

2. Lorsque vous avez terminé, ou lorsqu'une partie importante du formulaire a été
   créée, enregistrez-le. Vous serez redirigé vers le tableau de bord du projet du formulaire brouillon.

3. Trouvez et cliquez sur l'icône « Plus d'actions » (3 points). Dans le menu déroulant
   qui apparaît, cliquez sur « Gérer les traductions ».

   ![image](/images/language_dashboard/action.png)

4. Avant d'ajouter des langues supplémentaires, définissez d'abord votre langue par défaut en
   cliquant sur l'icône crayon et en remplissant les champs « Nom de la langue » et « Code de
   langue ».

   **Astuce** : Si vous n'êtes pas sûr de votre code de langue, vous pouvez rechercher
   dans la liste complète des codes de langue
   [ici](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).
   Si vous ne trouvez pas votre langue, il est possible qu'elle ait été étiquetée sous
   un autre nom et il vaut la peine de rechercher en ligne des noms alternatifs.

   Exemples : Anglais (en), Allemand (de), Arabe (ar), etc.

   ![image](/images/language_dashboard/example.gif)

5. Une fois la langue par défaut définie, cliquez sur le bouton « Ajouter une langue » pour
   remplir le nom de la langue et le code de la nouvelle langue ajoutée.

6. Une fois la nouvelle langue ajoutée, cliquez sur l'icône « Mettre à jour les traductions »
   (globe) à droite du titre de la langue pour ouvrir le « Tableau des traductions »
   pour cette langue.

   ![image](/images/language_dashboard/add_language.gif)

7. Remplissez les traductions avec les chaînes originales associées correctes dans la
   vue tableau, puis cliquez sur « Enregistrer les modifications » lorsque vous avez terminé. Fermez ensuite la
   vue tableau en cliquant sur le bouton « x » en haut à droite du tableau.

   ![image](/images/language_dashboard/translation.png)

8. De retour dans le tableau de bord du projet, cliquez sur l'icône « Aperçu » (œil) pour ouvrir un
   aperçu du formulaire. En haut, à côté de Choisir la langue, cliquez sur le menu
   déroulant. Il affichera par défaut (votre langue d'origine) ainsi que la ou les nouvelles
   langues que vous venez d'ajouter.

   ![image](/images/language_dashboard/preview.gif)

9. Répétez les étapes pour toutes les langues supplémentaires.

**Conseils supplémentaires** :

**Modifier la langue par défaut**

La langue par défaut doit être la langue la plus couramment utilisée pendant la
collecte de données. Pour modifier la langue par défaut, cliquez sur « Gérer les traductions », puis
cliquez sur l'icône qui apparaît à droite de la langue souhaitée lorsque
votre souris passe dessus.

![image](/images/language_dashboard/default.gif)

**Traduire des écritures de droite à gauche**

Lors de l'ajout d'une langue qui utilise une écriture de droite à gauche, il est important d'utiliser
le code de langue correct. Cependant, même si le code correct est utilisé, si la
première question, indication ou note est écrite dans une écriture de gauche à droite, le formulaire
formatera automatiquement le reste de la traduction dans un format de gauche à droite.