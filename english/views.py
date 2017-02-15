from django.shortcuts import render
from django.http import HttpResponse
import random
from english.models import Word
import json

def test(request):
    list_of_words = list(Word.objects.all())
    five_words = []
    for i in range(5):
        random_number = random.randint(1, len(list_of_words) - 1)
        while list_of_words[random_number] in five_words:
            random_number = random.randint(1, len(list_of_words) - 1)
        five_words.append(list_of_words[random_number])
    jsonStr = json.dumps([w.toJSON() for w in five_words])
    return HttpResponse(jsonStr, content_type='application/json')

def index(request):
    return render(request, 'index.html', {})

def english(request):
    list_of_words = list(Word.objects.all())
    five_words = []
    for i in range(5):
        random_number = random.randint(1, len(list_of_words) - 1)
        while list_of_words[random_number] in five_words:
            random_number = random.randint(1, len(list_of_words) - 1)
        five_words.append(list_of_words[random_number])
    russian_words = five_words
    random.shuffle(five_words)
    english_words = []
    for i in range(5):
        random_number = random.randint(0, 4)
        while five_words[random_number] in english_words:
            random_number = random.randint(0, 4)
        english_words.append(five_words[random_number])
    return render(request, 'english.html', {'russian_words': russian_words, 'english_words': english_words, 'test': test})

