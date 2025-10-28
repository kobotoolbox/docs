# Type de question Calcul
<a href="../calculate_questions.html">Read in English</a> | <a href="../es/calculate_questions.html">Leer en español</a> | <a href="../ar/calculate_questions.html">اقرأ باللغة العربية</a>

**Dernière mise à jour :**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/calculate_questions.md" class="reference">15
fév. 2022</a>

Certains formulaires avancés peuvent nécessiter qu'un calcul interne soit effectué dans le cadre du
formulaire (plutôt qu'après, lors de l'analyse). Cela peut être fait en
ajoutant un Calcul et en écrivant l'expression mathématique dans le champ
d'étiquette de la question.

![image](/images/calculate_questions/calculation.gif)

Une expression mathématique peut être aussi simple que `5 + 1`, mais il est
plus probable qu'elle inclue une référence à une autre question.

Référencer d'autres questions dans votre question de calcul nécessite de donner aux autres
questions des noms fixes via les paramètres de la question, tels que `girls` ou
`income`. Lorsque vous référencez ces questions, vous devez toujours utiliser le
nom de question unique (et non l'étiquette) - `${girls}` ou `${income}`

Par exemple, si vous souhaitez convertir la réponse à une question sur le
revenu de quelqu'un dans une autre devise (comme les francs rwandais en dollars américains), vous devez
écrire `${income} div 688`.

Vous pouvez également utiliser la réponse à cette question Calcul à d'autres fins, telles que
construire votre logique de saut (par exemple, ne poser une question de suivi qu'au-dessus d'un
certain seuil de revenu) ou en l'affichant dans une Note
([voir ici](responses_inside_question.md) pour obtenir de l'aide sur la façon d'afficher la
réponse à une question dans l'étiquette d'une autre question).

## Liste des fonctions disponibles

Il existe de nombreuses options différentes disponibles, telles que la fonction round()
(par exemple, `round(${int_1} div ${int_2}, 1`) arrondira le résultat d'une division à une
seule décimale). Pour une liste de certaines des nombreuses expressions mathématiques qui
peuvent être utilisées dans ce champ, veuillez consulter
[les spécifications XForm sur les fonctions de calcul](https://docs.getodk.org/form-operators-functions/)
pour le contexte technique de toutes les fonctions disponibles dans KoboToolbox et
XLSForms. Pour une utilisation avancée des calculs dans KoboToolbox, veuillez vous référer à
[cet article](advanced_calculate.md).

## Liste des opérateurs mathématiques disponibles

| Opérateur              | Description                        |
| :--------------------- | :--------------------------------- |
| `+`                    | Addition                           |
| `-`                    | Soustraction                       |
| `*`                    | Multiplication                     |
| `div`                  | Division                           |
| `=`                    | Égal                               |
| `!=`                   | Différent de                       |
| `<`                    | Inférieur à                        |
| `<=`                   | Inférieur ou égal à                |
| `>`                    | Supérieur à                        |
| `>=`                   | Supérieur ou égal à                |
| `or`                   | Ou                                 |
| `and`                  | Et                                 |
| `mod`                  | Modulo (reste de la division)      |
| `pow([base], [power])` | Puissance / exposant               |