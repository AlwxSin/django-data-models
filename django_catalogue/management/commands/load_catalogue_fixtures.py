from django.core.management import call_command
from django.core.management.base import BaseCommand
import django.apps

from ...models import CatalogueModel


class Command(BaseCommand):
    help = 'Loads data for all Catalogue Models'

    def handle(self, *args, **options):
        for model in django.apps.apps.get_models():
            if not issubclass(model, CatalogueModel):
                continue
            if not model.fixtures_list:
                continue

            for fixure in model.fixtures_list:
                print("Loading %s..." % fixure)
                call_command('loaddata', fixure, verbosity=1, skip_checks=True)
                print('')

