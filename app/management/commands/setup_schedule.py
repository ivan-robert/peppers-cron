from django.core.management.base import BaseCommand
from django_q.models import Schedule


class Command(BaseCommand):
    help = 'Setup scheduled tasks for django-q'

    def handle(self, *args, **options):
        # Delete existing schedule if it exists
        Schedule.objects.filter(name='log_random_number').delete()
        
        # Create the schedule - every 10 seconds
        Schedule.objects.create(
            name='log_random_number',
            func='app.tasks.log_random_number',
            schedule_type=Schedule.MINUTES,
            minutes=60,  # 1h
            repeats=-1,  # Repeat indefinitely
        )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created scheduled task: log_random_number (every 10 seconds)')
        )

