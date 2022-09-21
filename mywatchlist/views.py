from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from mywatchlist.models import MyWatchList

# Create your views here.
data = MyWatchList.objects.all()

def show_watchlist(request):
    context = {
    'nama': 'Najmi Anasya Calyla',
    'npm': '2106639825',
    }
    return render(request, "watchlist.html", context)

def show_html(request):
    watchlist = MyWatchList.objects.all()
    watched = 0
    not_yet_watched = 0

    for movie in watchlist:
        if movie.watched == True:
            watched += 1
        else:
            not_yet_watched += 1
    
    if watched >= not_yet_watched:
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton"

    context = {
    'watchlist': watchlist,
    'message': message
    }
    return render(request, "mywatchlist.html", context)
    
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")