import csv
import requests


with open('movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        code = row['영진위 영화 대표코드']
        url = row['영화 썸네일 이미지 URL']
        with open(f'images/{code}.jpg', 'wb') as f:
            response = requests.get(url)
            f.write(response.content)