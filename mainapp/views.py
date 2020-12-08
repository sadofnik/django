from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Товары',
        'list_menu': [
            {'href': 'products', 'name': 'Новинки'},
            {'href': 'products', 'name': 'Одежда'},
            {'href': 'products', 'name': 'Обувь'},
            {'href': 'products', 'name': 'Аксессуары'},
            {'href': 'products', 'name': 'Подарки'},
            {'href': 'test_context', 'name': 'Тест'},
        ],
        'list_products': [
            {'href': 'test_context', 'src': 'vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.',
             'desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'href': 'test_context', 'src': 'vendor/img/products/Blue-jacket-The-North-Face.png',
             'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.',
             'desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'href': 'test_context', 'src': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.',
             'desc': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'href': 'test_context', 'src': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
             'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.',
             'desc': 'Плотная ткань. Легкий материал.'},
            {'href': 'test_context', 'src': 'vendor/img/products/Black-Dr-Martens-shoes.png',
             'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00 руб.',
             'desc': 'Гладкий кожаный верх. Натуральный материал.'},
            {'href': 'test_context', 'src': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00 руб.',
             'desc': 'Легкая эластичная ткань сирсакер Фактурная ткань.'}
        ]
    }
    return render(request, 'mainapp/products.html', context)


def test_context(request):
    context = {
        'title': 'Добро пожаловать!',
        'username': 'Alex Gr',
        'products': [
            {'name': 'Чёрное худи', 'price': '2 990 руб.'},
            {'name': 'Джинсы', 'price': '5 800 руб.'},
            {'name': 'Джемпер', 'price': '4 990 руб.'},
        ],
        # 'promotion': True,
        'promotion_products': [
            {'name': 'Туфли Dr Martens', 'price': '12 390 руб.'},
        ],
        'list_menu': [
            {'href': 'test_context', 'name': 'все'},
            {'href': 'test_context', 'name': 'дом'},
            {'href': 'test_context', 'name': 'офис'},
            {'href': 'test_context', 'name': 'модерн'},
            {'href': 'test_context', 'name': 'классика'},
        ],
        'list_products': [
            {'href': 'test_context', 'src': 'vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.',
             'desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'href': 'test_context', 'src': 'vendor/img/products/Blue-jacket-The-North-Face.png',
             'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.',
             'desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},


        ]
    }

    products = context['products']

    return render(request, 'mainapp/context.html', context)
