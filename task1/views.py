from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


def home_page(request):
    return render(request, 'fourth_task/home.html')


def shop_page(request):
    games = Game.objects.all()

    context = {
        'games': games
    }

    return render(request, 'fourth_task/shop.html', context)


def cart_page(request):
    return render(request, 'fourth_task/cart.html')


users = []


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            try:
                existing_buyer = Buyer.objects.get(name=username)
                info['error'] = 'Пользователь уже существует'
            except Buyer.DoesNotExist:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif age < 18:
                    info['error'] = 'Вы должны быть старше 18'
                else:
                    buyer = Buyer.objects.create(
                        name=username,
                        age=age
                    )
                    return render(request, 'fifth_task/registration_page.html',
                                  {'message': f'Приветствуем, {username}!'})

        info['form'] = form
    else:
        info['form'] = UserRegister()

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})
        info['form'] = form
    else:
        info['form'] = UserRegister()

    return render(request, 'fifth_task/registration_page.html', info)
