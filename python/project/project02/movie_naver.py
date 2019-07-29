import csv
import requests
from decouple import config

client_id = config('NAVER_CLIENT_ID')
client_secret = config('NAVER_CLIENT_SECRET')

with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    movie_list = {}
    for row in reader:
        movie_list[row['영화명(국문)']] = row['영화 대표코드']

headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}

api_url = 'https://openapi.naver.com/v1/search/movie.json'
    
naver_movie_list = {'link': '하이퍼텍스트 link', 'image': '영화 썸네일 이미지 URL', 'userRating': '유저 평점'}
naver_movie = {}
for name, code in movie_list.items():
    query = name
    response = requests.get(f'{api_url}?query={query}', headers=headers).json()
    movie_info = response['items'][0]
    naver_movie[name] = {'영진위 영화 대표코드': code}
    naver_movie[name].update({result: movie_info[fieldname] for fieldname, result in naver_movie_list.items()})
   

with open ('movie_naver.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['영진위 영화 대표코드', '하이퍼텍스트 link', '영화 썸네일 이미지 URL', '유저 평점']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in naver_movie.values(): 
        csv_writer.writerow(item)