from django.core.management import call_command
from django.test import TestCase

from django_catalogue.models import CatalogueReadOnlyException
from .models import PostType


class CatalogueModelTestCase(TestCase):

    def test_model(self):
        pt = PostType()
        self.assertRaises(CatalogueReadOnlyException, pt.save)
        self.assertRaises(CatalogueReadOnlyException, pt.delete)

    def test_manager(self):
        self.assertRaises(CatalogueReadOnlyException, PostType.objects.all().delete)
        self.assertRaises(CatalogueReadOnlyException, PostType.objects.all()._raw_delete)
        self.assertRaises(CatalogueReadOnlyException, PostType.objects.all().update)
        self.assertRaises(CatalogueReadOnlyException, PostType.objects.all()._update)
        self.assertRaises(CatalogueReadOnlyException, PostType.objects.all().select_for_update)
        self.assertRaises(CatalogueReadOnlyException, PostType.objects.create)

    def test_load_data(self):
        self.assertEqual(PostType.objects.count(), 0)
        call_command('load_catalogue_fixtures', verbosity=1, skip_checks=True)
        self.assertEqual(PostType.objects.count(), 1)
        pt = PostType.objects.get()
        self.assertEqual(pt.name, 'Test Name')

