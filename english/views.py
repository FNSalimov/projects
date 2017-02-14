from django.shortcuts import render
from django.http import HttpResponse
import random
from english.models import Word

def index(request):
    return render(request, 'index.html', {})

def english(request):
    """my_file = open('/home/firdavs-senior/teach/my_projects/english/text.txt', 'r')
    list_of_words = []
    five_words = []
    for line in my_file:
        line = line.strip()
        list_of_words.append(line)
    for i in range(5):
        random_number = random.randint(1, len(list_of_words) - 1)
        while list_of_words[random_number] in five_words:
            random_number = random.randint(1, len(list_of_words) - 1)
        five_words.append(list_of_words[random_number])
    russian_words, english_words = {}, {}
    ran = [0, 1, 2, 3, 4]
    random.shuffle(ran)
    for i in range(5):
        english_words[i] = five_words[i][five_words[i].index('--') + 2:]
    for i in range(5):
        russian_words[i] = five_words[i][:five_words[i].index('--')]"""
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
    return render(request, 'english.html', {'russian_words': russian_words, 'english_words': english_words})

