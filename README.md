# Django Data Models

Provides DataModel that can't be used to describe fixtures in `fixtures` attribute to load using
`datamodels_loaddata` command.

### Example

For a given class

```python
from datamodels import DataModel

class PostType(DataModel):
    fixtures = ['post_types.json']
    ...
```


We can load fixtures
```
$ ./manage.py load_readonly_fixtures

Loading post_types.json...
Installed 14 object(s) from 1 fixture(s)
```

<a href="https://travis-ci.org/TriplePoint-Software/django-data-models"><img src="https://travis-ci.org/TriplePoint-Software/django-data-models.svg?branch=master"></a>