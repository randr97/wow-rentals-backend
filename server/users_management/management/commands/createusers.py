from django.core.management.base import BaseCommand

from users_management.models import User


class Command(BaseCommand):
    help = "Adds default users"

    def add_arguments(self, parser):
        # parser.add_argument("poll_ids", nargs="+", type=int)
        pass

    def handle(self, *args, **options):
        admin = {
            "email": "admin@gmail.com",
            "phone": "7325229576",
            "first_name": "Rohit",
            "last_name": "Shrothrium Srinath",
            "password": "password",
            "address_street": "544 Bayridge Pkwy",
            "address_city": "Brooklyn",
            "address_state": "NY",
            "address_zipcode": "11209"
        }
        u = User(is_superuser=True, is_staff=True, **admin)
        u.set_password(admin['password'])
        u.save()
        self.stdout.write(
            self.style.SUCCESS('Admin user created')
        )
