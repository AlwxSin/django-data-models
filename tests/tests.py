from django.core.management import call_command
from django.test import TestCase

from datamodels.models import DataModelsReadOnlyException
from .models import PostType, ReadOnlyModel


class DataModelsReadOnlyTestCase(TestCase):

    def test_model(self):
        pt = ReadOnlyModel()
        self.assertRaises(DataModelsReadOnlyException, pt.save)
        self.assertRaises(DataModelsReadOnlyException, pt.delete)

    def test_manager(self):
        self.assertRaises(DataModelsReadOnlyException, ReadOnlyModel.objects.all().delete)
        self.assertRaises(DataModelsReadOnlyException, ReadOnlyModel.objects.all()._raw_delete)
        self.assertRaises(DataModelsReadOnlyException, ReadOnlyModel.objects.all().update)
        self.assertRaises(DataModelsReadOnlyException, ReadOnlyModel.objects.all()._update)
        self.assertRaises(DataModelsReadOnlyException, ReadOnlyModel.objects.all().select_for_update)
        self.assertRaises(DataModelsReadOnlyException, ReadOnlyModel.objects.create)

    def test_load_data(self):
        self.assertEqual(PostType.objects.count(), 0)
        call_command('datamodels_loaddata', verbosity=1, skip_checks=True)
        self.assertEqual(PostType.objects.count(), 1)
        pt = PostType.objects.get()
        self.assertEqual(pt.name, 'Test Name')

    def test_load_data_default(self):
        self.assertEqual(PostType.objects.count(), 0)
        call_command('datamodels_loaddata', verbosity=1, skip_checks=True)
        self.assertEqual(PostType.objects.count(), 1)

        old_pt = PostType.objects.get()

        call_command('datamodels_loaddata_default', verbosity=1, skip_checks=True)
        self.assertEqual(PostType.objects.count(), 2)
        post_type1 = PostType.objects.get(id=1)
        self.assertEqual(post_type1.name, old_pt.name)

        post_type2 = PostType.objects.get(id=2)
        self.assertEqual(post_type2.name, 'Test Name 2')

