import requests
key = 'd558ccf8bcadebbbe96d9bee48206e8f'
targetDt ='20190713'
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'
print(api_url)
response = requests.get(api_url).json()
print(response)