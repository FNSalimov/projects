from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rssreader.models import User, Feed

# Create your views here.

def news(request):
    return render(request, 'rssreader/news.html', {})

def profile(request):
    print(len(request.POST.keys()))
    if (len(request.POST.keys()) == 4):
        try:
            print(request.POST['email'], request.POST['password'], list(User.objects.all())[0].email, list(User.objects.all())[0].password)
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
            return render(request, 'rssreader/profile.html', {'name': user.name, 
                                                              'userid': user.id,
                                                              'feeds': Feed.objects.all()})
        except User.DoesNotExist:
            return render(request, 'rssreader/news.html', {'error': "There is no such account"})
    elif (len(request.POST.keys()) == 5):
        try:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
            return render(request, 'rssreader/news.html', {'error_up': "Already there is exist such account"})
        except User.DoesNotExist:
            User(name=request.POST['name'], email=request.POST['email'], password=request.POST['password']).save()
            users = list(User.objects.all())
            #userid = User.objects.filter(id=len(users)).id
            print("PROFILE", "USERID", len(users))
            return render(request, 'rssreader/profile.html', {'name': request.POST['name'], 
                                                    'userid': len(users),
                                                    'feeds': Feed.objects.all()})

def add(request, userid):
    print("ADD", "USERID", userid)
    Feed(url=request.POST['feedurl']).save()
    return render(request, 'rssreader/profile.html', {'name': User.objects.filter(id=userid)[0].name, 
                                            'userid': userid,
                                            'feeds': Feed.objects.all()})
