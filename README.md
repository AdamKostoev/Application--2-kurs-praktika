# Application--2-kurs-praktika
Application--2-kurs-praktika
Описание проекта
Этот проект представляет собой платформу для парсинга вакансий с сайта HeadHunter и их отображения на веб-странице.

Установка
1. Клонирование репозитория
Склонируйте этот репозиторий на свой компьютер:
git clone https://github.com/AdamKostoev/Application--2-kurs-praktika.git
cd Application--2-kurs-praktika
2. Создание виртуального окружения
Создайте виртуальное окружение и активируйте его:
Для Windows:
python -m venv venv
venv\Scripts\activate
Для macOS и Linux:
python3 -m venv venv
source venv/bin/activate
3. Установка зависимостей
Установите все необходимые зависимости:
pip install -r requirements.txt
4. Настройка базы данных
Примените миграции для настройки базы данных:
python manage.py migrate

Запуск
1.Запустите сервер разработки Django:
2.python manage.py runserver
3.Сервер будет доступен по адресу http://127.0.0.1:8000/.

Использование
1.Откройте браузер и перейдите по адресу http://127.0.0.1:8000/.
2.Введите поисковый запрос, город, минимальную и максимальную зарплату в соответствующие поля и нажмите "Search".
3.На главной странице будут отображены вакансии, соответствующие вашему запросу.
4.Перейдите на страницу "All Vacancies" для просмотра всех сохраненных вакансий.

Примеры
Пример использования:
1.Введите в поле поиска "Python Developer".
2.Укажите город "Москва".
3.Задайте минимальную зарплату "50000".
4.Нажмите "Search".
5.На главной странице будут отображены все вакансии, соответствующие этим критериям.

Требования
1.Python 3.9
2.Django 3.0+
3.Интернет-соединение для доступа к API HeadHunter

Авторы и контакты
1.Автор проекта: Костоев Адам
2.Телеграмм: @kostoev_077

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами.
Если у вас есть дополнительные требования или хотите добавить что-то еще, дайте знать, и я помогу доработать инструкцию.
