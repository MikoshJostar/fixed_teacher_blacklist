
# Чорний список викладача

Простий Django-проєкт для ведення списку учнів:
- Ім'я учня
- Клас / курс
- Причина
- Борг / двійка
- Дата додавання

## Запуск

1. Встанови Python 3.11+
2. Встанови Django:

pip install -r requirements.txt

3. Запусти міграції:

python manage.py makemigrations


python manage.py migrate

5. Створи адміна:

python manage.py createsuperuser

5. Запуск сервера:

python manage.py runserver

