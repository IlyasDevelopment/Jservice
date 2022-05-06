Инструкция для запуска проекта:

Запустить Docker

git clone https://github.com/IlyasDevelopment/Jservice

Перейти в папку с проектом cd Jservice

docker-compose build

docker-compose run app alembic revision --autogenerate -m “FirstMigration”

Иногда при запросе на создание миграции на стороне сервера может происходить ошибка, в таком случае нужно продублировать команду выше, все сработает.

docker-compose run app alembic upgrade head

docker-compose up

Можно перейти на http://localhost:8000/, убедиться, что сервер работает.

http://localhost:8000/questions/ вернет пустой список, так как база данных изначально пустая. Но данные будут сохраняться при рестарте контейнера.

По адресу http://localhost:7080 откроется сервис администрирования базой данных PostgreSQL.

Логин: admin@admin.com

Пароль: adminpass

При первом запуске необходимо зарегистрировать сервер, для этого переходим в Add New Server.

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/1.png "Таблица")

Name: db, далее переходим в пункт Connection.

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/2.png "Таблица")

Hostname/address: db, Urename: postgres, Password: postgrespass

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/3.png "Таблица")

Сначала база данных quiz_db будет неактивна, нужно её раскрыть.

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/4.png "Таблица")

Видим таблицы, значит, все прошло успешно.

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/5.png "Таблица")

 По ссылке http://localhost:8000/docs видим такой интерфейс. Раскрыв метод POST и нажав try it out протестируем запрос с questions_num: 432.

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/6.png "Таблица")

Пример запроса видно ниже. Сервис вернет статус 200 и последний добавленный вопрос.

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/7.png "Таблица")

Убедимся, что данные есть в БД. Столбцы question_answer и jservice_id присутствуют, их видно при сдвиге ползунка. Также можно получить json с данными из БД через http://localhost:8000/questions/

![alt text](https://github.com/IlyasDevelopment/Jservice/blob/main/screenshots/8.png "Таблица")

Ctrl + C для остановки проекта.

Данные для авторизации можно изменить в файле .env
