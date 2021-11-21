from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Game
from .serializers import GameSerializer

class GamesList(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GamesDetail(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer