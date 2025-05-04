# Интернет-магазин

Это простой интернет-магазин на Django с основными разделами: главная, каталог товаров, корзина и личный кабинет пользователя.

## Установка

1. Клонируйте репозиторий

```bash
git clone https://github.com/yemorkovin/ecommerce.git
cd ecommerce
```

2. Создайте виртуальное окружение и активируйте его
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```
3. Установите зависимости
```bash
pip install -r requirements.txt
```
4. Примените миграции
```bash
python manage.py migrate
```
5. Запустите сервер
```bash
python manage.py runserver
```
## Структура проекта

- Главная страница — /  
- Каталог товаров — /catalog/  
- Корзина — /cart/  
- Личный кабинет — /account/

## Используемые библиотеки

- Django — фреймворк для веб-разработки  
- Bootstrap5 — для адаптивной верстки  
- django-crispy-forms — для удобной работы с формами

## Технологии

- Python 3  
- Django  
- HTML, CSS, Bootstrap5  

