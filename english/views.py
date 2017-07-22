from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from english.models import Word, User, Feed
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
    print(len(list_of_words))
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

def fifteen(request):
    return render(request, 'fifteen.html', {})

def news(request):
    return render(request, 'news.html', {})

def profile(request):
    print(len(request.POST.keys()))
    if (len(request.POST.keys()) == 4):
        return render(request, 'profile.html', {'test': request.POST['sendin']})
    elif (len(request.POST.keys()) == 5):
        User(name=request.POST['name'], email=request.POST['email'], password=request.POST['password']).save()
        users = list(User.objects.all())
        #userid = User.objects.filter(id=len(users)).id
        print("PROFILE", "USERID", len(users))
        return render(request, 'profile.html', {'name': request.POST['name'], 
                                                'userid': len(users),
                                                'feeds': Feed.objects.all()})

def add(request, userid):
    print("ADD", "USERID", userid)
    Feed(url=request.POST['feedurl']).save()
    return render(request, 'profile.html', {'name': User.objects.filter(id=userid)[0].name, 
                                            'userid': userid,
                                            'feeds': Feed.objects.all()})
