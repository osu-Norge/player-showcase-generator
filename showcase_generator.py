"""
Spaghetti code, but hey it works!

WARNING:
This script makes 12 API requests & scrapes 8 images in the matter of a few seconds. 
Please do not run this script excessively.
"""


import yaml
from requests import get
import urllib.parse, urllib.request
from datetime import datetime
from PIL import Image
import locale


locale.setlocale(locale.LC_ALL, '')  # Sets locale (number formatting) to your systems language's

with open('config.yaml', 'r', encoding='utf8') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)
    osu_api_key = config['osu_api_key']
    teams = config.get('teams', {})
    players = config.get('players', {})


def make_text_file(folder, file_name, player):
    player = str(player)
    with open(f'{folder}/{file_name}.txt', 'w+', encoding='utf-8') as f:
        f.write(player)
    print(f'Wrote {folder}/{file_name}.txt')


def fetch_img(url, path):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, path)
    print(f'Saved image {path}')


def resize_avatar(player):
    image = Image.open(f'{player}/avatar.png').convert('RGBA').resize((128, 128))
    image.save(f'{player}/avatar_resized.png')
    print(f'Resized {player} avatar')


def fetch_info(team_member, player, osu_api_key):
    print(f'Fetching {team_member}...')

    # Fetches user info
    url = 'https://osu.ppy.sh/api/get_user?' + urllib.parse.urlencode({'u': player, 'k': osu_api_key})
    user_data = get(url).json()[0]
    user_id = user_data['user_id']
    username = user_data['username']
    rank = locale.format_string('%d', int(user_data['pp_rank']), grouping=True)
    country_rank = locale.format_string('%d', int(user_data['pp_country_rank']), grouping=True)
    pp = locale.format_string('%d', round(float(user_data['pp_raw'])), grouping=True)
    playtime = locale.format_string('%d', round((int(user_data['total_seconds_played']) / 60) / 60), grouping=True)
    playtime = f'{playtime} timer'
    join_date = datetime.strptime(user_data['join_date'], '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y')

    user_info = {
        'username': username,
        'rank': rank,
        'country_rank': country_rank,
        'pp': pp,
        'playtime': playtime,
        'join_date': join_date
    }
    for key, value in user_info.items():
        make_text_file(team_member, key, value)

    # Fetches top play
    url = 'https://osu.ppy.sh/api/get_user_best?' + urllib.parse.urlencode({
        'u': user_id, 'limit': '1', 'k': osu_api_key
        })
    play_data = get(url).json()[0]
    beatmap_id = play_data['beatmap_id']
    play_pp = locale.format_string('%d', round(float(play_data['pp'])), grouping=True)
    play_pp = f'{play_pp}PP'

    play_info = {
        'play_pp': play_pp
    }
    for key, value in play_info.items():
        make_text_file(team_member, key, value)

    # Fetches top play beatmap metadata
    url = 'https://osu.ppy.sh/api/get_beatmaps?' + urllib.parse.urlencode({
        'b': beatmap_id, 'limit': '1', 'k': osu_api_key
        })
    beatmap_data = get(url).json()[0]
    artist = beatmap_data['artist']
    title = beatmap_data['title']
    difficulty = beatmap_data['version']
    beatmap_name = f'{artist} - {title} [{difficulty}]'
    beatmap_creator = beatmap_data['creator']
    beatmap_set_id = beatmap_data['beatmapset_id']

    beatmap_info = {
        'beatmap_name': beatmap_name,
        'beatmap_creator': beatmap_creator
    }
    for key, value in beatmap_info.items():
        make_text_file(team_member, key, value)
    
    fetch_img(f'https://a.ppy.sh/{user_id}?.png', f'{team_member}/avatar.png')
    fetch_img(f'https://assets.ppy.sh/beatmaps/{beatmap_set_id}/covers/cover.jpg?',
              f'{team_member}/top_play_map_img.jpg')
    resize_avatar(team_member)

    print('DONE')


# Runs the script
for team_member, player in players.items():
    fetch_info(team_member, player, osu_api_key)
for team, team_name in teams.items():
    make_text_file('teams', team, team_name)
    print('DONE')