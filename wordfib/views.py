from django.shortcuts import render
from wordfib.models import WordAndTrue, FakeDefinitions
from random import randint, shuffle

# Create your views here.
def home_page(request):
    count = WordAndTrue.objects.count()
    rand_num = randint(1, count);
    rand_word = WordAndTrue.objects.get(pk=rand_num)
    def_list = []
    for defs in (rand_word.fakedefinitions_set.all()):
        def_list.append(defs.fake_def())

    def_list.append(rand_word.real_definition)
    shuffle(def_list)
    
    return render(request, 'home.html', {'rand_word': rand_word, 'def_list': def_list})
