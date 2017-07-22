from django.contrib import admin

from .models import Word
from rssreader.models import User

admin.site.register(Word)
admin.site.register(User)