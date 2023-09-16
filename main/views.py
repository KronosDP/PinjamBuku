from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import BooksForm
from django.urls import reverse
from main.models import Books
from django.core import serializers

# Create your views here.
def show_main(request):
    KumpulanBuku = Books.objects.all()
    context = {
        'name': 'PinjamBuku',
        'class': 'PBP E',
        'Books': KumpulanBuku
    }

    return render(request, "main.html", context)

def create_book(request):
    form = BooksForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_book.html", context)

def show_xml(request):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Books.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Books.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")