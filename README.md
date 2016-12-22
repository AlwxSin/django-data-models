# Django Catalogue

Provides CatalogueModel that can't be modified rather than with loading data from fixture.

Also provides `load_catalogue_fixtures` management command to load fixtures defined in `fixtures` attribute for all catalogue models.


### Example

For a given class

```python
from django_catalogue import catalogue_model

class PostType(CatalogueModel):
    fixtures = ['post_types.json']
    ...
```


We can load fixtures
```
$ ./manage.py load_catalogue_fixtures

Loading post_types.json...
Installed 14 object(s) from 1 fixture(s)
```
