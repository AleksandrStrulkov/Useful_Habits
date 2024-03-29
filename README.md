## Курсовая 7. Трекер полезных привычек.
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена 
приобретению новых полезных привычек и искоренению старых плохих привычек. 
Заказчик прочитал книгу, впечатлился и обратился к нам с запросом реализовать 
трекер полезных привычек.
В рамках учебного курсового проекта реализована бэкенд-часть SPA веб-приложения. 
* Перечень зависимостей в данном проекте:
1. python = "^3.11"
2. django = "4.2.10"
3. pillow = "^10.2.0"
4. psycopg2 = "^2.9.9"
5. python-dotenv = "^1.0.1"
6. djangorestframework = "^3.14.0"
7. redis = "^5.0.1"
8. routers = "^0.10.1"
9. django-filter = "^23.5"
10. djangorestframework-simplejwt = "^5.3.1"
11. generics = "^6.0.0"
12. coverage = "^7.4.1"
13. coreapi = "^2.3.3"
14. pyyaml = "^6.0.1"
15. celery = "^5.3.6"
16. django-celery-beat = "^2.5.0"
17. pyopenssl = "^24.0.0"
18. requests = "^2.31.0"
19. django-cors-headers = "^4.3.1"
20. drf-yasg = "^1.21.7"
21. flake8 = "^7.0.0"

* Перечень применимых настроек, функциональностей и реализации: 

1. Настройка CORS. +
2. Интеграция с Telegram. +
3. Реализована пагинация. +
4. Использованы переменные окружения. +
5. Все необходимые модели описаны или переопределены. +
6. Все необходимые эндпоинты реализованы. +
7. Настройка всех необходимых валидаторов. +
8. Описанные права доступа заложены. +
9. Настроены отложенные задачи через Celery. +
10. Проект покрыт тестами как минимум на 80%. +
11. Код оформлен в соответствии с лучшими практиками. +
12. Имеется список зависимостей. +
13. Результат проверки Flake8 равен 100%, при исключении миграций. +
14. Решение выложен на GitHub. +

* Docker compose

1. Собрать образ и запустить контейнер с помощью команды: - docker compose up --build
2. Для остановки и удаления контейнеров используйте Ctrl + C.
3. Для остановки контейнеров и удаления созданных ресурсов выполните команду: - docker-compose down

