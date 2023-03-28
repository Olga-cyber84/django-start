from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    book_object = Book.objects.order_by('-pub_date')
    context = {"books": book_object}
    return render(request, template, context)


def pub_date(request, pub_date):
    template = 'books/pub_date.html'
    book_object = Book.objects.filter(pub_date=pub_date)
    pub_date_values = Book.objects.order_by(
        '-pub_date').distinct('pub_date').values('pub_date')
    counter = 0
    for pos, val in enumerate(pub_date_values):
        if str(val['pub_date']) == pub_date:
            counter = pos
    if counter > 0:
        next_page = pub_date_values[counter-1]['pub_date']
    else:
        next_page = None

    if counter < len(pub_date_values)-1:
        previous_page = pub_date_values[counter+1]['pub_date']
    else:
        previous_page = None
    context = {"books": book_object, "next_page": next_page,
               "previous_page": previous_page}
    return render(request, template, context)
