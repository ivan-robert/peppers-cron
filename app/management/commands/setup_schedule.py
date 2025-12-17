from django.core.management.base import BaseCommand
from django_q.models import Schedule
from django_q.tasks import schedule


class Command(BaseCommand):
    help = 'Setup scheduled tasks for django-q'

    def handle(self, *args, **options):
        # Delete existing schedule if it exists
        Schedule.objects.filter(name='log_random_number').delete()

        schedule(
            func='app.masterclass.log_random_number',
            schedule_type=Schedule.MINUTES,
            minutes=1/10,  # 6 seconds
            repeats=-1,  # Repeat indefinitely
            hook='app.tasks.print_result_hook',
        )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created scheduled task: log_random_number (every 10 seconds)')
        )

