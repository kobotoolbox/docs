# Recherche avancée dans les Collections publiques

**Dernière mise à jour :**
<a href="https://github.com/kobotoolbox/docs/blob/a6ae76d4d566c1139914f03ba8452fdbf122cf11/source/public_collections_advanced_search.md" class="reference">4
mars 2021</a>

**_Veuillez noter que la fonctionnalité de recherche est en cours de développement et nous prévoyons d'ajouter une syntaxe plus conviviale dans les prochaines versions._**

## Le comportement de recherche par défaut

Lorsque vous saisissez un terme dans la barre de recherche sans spécifier de champ, votre requête renverra des résultats où ce terme, quelle que soit la casse, peut être trouvé dans :

-   Le nom de l'enquête, de la collection, de la question, du bloc ou du modèle ;
-   Le nom d'utilisateur du propriétaire ;
-   La description ;
-   Le résumé, qui contient toutes les étiquettes de questions et les langues ;
-   Le nom de toute balise attribuée ;
-   L'UID de l'objet.

Par exemple, une recherche par défaut avec le terme : « _examples_ », donnera le résultat suivant :

```
name__icontains:examples OR owner__username__icontains:examples OR
settings__description__icontains:examples OR summary__icontains:examples OR
tags__name__icontains:examples OR uid__icontains:examples
```

![examples](/images/public_collections_advanced_search/advanced_search_1.png)

## Opérateurs de champ de recherche valides

L'opérateur de champ est la valeur après le dernier double trait de soulignement dans le champ de recherche, c'est-à-dire `__icontains`.

-   Pour les recherches de **texte** _sensibles à la casse_, les opérateurs suivants peuvent être utilisés :
    `contains`, `exact`, `startswith`
-   Pour les recherches de **texte** _insensibles à la casse_ : `icontains`, `iexact`,
    `istartswith`
-   Pour les recherches **numériques**, les opérateurs suivants sont valides : `exact`, `lt`,
    `lte`, `gt`, `gte`

Notez que par défaut l'opérateur `exact` est défini, donc `name:foo` est
équivalent à `name__exact:foo`

## Comprendre la syntaxe du champ de recherche

La syntaxe à double trait de soulignement imite le comportement de la
[syntaxe de filtrage d'objets de Django](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
et elle permet de parcourir les relations d'objets liés et les hiérarchies JSON,
comme celles visibles au point de terminaison :

`https://kf.kobotoolbox.org/api/v2/assets/`

Par exemple, si un actif a les paramètres suivants :

```
{
    ...
    "settings": {
        ...
        "country": {
            "label": "United States",
            "value": "USA"
        }
        ...
    },
    ...
}
```

L'objet pourrait être recherché par les méthodes suivantes :

```
settings__country__value:USA
```

![examples](/images/public_collections_advanced_search/advanced_search_2.png)

Ou de manière plus souple :

```
settings__country__value__icontains:usa
```

![examples](/images/public_collections_advanced_search/advanced_search_3.png)

## Utilisation de l'analyseur de requêtes

Enfin, les champs de recherche décrits ci-dessus peuvent être combinés en utilisant la
syntaxe de l'[analyseur de requêtes](https://github.com/kobotoolbox/kpi#searching) pour des
recherches plus précises. Par exemple :

```
owner__username__icontains:foo AND tags__name__icontains:bar
```

Ou :

```
owner__username__icontains:foo AND NOT tags__name__icontains:bar
```

![examples](/images/public_collections_advanced_search/advanced_search_4.png)