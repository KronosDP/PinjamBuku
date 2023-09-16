from django.forms import ModelForm
from main.models import Books

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ["name", "amount", "description"]