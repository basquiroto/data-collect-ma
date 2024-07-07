# %% 
# Parei na segunda aula. https://youtu.be/JqBLUi9vqgM?feature=shared&t=2621
# https://developer.spotify.com/documentation/web-api

import requests
import json
import os

# %%
client_id = os.environ['CLIENT_ID']
secret_id = os.environ['CLIENT_SECRET_ID']
# %%

data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': secret_id,
}

response = requests.post('https://accounts.spotify.com/api/token', data=data)
print(response.json())
# %%
token = 'Bearer ' + response.json()['access_token']
header = {
    'Authorization': token
}
# %%
def get_artist_id(search_text, query_type, **kwargs):
    url = 'https://api.spotify.com/v1/search'
    params = {
        'q': search_text,
        'type': query_type,
        'limit': kwargs.get('limit')
    }

    response = requests.get(url, params=params, headers=header)
    return response.json()

# %%
response = get_artist_id(search_text='gangrena gasosa', query_type='artist', limit=1)
artist_id = response['artists']['items'][0]['id']
print('Artist ID: ', artist_id)
# %%
