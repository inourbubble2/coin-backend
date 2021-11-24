import requests
from database.cafe import Cafe
from database import Database

header = {'Authorization': 'KakaoAK e739d059fb281ac73a2ca928910f688d'}

queries = ['회기', '서울시립대 전농로', '망우로']
keywords = ['hoegi', 'front', 'back']

for i in range(3):
    query = queries[i]
    is_end = False
    page = 1
    size = 15
    while not is_end:
        url = f'https://dapi.kakao.com/v2/local/search/keyword.json?page={page}&sort=accuracy&query={query}&category_group_code=CE7&size={size}'

        if i == 2:
            url += '&x=127.060769&y=37.586549&radius=400'

        data = requests.get(url, headers=header).json()
        cafes = data['documents']
        meta = data['meta']
        is_end = meta['is_end']
        print(meta)

        with Database() as db:
            for document in cafes:
                cafe = Cafe(
                    kakao_id=document.get('id'),
                    name=document.get('place_name'),
                    address=document.get('road_address_name'),
                    latitude=document.get('x'),
                    longitude=document.get('y'),
                    location=keywords[i]
                )
                print(cafe.name)
                db.add(cafe)
                db.commit()
        page += 1
