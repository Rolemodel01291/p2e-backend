from django.db import models
from django.urls import reverse

# Create your models here.

class Game(models.Model):

    # DATABASE FIELDS
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=255)
    detail_link = models.CharField('detail_link', max_length=255, null=True)
    profile_pic = models.CharField('profile_pic', max_length=255, null=True)
    short_desc = models.CharField('short_desc', max_length=255, null=True)
    genres = models.CharField('genres', max_length=255, null=True)
    block_chains = models.CharField('block_chains', max_length=255, null=True)
    devices = models.CharField('devices', max_length=255, null=True)
    status = models.CharField('status', max_length=255, null=True)
    nft = models.CharField('nft', max_length=255, null=True)
    f2p = models.CharField('f2p', max_length=255, null=True)
    p2e = models.CharField('p2e', max_length=255, null=True)
    p2e_score = models.CharField('p2e_score', max_length=1000, null=True)
    social_24h = models.CharField('social_24h', max_length=255, null=True)
    social_7d = models.CharField('social_7d', max_length=255, null=True)
    is_new = models.IntegerField(null=True)
    description = models.CharField('description', max_length=255, null=True)
    social_url = models.JSONField(null=True)
    p2e_score_data = models.JSONField(null=True)
    supported_nfts = models.JSONField(null=True)
    supported_tokens = models.JSONField(null=True)
    app_images = models.JSONField(null=True)
    app_video = models.CharField('app_video', max_length=255, null=True)
    related_games = models.JSONField(null=True)
    facebook_url = models.CharField('facebook_url', max_length=255, null=True)
    twitter_url = models.CharField('twitter_url', max_length=255, null=True)
    total_data = models.JSONField(null=True)
    ethereum_data = models.JSONField(null=True)

    # META CLASS
    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        db_table = 'games'

    # TO STRING METHOD
    def __str__(self):
        return self.name


class GameHistory(models.Model):

    # DATABASE FIELDS
    id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, db_column='game_id' ,on_delete=models.CASCADE)
    date = models.DateField(null=True)
    user_id = models.IntegerField(null=True)
    transactions = models.IntegerField(null=True)
    volume = models.FloatField(null=True)
    total_volume = models.FloatField(null=True)

    # META CLASS
    class Meta:
        verbose_name = "GameHistory"
        verbose_name_plural = "GameHistory"
        db_table = 'game_history'


class GameContract(models.Model):

    # DATABASE FIELDS
    id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, db_column='game_id' ,on_delete=models.CASCADE)
    number = models.CharField('number', max_length=255)

    # META CLASS
    class Meta:
        verbose_name = "GameContract"
        verbose_name_plural = "GameContracts"
        db_table = 'game_contracts'