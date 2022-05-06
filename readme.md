Инструкция для запуска проекта:

Запустить Docker

git clone https://github.com/IlyasDevelopment/Jservice

Перейти в папку с проектом cd Jservice

docker-compose build

docker-compose run app alembic revision --autogenerate -m “FirstMigration”

Иногда при запросе на создание миграции на стороне сервера может происходить ошибка, в таком случае нужно продублировать команду выше, все сработает.

docker-compose run app alembic upgrade head

docker-compose up

Можно перейти на http://localhost:8000/, убедиться, что сервер работает

http://localhost:8000/questions/ вернет пустой список, так как база данных изначально пустая. Но данные будут сохраняться при рестарте контейнера.

По адресу http://localhost:7080 откроется сервис администрирования базой данных PostgreSQL. Логин: admin@admin.com Пароль: adminpass

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/1.png "Таблица")

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/2.png "Таблица")

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/3.png "Таблица")

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/4.png "Таблица")

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/5.png "Таблица")

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/6.png "Таблица")

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/7.png "Таблица")

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/8.png "Таблица")

Пароль postgrespass

Можно убедиться и через http://localhost:8000/questions/

Ctrl + C для остановки проекта
