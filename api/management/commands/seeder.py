from django.core.management.base import BaseCommand


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
        self.stdout.write(self.style.SUCCESS(number))
