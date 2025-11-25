# Type de question Sélectionner un ou plusieurs éléments d'un fichier externe
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/87ff8377b846dacb801191e0b619126a563040a9/source/external_file.md" class="reference">28 août 2025</a>

Dans certains cas, il peut être souhaitable d'héberger une liste d'options de choix dans un fichier externe, plutôt que directement dans le XLSForm du projet. Par exemple, une longue liste de choix (par exemple, des centaines ou des milliers) pourrait ralentir le chargement et la navigation du formulaire, ou l'ajout de nouvelles options de choix après le début de la collecte de données pourrait parfois être problématique.

<p class="note"> <b>Remarque :</b> Cet article couvre les étapes de configuration des questions Sélectionner un ou plusieurs éléments d'un fichier externe dans XLSForm. Pour configurer ces questions dans l'interface de création de formulaires, vous devez d'abord importer le fichier de choix externe dans KoboToolbox, dans l'onglet <b>Médias</b> de la page <b>PARAMÈTRES</b>. Une fois le fichier importé, les types de questions Sélectionner un ou plusieurs éléments d'un fichier externe apparaîtront dans l'interface de création de formulaires. </p>

![image](/images/external_file/select_from_file.png)

Cet article fournit un exemple détaillé et une méthode pour créer un type de question `select_one` ou `select_many` avec la liste de choix dans un fichier externe séparé. Consultez la [documentation XLSForm](https://xlsform.org/en/#multiple-choice-from-file) pour plus d'informations.

**1.** Dans le XLSForm, le type doit être soit `select_one_from_file [nom_du_fichier]` soit `select_multiple_from_file [nom_du_fichier]` :

<p class="note">Le type de fichier peut être soit <code>CSV</code> soit <code>XML</code></p>

**Feuille survey**

| type                            | name   | label                           |
| :------------------------------ | :----- | :------------------------------ |
| text                            | name   | Quel est votre nom ?            |
| select_one sex                  | sex    | Quel est votre sexe ?           |
| select_one_from_file fruits.csv | fruits | Quel est votre fruit préféré ?  |
| survey |

**Feuille choices**

| list_name | name | label  |
| :-------- | :--- | :----- |
| sex       | 1    | Homme  |
| sex       | 2    | Femme  |
| choices |

<p class="note">Le fichier <code>fruits.csv</code> est le nom du fichier contenant les choix pour la question « Quel est votre fruit préféré ? ».</p>

**2.** Créez un nouveau fichier `CSV` et structurez-le de la même manière que la feuille `choices` dans le XLSForm :

**fruits.csv**

| list_name | name | label       |
| :-------- | :--- | :---------- |
| fruits    | 1    | Pomme       |
| fruits    | 2    | Pastèque    |
| fruits    | 3    | Orange      |
| fruits    | 4    | Poire       |
| fruits    | 5    | Cerise      |
| fruits    | 6    | Fraise      |
| fruits    | 7    | Nectarine   |
| fruits    | 8    | Raisin      |
| fruits    | 9    | Mangue      |
| fruits    | 10   | Myrtille    |
| fruits    | 11   | Grenade     |

**3.** Importez et déployez le XLSForm dans KoboToolbox.

**4.** Importez le fichier `CSV` de la même manière que vous [ajouteriez un fichier média au formulaire](media.md)