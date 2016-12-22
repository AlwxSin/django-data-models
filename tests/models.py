from django.db import models

from django_readonlymodel.models import ReadOnlyModel


class PostType(ReadOnlyModel):
    fixtures_list = ['django_readonlymodel_test_fixtures']
    name = models.CharField(max_length=255, default='Type')
