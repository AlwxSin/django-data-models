# Django ReadOnlyModel

Provides ReadOnlyModel that can't be modified rather than with loading data from fixture.

Also provides `load_readonly_fixtures` management command to load fixtures defined in `fixtures` attribute for all
registerd read-only models.


### Example

For a given class

```python
from django_readonlymodel import ReadOnlyModel

class PostType(ReadOnlyModel):
    fixtures = ['post_types.json']
    ...
```


We can load fixtures
```
$ ./manage.py load_readonly_fixtures

Loading post_types.json...
Installed 14 object(s) from 1 fixture(s)
```
