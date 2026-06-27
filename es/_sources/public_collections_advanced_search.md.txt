# Búsqueda avanzada en Colecciones públicas

**_Ten en cuenta que la función de búsqueda está en desarrollo y planeamos agregar una sintaxis más fácil de usar en versiones futuras._**

## Comportamiento de búsqueda predeterminado

Cuando ingresas un término en la barra de búsqueda sin especificar un campo, tu consulta devolverá resultados donde ese término, independientemente de las mayúsculas o minúsculas, se encuentre en:

-   El nombre de la encuesta, recolección, pregunta, bloque o plantilla;
-   El nombre de usuario del propietario;
-   La descripción;
-   El resumen, que contiene todas las etiquetas de preguntas e idiomas;
-   El nombre de cualquier etiqueta asignada;
-   El UID del objeto.

Por ejemplo, una búsqueda predeterminada con el término: "_examples_", dará el siguiente resultado:

```
name__icontains:examples OR owner__username__icontains:examples OR
settings__description__icontains:examples OR summary__icontains:examples OR
tags__name__icontains:examples OR uid__icontains:examples
```

![examples](/images/public_collections_advanced_search/advanced_search_1.png)

## Operadores válidos para campos de búsqueda

El operador de campo es el valor que aparece después del último doble guión bajo en el campo de búsqueda, es decir, `__icontains`.

-   Para búsquedas de **texto** que _distinguen entre mayúsculas y minúsculas_, se pueden usar los siguientes operadores: `contains`, `exact`, `startswith`
-   Para búsquedas de **texto** que _no distinguen entre mayúsculas y minúsculas_: `icontains`, `iexact`, `istartswith`
-   Para búsquedas **numéricas**, los siguientes operadores son válidos: `exact`, `lt`, `lte`, `gt`, `gte`

Ten en cuenta que, de forma predeterminada, el operador `exact` está configurado, por lo que `name:foo` es equivalente a `name__exact:foo`.

## Entender la sintaxis de los campos de búsqueda

La sintaxis de doble guión bajo imita el comportamiento de la
[sintaxis de filtrado de objetos de Django](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
y permite recorrer relaciones entre objetos relacionados y jerarquías JSON, como las que se encuentran en el endpoint:

`https://kf.kobotoolbox.org/api/v2/assets/`

Por ejemplo, si un recurso tiene la siguiente configuración:

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

El objeto se puede buscar mediante los siguientes métodos:

```
settings__country__value:USA
```

![examples](/images/public_collections_advanced_search/advanced_search_2.png)

O de forma más flexible:

```
settings__country__value__icontains:usa
```

![examples](/images/public_collections_advanced_search/advanced_search_3.png)

## Usar el analizador de consultas

Por último, los campos de búsqueda descritos anteriormente se pueden combinar usando la sintaxis del
[analizador de consultas](https://github.com/kobotoolbox/kpi#searching) para realizar búsquedas más refinadas. Por ejemplo:

```
owner__username__icontains:foo AND tags__name__icontains:bar
```

O:

```
owner__username__icontains:foo AND NOT tags__name__icontains:bar
```

![examples](/images/public_collections_advanced_search/advanced_search_4.png)