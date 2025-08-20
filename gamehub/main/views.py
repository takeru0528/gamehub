from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def game_list(request):
    return render(request, 'main/game_list.html')

def game_upload(request):
    return render(request, 'main/game_upload.html')

def game_detail(request, game_id):
    return render(request, 'main/game_detail.html', {'game_id': game_id})

# views.py
from .models import KanjiWord

def typing_game(request):
    kanji_words = KanjiWord.objects.all()
    return render(request, 'main/typing_game.html', {'kanji_words': kanji_words})