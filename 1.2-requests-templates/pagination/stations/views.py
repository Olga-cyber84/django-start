from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    stations = []
    path = settings.BUS_STATION_CSV
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations.append(row)

    page_number = int(request.GET.get("page", 1))
    quantity = 10
    paginator = Paginator(stations, quantity)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': stations[(page_number - 1)*quantity: page_number*quantity],
        'page': page,
    }
    return render(request, 'stations/index.html', context)
