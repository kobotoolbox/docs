# Type de question Calcul avancé
<a href="../advanced_calculate.html">Read in English</a> | <a href="../es/advanced_calculate.html">Leer en español</a> | <a href="../ar/advanced_calculate.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/c2e8c882fdd831549c2f7f4474a9d522bafc181b/source/advanced_calculate.md" class="reference">2 déc. 2021</a>

Certains formulaires avancés peuvent nécessiter qu'un calcul interne soit effectué dans le cadre du formulaire (plutôt qu'après, lors de l'analyse). Cela peut être fait en ajoutant un **Calcul** et en écrivant l'expression mathématique dans le champ de libellé de la question.

Cet article fournit des instructions étape par étape sur la façon d'ajouter des calculs lors de l'utilisation de l'interface de création de formulaires ou en téléchargeant et en l'ajoutant directement au XLSForm.

Pour consulter une liste complète et détaillée de toutes les fonctions, veuillez visiter l'excellente [documentation sur les fonctions XPath](https://getodk.github.io/xforms-spec) d'ODK.

## Approches pour ajouter des questions de calcul :

### Utilisation de l'interface de création de formulaires

Étape 1 : Ajoutez une question de calcul

![image](/images/advanced_calculate/calculate_question.jpg)

Étape 2 : Tapez votre formule de calcul là où vous écririez normalement votre question.

![image](/images/advanced_calculate/formulas.jpg)

Remarque :

* Votre question de calcul ne sera pas affichée lors de la saisie/collecte de données, que ce soit sur KoboCollect ou Enketo. Elle sera cependant affichée lors de la consultation des données en mode Tableau ou dans la version téléchargée.
* Vous devez suivre des règles similaires à celles des XLS Forms (voir notre section sur les règles ci-dessous).

### Utilisation des XLS Forms

Nous recommandons cette approche lorsque vous travaillez avec des fonctions de calcul plus avancées.

Les XLS Forms permettent l'utilisation de la fonction de calcul sur différents types de questions.

* Vous pouvez reproduire l'approche utilisée dans l'interface de création de formulaires où la question ne sera pas affichée lors de la collecte de données en définissant simplement le type de question comme « calculate » puis en tapant votre calcul dans la colonne calculate.
* Vous pouvez utiliser « calculate » pour différents types de questions, et dans ce cas la question sera affichée pendant la collecte de données. Vous pouvez choisir de rendre cette question en lecture seule afin que personne ne puisse modifier la saisie. Les types de questions que nous avons testés avec cette approche incluent :

    a. integer (n'acceptera que les fonctions de calcul numériques)
    b. text (n'acceptera que les fonctions de calcul de chaînes)
    c. note (n'acceptera que le référencement de questions et non les fonctions de calcul)
    d. date (n'acceptera que les fonctions de calcul de dates)
    e. time (n'acceptera que les fonctions de calcul de temps)
    
    ![image](/images/advanced_calculate/xls.png)

## Règles lors du travail avec des questions de calcul :

### Ces règles s'appliquent à la fois à l'interface de création de formulaires et au XLSForm

1. Vous ne pouvez pas utiliser à la fois des calculs numériques et de chaînes dans la même question
2. Vos calculs numériques suivront la règle BODMAS dans l'application des calculs, c'est-à-dire que l'ordre d'exécution des calculs sera Parenthèses, Divisions, Multiplications, Additions puis Soustractions (Rappelez-vous toujours cela lors de l'ordonnancement d'une question)
3. Les questions de calcul qui référencent d'autres questions ne doivent pas être placées dans le même groupe que les questions de référence car le calcul n'apparaîtra pas à moins que vous ne quittiez le groupe
4. Lorsque vous référencez une question dans un calcul, vous devez l'indiquer comme `${Question}` où question est le nom de la question
5. Vous pouvez « forcer » un calcul à s'évaluer en définissant « required » sur TRUE

### Liste des fonctions de calcul testées

_(N'hésitez pas à en recommander d'autres et nous les mettrons à jour)_

![image](/images/advanced_calculate/list.png)

### Utilisation de la commande IF dans les calculs

![image](/images/advanced_calculate/if_command.png)

### Solutions de contournement pour les calculs

_Recommandé pour les utilisatrices et utilisateurs avancés_

#### Solution de contournement 1 : Créer des questions factices pour le calcul du score final dans une série de questions

Disons que vous avez une question comme `QN1 Avez-vous une question ?` Réponses `Oui=1 Non=2 Ne sait pas=999`

Dans ce cas, vous voudrez peut-être créer une QN1 factice juste après QN1 pour tenir compte des différences de codage et définir l'équivalent mathématique. Vous créerez donc une question de calcul QN1d (_notez qu'il s'agit de ma propre convention de nommage, d signifie dummy/factice) et définirez la valeur par défaut à 0 mais écrirez la formule comme **If (${QN1}=1,1,0)**

Remarquez que dans mon formulaire de test, j'ai réussi à créer la situation et les données apparaissent comme codées pour Q1N et comme calculées pour la signification mathématique pour Q1Nd. Cela devrait être la signification prévue par votre score. _Vous pouvez faire cela pour des calculs tels que la richesse où Oui et Non pourraient signifier une valeur différente dans différents pays._

Une fois que vous avez fait cela pour toutes vos questions, vous pouvez ajouter une question de calcul qui additionne toutes les factices comme :

`${QN1d}+${QN2d}+ etc`