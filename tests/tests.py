from django.core.management import call_command
from django.test import TestCase

from django_readonlymodel.models import ReadModelOnlyException
from .models import PostType


class ReadOnlyModelTestCase(TestCase):

    def test_model(self):
        pt = PostType()
        self.assertRaises(ReadModelOnlyException, pt.save)
        self.assertRaises(ReadModelOnlyException, pt.delete)

    def test_manager(self):
        self.assertRaises(ReadModelOnlyException, PostType.objects.all().delete)
        self.assertRaises(ReadModelOnlyException, PostType.objects.all()._raw_delete)
        self.assertRaises(ReadModelOnlyException, PostType.objects.all().update)
        self.assertRaises(ReadModelOnlyException, PostType.objects.all()._update)
        self.assertRaises(ReadModelOnlyException, PostType.objects.all().select_for_update)
        self.assertRaises(ReadModelOnlyException, PostType.objects.create)

    def test_load_data(self):
        self.assertEqual(PostType.objects.count(), 0)
        call_command('load_readonly_fixtures', verbosity=1, skip_checks=True)
        self.assertEqual(PostType.objects.count(), 1)
        pt = PostType.objects.get()
        self.assertEqual(pt.name, 'Test Name')

