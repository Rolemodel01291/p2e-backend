from django.shortcuts import render
from django.db.models import Q
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from games.models import Game as GameModel, GameHistory as GameHistoryModel, GameContract as GameContractModel
from games.serializers import AutoCompleteSerializer, GameSerializer, GameDetailSerializer, GameHistorySerializer, GameContractSerializer
from rest_framework.decorators import api_view

from games.utilities import __with_sponsored_game, __game_list_set

@api_view(['GET'])  
def list(request, page):
    if request.method=='GET':
        page = int(page)
        try:                
            games = __with_sponsored_game(__game_list_set()[(page-1)*50: page*50])
            games_serializer = GameSerializer(games, many=True)
            return JsonResponse(games_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def new_list(request):
    if request.method=='GET':
        try:
            games = __game_list_set().filter(is_new=1)
            games_serializer = GameSerializer(games, many=True)
            return JsonResponse(games_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search(request, keyword):
    if request.method=='GET':
        try:
            games = __game_list_set().filter(Q(name__contains=keyword)|Q(short_desc__contains=keyword)|Q(genres__contains=keyword))
            games_serializer = GameSerializer(games, many=True)
            return JsonResponse(games_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def filter(request, platform, genre, device, status, nft, f2p, p2e):
    if request.method=='GET':
        try:
            games = __game_list_set().filter(
                Q(block_chains__contains=('' if platform=='all-platform' else platform)) & 
                Q(genres__contains=('' if genre=='all-genre' else genre)) & 
                Q(devices__contains=('' if device=='all-device' else device)) & 
                Q(status__contains=('' if status=='all-status' else status)) & 
                Q(nft__contains=('' if nft=='all-nft' else nft)) & 
                Q(f2p__contains=('' if f2p=='all-f2p' else f2p)) & 
                Q(p2e__contains=('' if p2e=='all-p2e' else p2e))
            )
            games_serializer = GameSerializer(games, many=True)
            return JsonResponse(games_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detail(request, id):
    if request.method=='GET':
        try: 
            game = GameModel.objects.filter(id=id)
            game_detail_serializer = GameDetailSerializer(game, many=True)
            return JsonResponse(game_detail_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def history(request, id):
    if request.method=='GET':
        try: 
            game = GameHistoryModel.objects.filter(game_id=id)
            game_history_serializer = GameHistorySerializer(game, many=True)
            return JsonResponse(game_history_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def contracts(request, id):
    if request.method=='GET':
        try: 
            contracts = GameContractModel.objects.filter(game_id=id)
            game_contract_serializer = GameContractSerializer(contracts, many=True)
            return JsonResponse(game_contract_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def auto_complete(request, keyword):
    if request.method=='GET':
        try: 
            games = GameModel.objects.only('id', 'name', 'detail_link', 'profile_pic') \
                        .filter(Q(name__contains=keyword)|Q(short_desc__contains=keyword))
            autocomplete_serializer = AutoCompleteSerializer(games, many=True)
            return JsonResponse(autocomplete_serializer.data, safe=False)
        except GameModel.DoesNotExist:
            return JsonResponse({'message': 'The game does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)