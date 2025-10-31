# Inclure des réponses dans une autre question
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/aca19282c9a46e952209d16a75fce9e800f6ea1c/source/responses_inside_question.md" class="reference">5 oct. 2020</a>

Vous pouvez inclure la réponse d'une question (par exemple, inclure la réponse à la question « Quel âge avez-vous ? ») dans le libellé d'une autre question. Cela peut être utile pour de nombreuses raisons dans les formulaires avancés. Par exemple, vous pourriez vouloir confirmer qu'une réponse est vraiment correcte.

Référencer d'autres questions dans une autre question nécessite de leur donner un nom fixe via les paramètres de la question, tel que `age` ou `revenu`. Lorsque vous référencez d'autres questions, utilisez toujours le nom unique de la question dans le style de référencement de question, tel que

`${age}` ou `${revenu}`

Incluez simplement la référence à l'autre question parmi les autres mots de votre libellé. Par exemple, vous pouvez ajouter une nouvelle question avec le libellé

`Êtes-vous sûr(e) d'avoir ${age} ans ?`

![image](/images/responses_inside_question/question_name.gif)

Et vous pouvez également créer une logique de saut pour cette question afin qu'elle ne soit posée que lorsque la réponse concernant l'âge est inférieure à 18.

Notez que si vous référencez une question qui n'existe pas, cela créera une erreur lorsque vous essaierez de déployer votre formulaire. Assurez-vous toujours de référencer les questions avec leur nom exact, qui est également sensible à la casse. Par exemple, si votre question s'appelle `age`, vous ne pouvez pas utiliser `${Age}`. Vous pouvez facilement vérifier votre formulaire en cliquant sur Aperçu à tout moment.

![image](/images/responses_inside_question/preview.gif)

**Vous pouvez également référencer la réponse d'une question à choix unique/multiple et afficher la réponse au lieu du code en utilisant des questions de calcul masquées**

Si vous souhaitez référencer la réponse à une question à choix unique/multiple et afficher la réponse de la réponse (par exemple « Tout à fait d'accord ») au lieu de sa valeur encodée (par exemple « tout_a_fait_daccord »), vous pouvez :

1. Créer une question à choix unique/multiple, et donner à la question un nom de référence fixe via les paramètres de la question, tel que `instruction`. Et créer une question de calcul intermédiaire et saisir : `jr:choice-name(${instruction}, '${instruction}')`.

    ![image](/images/responses_inside_question/select_updated.gif)

2. Donner à cette question de calcul un nom de référence, tel que `instruction_calcul`. Dans votre nouvelle question, référencez cette question de calcul au lieu du nom donné à la question à choix unique/multiple.

    ![image](/images/responses_inside_question/calculate.gif)

3. Prévisualiser et valider le formulaire pour vous assurer que tout fonctionne comme prévu.

    ![image](/images/responses_inside_question/preview_calculate.gif)