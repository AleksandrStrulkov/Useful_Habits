from datetime import timedelta

from django.utils.timezone import now
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from habit_app.models import Habit
from users.models import User


class HabitListTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='astrulkov@yandex.ru')
        self.user.set_password('1247')
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            name='Полезная',
            place='Тест место',
            time_when_execute='12:00',
            action='Тест действие',
            nice_habit=False,
            periodicity=1,
            reward='Тест вознаграждение',
            lead_time="00:02:00",
            is_public=True
        )

    def test_create_habit(self):
        """ Тестирование создания привычки """

        # задаем данные для создания привычки
        data_habit = {
            'owner': self.user.pk,
            'name': 'Полезная',
            'place': 'Тест место',
            'time_when_execute': '05:30',
            'action': 'Тест действие',
            'nice_habit': False,
            'periodicity': 1,
            'reward': 'Тест подарок',
            'lead_time': "00:02:00",
            'is_public': True,
        }

        # создаем привычку
        response = self.client.post('/api/habit/create/', data=data_habit)

        # проверка ответа на создание привычки
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # проверяем на существование объектов привычек
        self.assertTrue(Habit.objects.all().exists())

    def test_list_habit(self):
        """ Тестирование списка привычек """

        # получаем список привычек
        response = self.client.get('/api/habit/')

        # проверяем ответ на получение списка привычек
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results': [{'id': 6,
                          'owner': 5,
                          'name': 'Полезная',
                          'date': (now() + timedelta(hours=3)).strftime("%d.%m.%Y %H:%M"),
                          'place': 'Тест место',
                          'time_when_execute': '12:00:00',
                          'action': 'Тест действие',
                          'nice_habit': False,
                          'related_habit': None,
                          'periodicity': 1,
                          'reward': 'Тест вознаграждение',
                          'lead_time': "00:02:00",
                          'is_public': True},
                         ]
             }
        )

    def test_detail_habit(self):
        """ Тестирование информации о привычке """

        # получаем детали привычки
        response = self.client.get(reverse('habit_app:detail_get_habit', args=[self.habit.id]))

        # проверяем ответ на получение привычки
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'id': 5,
             'owner': 4,
             'name': 'Полезная',
             'date': (now() + timedelta(hours=3)).strftime("%d.%m.%Y %H:%M"),
             'place': 'Тест место',
             'time_when_execute': '12:00:00',
             'action': 'Тест действие',
             'nice_habit': False,
             'related_habit': None,
             'periodicity': 1,
             'reward': 'Тест вознаграждение',
             'lead_time': '00:02:00',
             'is_public': True}
        )

    def test_change_habit(self):
        """ Тестирование изменения привычки """

        # данные для изменения привычки
        data_habit_change = {
            'name': 'Полезная',
            'place': 'Тест изменение',
            'time_when_execute': '08:30:00',
            'action': 'Тест изменение',
            'nice_habit': False,
            'related_habit': 1,
            'periodicity': 3,
            'reward': '',
            'lead_time': "00:00:30",
            'is_public': True
        }

        # получаем детали привычки
        response = self.client.put(reverse('habit_app:put_patch_habit', args=[self.habit.id]),
                data=data_habit_change)

        # проверяем ответ на получение привычки
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'id': 1,
             'owner': 1,
             'name': 'Полезная',
             'date': (now() + timedelta(hours=3)).strftime("%d.%m.%Y %H:%M"),
             'place': 'Тест изменение',
             'time_when_execute': '08:30:00',
             'action': 'Тест изменение',
             'nice_habit': False,
             'related_habit': 1,
             'periodicity': 3,
             'reward': '',
             'lead_time': '00:00:30',
             'is_public': True}
        )

    def test_delete_habit(self):
        """ Тестирование удаления привычки """

        response = self.client.delete(reverse('habit_app:delete_habit', args=[self.habit.id]))

        # проверяем ответ на получение привычки
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


