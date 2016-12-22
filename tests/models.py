from django.db import models

from django_catalogue.models import CatalogueModel


class PostType(CatalogueModel):
    fixtures_list = ['django_catalogue_test_fixtures']
    name = models.CharField(max_length=255, default='Type')
