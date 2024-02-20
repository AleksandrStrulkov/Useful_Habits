from datetime import datetime, timedelta, time

from django_celery_beat.models import PeriodicTask, CrontabSchedule
from config import settings


def create_reminder(habit):
    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.time_when_execute.minute - 1,
        hour=habit.time_when_execute.hour,
        day_of_week='*' if habit.periodicity == 1 else '2,4,6' if habit.periodicity == 2
        else '1,4,7' if habit.periodicity == 3 else '6',
        # day_of_week='*' if habit.periodicity == 1 else f'*/{habit.periodicity}',
        timezone=settings.TIME_ZONE
    )

    PeriodicTask.objects.create(
        crontab=crontab_schedule,
        name=f'telegram_message_{habit.id}',
        task='habit_app.tasks.telegram_message',
        args=[habit.id],
    )


def delete_reminder(habit):
    task_name = f'telegram_message_{habit.id}'
    PeriodicTask.objects.filter(name=task_name).delete()


def update_reminder(habit):
    delete_reminder(habit)
    create_reminder(habit)
