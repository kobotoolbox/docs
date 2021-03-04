# Public Collections Advanced Search

**_Note that the user-friendliness of the advanced search will improve in the
coming months._**

### The Default Search Behaviour

When you enter a term into the search bar, the following fields are searched by
default when no explicit field is given (combined with the `OR` operator):
`name__icontains`, `owner__username__icontains`,
`settings__description__icontains`, `summary__icontains`,
`tags__name__icontains`, `uid__icontains`.

For example, a default search with the term: "_examples_", will result in the
following:

```
name__icontains:examples OR owner__username__icontains:examples OR
settings__description__icontains:examples OR summary__icontains:examples OR
tags__name__icontains:examples OR uid__icontains:examples
```

![examples](/images/public_collections_advanced_search/advanced_search_1.png)

### Valid Search Field Operators

The field operator is the value after the last double-underscore in the search
field, i.e. `__icontains`.

- For _case-sensitive_ **text** searches, the following operators can be used:
  `contains`, `exact`, `startswith`
- For _case-insensitive_ **text** searches: `icontains`, `iexact`, `istartswith`
- For **numeric** search, the following operators are valid: `lte`, `gte`

Note that by default the `exact` operator is set, therefore `name:foo` is
equivalent to `name__exact:foo`

### Understanding the Search Field Syntax

The double underscore syntax mimics the behaviour of [Django's object filtering
syntax](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
and it allows one to traverse related object relationships and JSON hierarchies,
such as those seen at the endpoint:

`https://kf.kobotoolbox.org/api/v2/assets/`

For example, if an asset has the following settings:

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

The object could be searched through the following methods:

```
settings__country__value:USA
```

![examples](/images/public_collections_advanced_search/advanced_search_2.png)

Or more loosely:

```
settings__country__value__icontains:usa
```

![examples](/images/public_collections_advanced_search/advanced_search_3.png)

### Using the Query Parser

Finally, the search fields described above can be combined using the [query
parser](https://github.com/kobotoolbox/kpi#searching) syntax for more refined
searches. For example:

```
owner__username__icontains:foo AND tags__name__icontains:bar
```

Or:

```
owner__username__icontains:foo AND NOT tags__name__icontains:bar
```

![examples](/images/public_collections_advanced_search/advanced_search_4.png)

