from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_object = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort:
        if sort == 'name':
            phone_object = Phone.objects.order_by('name')
        if sort == 'min_price':
            phone_object = Phone.objects.order_by('price')
        if sort == 'max_price':
            phone_object = Phone.objects.order_by('-price')
    context = {"phones": phone_object}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    context = {"phone": phone_object[0]}
    return render(request, template, context)
