from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='astr@sky.ru',
            first_name='Александр',
            last_name='Струльков',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        user.set_password('gizn1247')
        user.save()
