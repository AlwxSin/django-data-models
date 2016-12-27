# Django Data Models

Provides DataModel that can't be used to load data from all DataModel children instances using `datamodels_loaddata`
and `datamodels_loaddata_default` command.

Main purpose of this application is to keep links to data along with your model definition and not to split it into
different places for deploy.

### API

```python
from datamodels import DataModel

class PostType(DataModel):
    ...

    class DataModelMeta:
        fixtures = ['django_datamodels_test_fixtures']
        default_fixtures = ['django_datamodels_test_default_fixtures']
        readonly = True
    ...
```

`DataModelMeta`'s attributes:

 - `fixtures` — data from these fixtures will be loaded on every `datamodels_loaddata` command
 - `default_fixtures` — data frome these fixtures will be loaded on every `datamodels_loaddata_default` command without
   updating existing objects.
 - `readonly` — model could not be modified/deleted and will raise an `DataModelsReadOnlyException`


### Commands
 - `datamodels_loaddata` loads fixtures given in `DataModelMeta.fixtures`
 - `datamodels_loaddata_default` loads fixtures given in `DataModelMeta.default_fixtures`

<a href="https://travis-ci.org/TriplePoint-Software/django-data-models">
<img src="https://travis-ci.org/TriplePoint-Software/django-data-models.svg?branch=master">
</a>