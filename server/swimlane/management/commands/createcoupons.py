from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Adds default users"

    def add_arguments(self, parser):
        # parser.add_argument("poll_ids", nargs="+", type=int)
        pass

    def handle(self, *args, **options):
        pass
