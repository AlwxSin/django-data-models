from __future__ import unicode_literals

from django.db import models


class ReadModelOnlyException(Exception):
    pass


class RedaOnlyModelQuerySet(models.QuerySet):
    def delete(self):
        raise ReadModelOnlyException("You can't delete ReadOnlyModel objects")

    def _raw_delete(self, *args, **kwargs):
        raise ReadModelOnlyException("You can't delete ReadOnlyModel objects")

    def update(self, *args, **kwargs):
        raise ReadModelOnlyException("You can't update ReadOnlyModel objects")

    def _update(self, *args, **kwargs):
        raise ReadModelOnlyException("You can't update ReadOnlyModel objects")

    def select_for_update(self, *args, **kwargs):
        raise ReadModelOnlyException("You can't update ReadOnlyModel objects")


class ReadOnlyModel(models.Model):
    fixtures_list = None
    objects = RedaOnlyModelQuerySet.as_manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        raise ReadModelOnlyException("You can't update or create ReadOnlyModel objects")

    def delete(self, *args, **kwargs):
        raise ReadModelOnlyException("You can't delete ReadOnlyModel objects")
