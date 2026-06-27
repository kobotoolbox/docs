# Inclure des réponses dans une autre question

Vous pouvez inclure la réponse d'une question (par exemple, la réponse à la question « Quel est votre âge ? ») dans le libellé d'une autre question. Cela peut être utile dans de nombreux cas pour des formulaires avancés. Par exemple, vous pouvez souhaiter confirmer qu'une réponse est bien correcte.

Pour référencer d'autres questions dans le libellé d'une question, vous devez leur attribuer un nom fixe dans les paramètres de la question, comme `age` ou `income`. Lorsque vous référencez d'autres questions, utilisez toujours le nom unique de la question dans le format de référencement de questions, par exemple :

`${age}` ou `${income}`

Incluez simplement la référence à l'autre question parmi les autres mots de votre libellé. Par exemple, vous pouvez ajouter une nouvelle question avec le libellé suivant :

`Are you sure you are ${age} years old?`

![image](/images/responses_inside_question/question_name.gif)

Vous pouvez également créer une logique de saut pour cette question afin qu'elle ne soit posée que lorsque la réponse à la question sur l'âge est inférieure à 18.

Notez que si vous référencez une question qui n'existe pas, cela génèrera une erreur lorsque vous tenterez de déployer votre formulaire. Veillez toujours à référencer les questions avec leur nom exact, qui est également sensible à l'utilisation de majuscules et de minuscules. Par exemple, si votre question s'appelle `age`, vous ne pouvez pas utiliser `${Age}`. Vous pouvez facilement vérifier votre formulaire en cliquant sur Aperçu à tout moment.

![image](/images/responses_inside_question/preview.gif)

**Vous pouvez également référencer la réponse d'une question de type Choix unique ou Choix multiple et afficher la réponse au lieu du code à l'aide de questions de type Calcul masquées**

Si vous souhaitez référencer la réponse à une question de type Choix unique ou Choix multiple et afficher le libellé de la réponse (par exemple, « Tout à fait d'accord ») plutôt que sa valeur encodée (par exemple, « strongly_agr »), vous pouvez procéder comme suit :

1. Créez une question de type Choix unique ou Choix multiple, et attribuez-lui un nom de référence fixe dans les paramètres de la question, comme `instruction`. Créez ensuite une question de type Calcul intermédiaire et saisissez : `jr:choice-name(${instruction}, '${instruction}')`.

    ![image](/images/responses_inside_question/select_updated.gif)

2. Attribuez un nom de référence à cette question de type Calcul, par exemple `instruction_calculation`. Dans votre nouvelle question, référencez cette question de type Calcul plutôt que le nom attribué à la question de type Choix unique ou Choix multiple.

    ![image](/images/responses_inside_question/calculate.gif)

3. Prévisualisez et validez le formulaire pour vous assurer que tout fonctionne comme prévu.

    ![image](/images/responses_inside_question/preview_calculate.gif)