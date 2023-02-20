from django.shortcuts import render
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cofe': {
        'кофе, ст.л': 1,
        'кипяток, мл': 250,
    },
}


def main(request):
    context = {
        'recipe': DATA
    }
    return render(request, 'calculator/main.html', context)


def get_ingredients(request, recipe):
    servings = int(request.GET.get('servings', 1))
    ingredients = {}

    for ingredient, amount in DATA[recipe].items():
        ingredients[ingredient] = f'{amount * servings: .2f}'

    context = {
        'recipe': ingredients
    }
    return render(request, 'calculator/index.html', context)
