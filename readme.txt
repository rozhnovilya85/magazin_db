Задание на Python
Реализовать сервис, который принимает и отвечает на HTTP запросы.
Описание
GET /city/ — получение всех городов из базы
POST /city/ — создание города
GET /city/city_id/street/ — получение всех улиц города; (city_id — идентификатор города)
POST /shop/ — создание магазина; Данный метод получает json c объектом магазина, в ответ возвращает данные созданной записи
GET /shop/?street=&city=&open=0/1 — получение списка магазинов
Подготовительные действия
Клонировать проект git clone https://github.com/rozhnovilya85/magazin_db
Установить зависимости pip3 install -r requirements.txt
Создать базу данных в СУБД PostreSQL
По пути mediasoft/settings.py в DATABASES указать данные базы данных
Запустить миграции командой py manage.py migrate
Запуск в режиме отладки осуществляется командой py manage.py runserver