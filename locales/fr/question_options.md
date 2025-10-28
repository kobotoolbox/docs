# Utilisation des options de question
<a href="../question_options.html">Read in English</a> | <a href="../es/question_options.html">Leer en español</a> | <a href="../ar/question_options.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/43a3384fad535287d1c7820457ab2d25a86877fc/source/question_options.md" class="reference">24 Sep 2025</a>

Après avoir ajouté une question, vous pouvez effectuer de nombreuses personnalisations en utilisant les options de question. Pour accéder à l'écran des options d'une question, cliquez sur son bouton <i class="k-icon k-icon-settings"></i> Paramètres.

![Options de question](/images/question_options/options2.png)

## Nom de la colonne de données

Le **Nom de la colonne de données** est l'identifiant unique (ID) de votre question.

Ce champ est obligatoire pour chaque question. Seuls les lettres, les chiffres et les traits de soulignement sont autorisés dans ce champ, et le champ doit commencer par une lettre ou un trait de soulignement. Vous pouvez saisir ce que vous voulez, par exemple `quel_est_votre_nom` ou `age`.

Le Nom de la colonne de données est important car il est utilisé dans les en-têtes de colonnes des tableaux et des feuilles de calcul après la collecte de vos données. Si vous souhaitez que votre feuille de calcul suive une convention de nommage spécifique, vous devez spécifier le nom de chacune de vos questions avant de déployer le formulaire en tant que projet de collecte de données.

## Indication d'aide (facultatif)

Les **Indications d'aide** sont des instructions supplémentaires que vous pouvez ajouter à vos questions sous forme de notes. Par défaut dans les formulaires web Enketo, les indications d'aide sont affichées sous un accordéon qui peut être développé et réduit comme indiqué ci-dessous.

![Indication d'aide dans les formulaires web Enketo](/images/question_options/guidance_hint_enketo.gif)

Dans [KoboCollect](kobocollect_on_android_latest.md), les indications d'aide ne sont pas affichées par défaut. Vous pouvez [choisir comment les indications d'aide doivent être affichées](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings) dans vos formulaires en allant dans Paramètres -> Gestion des formulaires -> Afficher les indications pour les questions. Vous avez ici 3 choix : Non, Oui - toujours affiché et Oui - toujours réduit.

![Indication d'aide dans KoboCollect](/images/question_options/guidance_hint_kobocollect.gif)

Les indications d'aide peuvent être utilisées comme notes internes lors de la collaboration avec d'autres personnes dans le développement du formulaire. Vous pouvez également les afficher sur des impressions ou comme instructions supplémentaires lors de la formation des enquêtrices et enquêteurs.

## Réponse obligatoire

Ce paramètre vous permet de spécifier si la question doit toujours recevoir une réponse ou non. Dans XLSForm, cela s'appelle `required`.

Dans KoboToolbox, il existe trois options pour la réponse obligatoire :

1. Oui - La question doit toujours recevoir une réponse. Si aucune réponse n'est fournie, l'utilisatrice ou l'utilisateur ne pourra pas passer à la question suivante ou sauvegarder le formulaire.
2. Non - La question n'est pas obligatoire et peut donc être ignorée manuellement.
3. Logique personnalisée - Vous pouvez définir une logique en utilisant du code XLSForm qui définira quand la question sera obligatoire. Par exemple, si vous définissez la logique personnalisée suivante `${age} > 18`, la question sera obligatoire lorsqu'une question précédente avec le nom de colonne de données `age` est supérieure à 18.

## Réponse par défaut (facultatif)

Cela permet de spécifier une réponse par défaut que l'enquêtrice ou l'enquêteur peut accepter ou modifier.

Dans la plupart des études, cela ne serait pas recommandé car cela pourrait créer un biais accidentel, mais cela peut être utile pour les questions de date ou d'heure où les réponses ont tendance à se situer autour d'un certain point connu.

Pour les questions <i class="k-icon k-icon-qt-date"></i> Date, la réponse par défaut doit être écrite au format `AAAA-MM-JJ` (par exemple `1974-12-31`).

Pour les questions <i class="k-icon k-icon-qt-select-one"></i> Sélection unique ou <i class="k-icon k-icon-qt-select-many"></i> Sélection multiple, la réponse doit être écrite en utilisant la Valeur unique (valeur xml) - et non l'étiquette (par exemple `premiere_annee` plutôt que `Première année`).

## Apparence (facultatif)

Ce paramètre avancé permet d'afficher la question de manière modifiée. Certaines options d'apparence ne seront disponibles qu'en fonction du [Type de question](question_types.md).

Pour une liste complète des valeurs d'apparence, consultez [la documentation sur l'apparence d'ODK](http://xlsform.org/en/#appearance).

![Options d'apparence de question](/images/question_options/appearance.png)