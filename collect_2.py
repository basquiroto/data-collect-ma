# %% 
# segunda aula. https://youtu.be/JqBLUi9vqgM?feature=shared&t=2621
# https://openrouteservice.org/dev/#/api-docs -- Associar ao QGIS + Gerar Isocronicas + Salvar resultado no POstgresql

import os
import requests
import json

 # %%
headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': os.getenv('TOKEN_ORS'),
}

nome = 'Mirante Serra Rio Rastro'
json_data = {
    'locations': [
        [
            -49.549866,
            -28.393834
        ],
    ],
    'range': [
        60, 120, 180, 210, 240, 270, 300
    ],
    'range_type': 'time' # seconds
}

response = requests.post('https://api.openrouteservice.org/v2/isochrones/driving-car', headers=headers, json=json_data)
print(response.status_code)
# %%
json_file = json.loads(response.text)
print(json_file)
# %%
def list_to_wkt(coords, geom_type):
    # Example of coordinates
    # [8.663605, 49.402767, 8.702728, 49.435152]
    
    n_coords = len(coords)
    if n_coords % 2 != 0:
        raise ValueError('Coordinates are not an even number.')
    
    if geom_type == 'POLYGON':
        vertices = [(coords[i], coords[i+1]) for i in range(0, n_coords, 2)]
        print(vertices)

        wkt = 'POLYGON (('
        wkt += ', '.join(f'{long} {lat}' for long, lat in vertices)
        wkt += '))'
    
    elif geom_type == 'BBOX':
        vertices = [(coords[0], coords[1]),
                    (coords[0], coords[3]),
                    (coords[2], coords[3]),
                    (coords[2], coords[1]),
                    (coords[0], coords[1])]
        print(vertices)
        
        wkt = 'POLYGON (('
        wkt += ', '.join(f'{long} {lat}' for long, lat in vertices)
        wkt += '))'

    else:
        raise ValueError('Geometry convertion not available.')

    return wkt
# %%
bbox = list_to_wkt(json_file['bbox'], 'BBOX')

# %%
def pairs_to_wkt(coords):
    # Coordinates example
    # [[8.672785, 49.417949], [8.673054, 49.417007]]

    wkt = 'POLYGON (('
    wkt += ', '.join(f'{long} {lat}' for long, lat in coords)
    wkt += '))'

    return wkt
# %%
lat_origin = json_data['locations'][0][1]
long_origin = json_data['locations'][0][0]

## only one time value...
# time = json_data['range'][0]
# coords = json_file['features'][0]['geometry']['coordinates'][0]
# coordinates = pairs_to_wkt(coords)

## more than one time value...
nr_feat = len(json_file['features'])

time = []
coordinates = []

for i in range(0, nr_feat):
    coords = json_file['features'][i]['geometry']['coordinates'][0]
    wkt = pairs_to_wkt(coords)
    coordinates.append(wkt)

    time_value = json_file['features'][i]['properties']['value']
    time.append(time_value)
# %%
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import psycopg2

# %%
db_url = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(db_url)

Session = sessionmaker(bind=engine) # Cria classe Sessão.
s = Session() # Cria uma sessão para conectar no banco.

for i in range(0, nr_feat):
    insert_query = text('INSERT INTO isochrones (name, lat_origin, long_origin, time_seconds, isochrone) VALUES (:name, :lat_origin, :long_origin, :time_seconds, :isochrone)')
    s.execute(insert_query, {'name': nome,
                             'lat_origin': lat_origin, 
                             'long_origin': long_origin, 
                             'time_seconds': time[i], 
                             'isochrone': coordinates[i]})

s.commit()
s.close()

"""
CREATE TABLE IF NOT EXISTS public.isochrones
(
    id serial,
    name varchar,
    lat_origin varchar,
    long_origin varchar,
    time_seconds double precision,
    isochrone geometry(Polygon,4326),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT isochrones_pkey PRIMARY KEY (id)
)
"""
# %%
