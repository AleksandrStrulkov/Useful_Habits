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
    print("Привет таска запущена")
    requests.get(
        url=f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage',
        data={
            'chat_id': USER_ID,
            'text': f'Через 1 минуту в {habit.time_when_execute} вам надо выполнить: "{habit.action}"!!! '
                    f'Место выполнения: "{habit.place}"! '
                    f'Время выполнения: {habit.lead_time} минут! '
                    f'После выполнение вас ждет награда: " {habit.reward} " '
                    f'или выполнение: "{habit.related_habit.action}"!!!'
        }
    )
