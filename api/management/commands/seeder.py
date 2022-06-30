from django.core.management.base import BaseCommand, CommandError
from api.models import Product
from django_seed import Seed


class Command(BaseCommand):
    help = 'Seed api databases'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--number',
            help='Number of records to create',
            type=int
        )

    def handle(self, *args, **options):
        number = options['number'] if options['number'] else 100

        try:
            seeder = Seed.seeder()
            seeder.add_entity(Product, number, {
                'name': lambda x: seeder.faker.first_name(),
                'code': lambda x: seeder.faker.unique.isbn10(),
                'price': lambda x: seeder.faker.pyfloat(left_digits=4,
                                                        right_digits=2,
                                                        min_value=1,
                                                        max_value=10000),
                'dimensions': lambda x: '%ix%i' % (seeder.faker.pyint(min_value=0, max_value=100, step=1),
                                                   seeder.faker.pyint(min_value=0, max_value=100, step=1)),
                'colors': lambda x: seeder.faker.color_name(),
                'tags': lambda x: seeder.faker.word(),
                'stock': lambda x: seeder.faker.pyint(min_value=0, max_value=10000, step=1)
            })
            seeder.execute()
        except Exception as e:
            raise CommandError(e)

        self.stdout.write(self.style.SUCCESS('%i products created successfully' % number))
