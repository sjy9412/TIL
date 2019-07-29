# 파이썬을 활용한 데이터 수집 1

## 1. 주간/주말 박스오피스 데이터

* 사용한 모듈

  ```python
  import requests
  import csv
  from decouple import config
  from datetime import datetime, timedelta
  ```

* 시간을 나타내는 모듈 활용하기

  ```python
  from datetime import datetime, timedelta
  
  time = datetime(2019,7,13)
  time = time + timedelta(weeks=-1) # 원하는 만큼 시간을 더하고 뺄 수 있음
  targetDt.strftime('%Y%m%d')       # 시간을 문자열로 변환
  ```

* csv 파일로 저장하기

  ```python
  with open ('boxoffice.csv', 'w', encoding='utf-8') as f:
      fieldnames = ['영화 대표코드', '영화명', '해당일 누적관객수'] # 여기만 변경
      csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
      csv_writer.writeheader()
      for item in movies.values(): # 딕셔너리 만든 것 반복
          csv_writer.writerow(item)
  ```

  * 주의할 점 : DictWriter를 사용하기 위해서 딕셔너리를 {'key': {{'key1': 'value1'}, {'key2': 'value2'}} 형태로 작성해야한다.

* 영화 대표코드, 영화명, 해당일 누적관객수를 기록하였고, 최근 50주간 데이터 중에 주간 박스오피스 TOP10 데이터를 모은 결과 186편의 영화를 찾을 수 있었다.

* ![](C:\Users\student\Desktop\TIL\python\project\image\boxoffice.PNG)

* [boxoffice.csv](./boxoffice.csv)



## 2. 영화 상세정보

* csv 파일 불러오기

  ```python
  import csv
  
  movie_list = []
  with open('boxoffice.csv', 'r', encoding='utf-8') as f:
      reader = csv.DictReader(f)
      for row in reader:
          movie_list.append(row['영화 대표코드']) # row의 값이 딕셔너리로 저장된다.
  ```

* boxoffice.csv에 저장된 `영화 대표코드`를 불러와 186편의 영화 정보인 영화명, 관람등급, 개봉연도, 상영시간, 장르, 감독명의 데이터를 모아 정리함

* ![](C:\Users\student\Desktop\TIL\python\project\image\movie.PNG)

* [movie.csv](./movie.csv)



## 3. 영화인 정보

* movie.csv에 저장된 `감독명`을 불러와 영화인 코드, 영화인명, 분야, 필모리스트의 데이터를 모아 정리함
* 감독 정보가 없거나 동명이인을 처리하기 위해 조건문을 사용
* ![](C:\Users\student\Desktop\TIL\python\project\image\director.PNG)
* [director.csv](director.csv)

