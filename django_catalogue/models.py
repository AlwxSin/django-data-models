from __future__ import unicode_literals

from django.db import models


class CatalogueReadOnlyException(Exception):
    pass


class CatalogueQuerySet(models.QuerySet):
    def delete(self):
        raise CatalogueReadOnlyException("You can't delete Catalogue objects")

    def _raw_delete(self, *args, **kwargs):
        raise CatalogueReadOnlyException("You can't delete Catalogue objects")

    def update(self, *args, **kwargs):
        raise CatalogueReadOnlyException("You can't update Catalogue objects")

    def _update(self, *args, **kwargs):
        raise CatalogueReadOnlyException("You can't update Catalogue objects")

    def select_for_update(self, *args, **kwargs):
        raise CatalogueReadOnlyException("You can't update Catalogue objects")


class CatalogueModel(models.Model):
    fixtures_list = None
    objects = CatalogueQuerySet.as_manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        raise CatalogueReadOnlyException("You can't update or create Catalogue objects")

    def delete(self, *args, **kwargs):
        raise CatalogueReadOnlyException("You can't delete Catalogue objects")
