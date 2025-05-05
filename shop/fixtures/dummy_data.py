import random
from faker import Faker
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image

fake = Faker('ru_RU')

# Списки для генерации случайных данных
CATEGORY_NAMES = [
    "Электроника", "Одежда", "Книги", "Дом и сад",
    "Спорт", "Красота", "Игрушки", "Еда"
]

PRODUCT_NAMES = {
    "Электроника": ["Смартфон", "Ноутбук", "Наушники", "Телевизор", "Планшет", "Фитнес-браслет", "Умные часы"],
    "Одежда": ["Футболка", "Джинсы", "Куртка", "Платье", "Рубашка", "Юбка", "Шорты"],
    "Книги": ["Роман", "Детектив", "Фэнтези", "Научная литература", "Учебник", "Биография", "Поэзия"],
    "Дом и сад": ["Диван", "Кресло", "Стол", "Стул", "Шкаф", "Лампа", "Горшок для цветов"],
    "Спорт": ["Велосипед", "Гантели", "Мяч", "Скакалка", "Тренажер", "Спортивная форма", "Коврик для йоги"],
    "Красота": ["Шампунь", "Крем", "Тушь", "Помада", "Духи", "Лак для ногтей", "Бритва"],
    "Игрушки": ["Конструктор", "Кукла", "Мягкая игрушка", "Машинка", "Паззл", "Настольная игра", "Кубик Рубика"],
    "Еда": ["Шоколад", "Печенье", "Чай", "Кофе", "Сок", "Вода", "Снеки"]
}

BRANDS = {
    "Электроника": ["Samsung", "Apple", "Xiaomi", "Sony", "LG", "Huawei", "Asus"],
    "Одежда": ["Nike", "Adidas", "Zara", "H&M", "Levi's", "Puma", "Reebok"],
    "Книги": ["Эксмо", "АСТ", "Манн, Иванов и Фербер", "Питер", "Азбука", "Феникс", "Росмэн"],
    "Дом и сад": ["IKEA", "Hoff", "Ashley", "Kartell", "BoConcept", "West Elm", "Rooms To Go"],
    "Спорт": ["Nike", "Adidas", "Puma", "Reebok", "Under Armour", "Decathlon", "Wilson"],
    "Красота": ["L'Oreal", "Maybelline", "Nivea", "Dove", "Garnier", "Schwarzkopf", "Pantene"],
    "Игрушки": ["LEGO", "Barbie", "Hasbro", "Mattel", "Fisher-Price", "Nerf", "Hot Wheels"],
    "Еда": ["Nestle", "Coca-Cola", "Pepsi", "Danone", "Mars", "Unilever", "Kellogg's"]
}

def generate_dummy_image(width=200, height=200):
    """Генерирует случайное изображение"""
    color = (random.randint(0, 255), (random.randint(0, 255)), (random.randint(0, 255)))
    image = Image.new('RGB', (width, height), color)
    buffer = BytesIO()
    image.save(buffer, format='JPEG')
    return ContentFile(buffer.getvalue(), 'dummy.jpg')


def create_categories():
    from shop.models import Category
    for name in CATEGORY_NAMES:
        Category.objects.get_or_create(
            name=name,
            defaults={'slug': fake.unique.slug()}
        )


def create_products(count=50):
    from shop.models import Category, Product
    categories = Category.objects.all()

    for _ in range(count):
        category = random.choice(categories)

        # Проверка на случай, если вдруг категория не найдена в словарях
        if category.name not in PRODUCT_NAMES:
            print(f"Нет данных для категории: {category.name}")
            continue

        product_type = random.choice(PRODUCT_NAMES[category.name])
        brand = random.choice(BRANDS[category.name])

        Product.objects.create(
            category=category,
            name=f"{brand} {product_type} {fake.word()}",
            slug=fake.unique.slug(),
            description=fake.text(),
            price=random.randint(100, 100000),
            stock=random.randint(0, 100),
            available=random.choice([True, False]),
            image=generate_dummy_image()
        )