# Recherche avancée dans les collections publiques

**_Veuillez noter que la fonctionnalité de recherche est en cours de développement et que nous prévoyons d'ajouter une syntaxe plus facile à utiliser dans les prochaines versions._**

## Comportement de recherche par défaut

Lorsque vous saisissez un terme dans la barre de recherche sans spécifier de champ, votre requête retournera les résultats où ce terme, quelle que soit l'utilisation de majuscules ou de minuscules, peut être trouvé dans :

-   Le nom de l'enquête, de la collection, de la question, du bloc ou du modèle ;
-   Le nom d'utilisateur du propriétaire ;
-   La description ;
-   Le résumé, qui contient tous les libellés de questions et les langues ;
-   Le nom de tout tag attribué ;
-   L'UID de l'objet.

Par exemple, une recherche par défaut avec le terme : « _examples_ » donnera le résultat suivant :

```
name__icontains:examples OR owner__username__icontains:examples OR
settings__description__icontains:examples OR summary__icontains:examples OR
tags__name__icontains:examples OR uid__icontains:examples
```

![examples](/images/public_collections_advanced_search/advanced_search_1.png)

## Opérateurs de champ de recherche valides

L'opérateur de champ est la valeur qui suit le dernier double tiret bas dans le champ de recherche, c'est-à-dire `__icontains`.

-   Pour les recherches de **texte** _sensibles à l'utilisation de majuscules et de minuscules_, les opérateurs suivants peuvent être utilisés : `contains`, `exact`, `startswith`
-   Pour les recherches de **texte** _non sensibles à l'utilisation de majuscules et de minuscules_ : `icontains`, `iexact`, `istartswith`
-   Pour les recherches **numériques**, les opérateurs suivants sont valides : `exact`, `lt`, `lte`, `gt`, `gte`

Notez que par défaut l'opérateur `exact` est défini, par conséquent `name:foo` est équivalent à `name__exact:foo`

## Comprendre la syntaxe des champs de recherche

La syntaxe avec double tiret bas reproduit le comportement de la
[syntaxe de filtrage d'objets de Django](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
et permet de parcourir les relations entre objets liés et les hiérarchies JSON, telles que celles visibles au niveau du point de terminaison :

`https://kf.kobotoolbox.org/api/v2/assets/`

Par exemple, si un objet possède les paramètres suivants :

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

L'objet peut être recherché à l'aide des méthodes suivantes :

```
settings__country__value:USA
```

![examples](/images/public_collections_advanced_search/advanced_search_2.png)

Ou de manière plus souple :

```
settings__country__value__icontains:usa
```

![examples](/images/public_collections_advanced_search/advanced_search_3.png)

## Utiliser le parseur de requêtes

Enfin, les champs de recherche décrits ci-dessus peuvent être combinés à l'aide de la syntaxe du
[parseur de requêtes](https://github.com/kobotoolbox/kpi#searching) pour des recherches plus précises. Par exemple :

```
owner__username__icontains:foo AND tags__name__icontains:bar
```

Ou :

```
owner__username__icontains:foo AND NOT tags__name__icontains:bar
```

![examples](/images/public_collections_advanced_search/advanced_search_4.png)