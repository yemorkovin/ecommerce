from django.core.management.base import BaseCommand
from shop.fixtures.dummy_data import create_categories, create_products


class Command(BaseCommand):
    help = 'Generates dummy categories and products'

    def add_arguments(self, parser):
        parser.add_argument(
            '--products',
            type=int,
            default=50,
            help='Number of products to generate'
        )

    def handle(self, *args, **options):
        self.stdout.write("Creating dummy categories...")
        create_categories()

        self.stdout.write(f"Creating {options['products']} dummy products...")
        create_products(options['products'])

        self.stdout.write(
            self.style.SUCCESS('Successfully generated dummy data')
        )