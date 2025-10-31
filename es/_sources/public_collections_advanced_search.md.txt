# Búsqueda Avanzada en Colecciones Públicas

**Última actualización:**
<a href="https://github.com/kobotoolbox/docs/blob/a6ae76d4d566c1139914f03ba8452fdbf122cf11/source/public_collections_advanced_search.md" class="reference">4
Mar 2021</a>

**_Ten en cuenta que la capacidad de búsqueda es un trabajo en progreso, y planeamos
agregar una sintaxis más fácil de usar en futuras versiones._**

## El Comportamiento de Búsqueda Predeterminado

Cuando ingresas un término en la barra de búsqueda sin especificar un campo, tu consulta
devolverá resultados donde ese término, independientemente de las mayúsculas, se pueda encontrar
en:

-   El nombre de la encuesta, colección, pregunta, bloque o plantilla;
-   El nombre de usuario del/de la propietario/a;
-   La descripción;
-   El resumen, que contiene todas las etiquetas de preguntas e idiomas;
-   El nombre de cualquier etiqueta asignada;
-   El UID del objeto.

Por ejemplo, una búsqueda predeterminada con el término: "_examples_", resultará en lo
siguiente:

```
name__icontains:examples OR owner__username__icontains:examples OR
settings__description__icontains:examples OR summary__icontains:examples OR
tags__name__icontains:examples OR uid__icontains:examples
```

![examples](/images/public_collections_advanced_search/advanced_search_1.png)

## Operadores de Campo de Búsqueda Válidos

El operador de campo es el valor después del último guion bajo doble en el campo
de búsqueda, es decir, `__icontains`.

-   Para búsquedas de **texto** _sensibles a mayúsculas_, se pueden usar los siguientes operadores:
    `contains`, `exact`, `startswith`
-   Para búsquedas de **texto** _insensibles a mayúsculas_: `icontains`, `iexact`,
    `istartswith`
-   Para búsqueda **numérica**, los siguientes operadores son válidos: `exact`, `lt`,
    `lte`, `gt`, `gte`

Ten en cuenta que por defecto se establece el operador `exact`, por lo tanto `name:foo` es
equivalente a `name__exact:foo`

## Comprender la Sintaxis del Campo de Búsqueda

La sintaxis de guion bajo doble imita el comportamiento de
[la sintaxis de filtrado de objetos de Django](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
y permite recorrer relaciones de objetos relacionados y jerarquías JSON,
como las que se ven en el endpoint:

`https://kf.kobotoolbox.org/api/v2/assets/`

Por ejemplo, si un activo tiene la siguiente configuración:

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

El objeto se podría buscar a través de los siguientes métodos:

```
settings__country__value:USA
```

![examples](/images/public_collections_advanced_search/advanced_search_2.png)

O de manera más amplia:

```
settings__country__value__icontains:usa
```

![examples](/images/public_collections_advanced_search/advanced_search_3.png)

## Usar el Analizador de Consultas

Finalmente, los campos de búsqueda descritos anteriormente se pueden combinar usando la
sintaxis del [analizador de consultas](https://github.com/kobotoolbox/kpi#searching) para
búsquedas más refinadas. Por ejemplo:

```
owner__username__icontains:foo AND tags__name__icontains:bar
```

O:

```
owner__username__icontains:foo AND NOT tags__name__icontains:bar
```

![examples](/images/public_collections_advanced_search/advanced_search_4.png)