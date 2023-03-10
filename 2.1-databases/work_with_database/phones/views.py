from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_object = Phone.objects.all()
    if request.GET.get('sort'):
        if request.GET.get('sort') == 'name':
            phone_object = Phone.objects.order_by('name')
        if request.GET.get('sort') == 'min_price':
            phone_object = Phone.objects.order_by('price')
        if request.GET.get('sort') == 'max_price':
            phone_object = Phone.objects.order_by('-price')
    context = {"phones": phone_object}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
