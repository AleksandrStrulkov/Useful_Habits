import requests
from celery import shared_task
from config import settings
from habit_app.models import Habit

URL = settings.TELEGRAM_URL
TOKEN = settings.TELEGRAM_TOKEN
USER_ID = settings.USER_ID_TELEGRAM


@shared_task
def telegram_message(*args, **kwargs):
    habit = Habit.objects.get(id=args[0])
    print(habit)
    print("Привет таска запущена")
    habit_time = habit.time_when_execute.strftime('%H:%M')

    if not habit.nice_habit:
        text = f'Сейчас, в {habit_time} вам надо выполнить: "{habit.action}"!!! '
        f'Место выполнения: "{habit.place}"! '
        create_requests(text)

        if habit.related_habit:
            text = f'За это вам полагается сделать: "{habit.related_habit.action}"'
            create_requests(text)

        elif habit.reward:
            text = f'За это порадуйте себя этим: "{habit.reward}"'
            create_requests(text)


def create_requests(text):
    requests.post(
        url=f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage',
        data={
            'chat_id': USER_ID,
            'text': text})
