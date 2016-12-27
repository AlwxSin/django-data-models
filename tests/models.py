from django.db import models

from datamodels.models import DataModel


class ReadOnlyModel(DataModel):
    class DataModelMeta:
        readonly = True

class PostType(DataModel):
    name = models.CharField(max_length=255, default='Type')

    class DataModelMeta:
        fixtures = ['django_datamodels_test_fixtures']
        default_fixtures = ['django_datamodels_test_default_fixtures']
        readonly = True

