from django.shortcuts import render
from .models import ClassWords
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def words_view(request):
    return render(request, 'manozodynas/words.html', {'words': ClassWords.objects.all()})

class ClassNewWord(CreateView):
    model = ClassWords
    success_url = reverse_lazy('words_view')
    template_name = 'manozodynas/new_word.html'


