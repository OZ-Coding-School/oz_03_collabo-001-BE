from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create specified number of superusers with unique emails'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of superusers to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            email = f'{i}@admin.com'
            username = f'admin{i}'
            password = '1234'

            if not User.objects.filter(email=email).exists():
                try:
                    user = User(email=email, username=username)
                    user.set_password(password)
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {email}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error creating superuser {email}: {str(e)}'))
            else:
                self.stdout.write(self.style.WARNING(f'User {email} already exists'))
