# students = {
#     '01': '김성훈',
#     '02': '김은정'
# }

# with open('a.csv','w', encoding='utf-8') as f:
#     f.write('number, name\n')
#     for number, name in students.items():
#         f.write(f'{number}, {name}\n')

# import csv
# with open ('b.csv', 'w', encoding='utf-8') as f:
#     csv_writer = csv.writer(f)
#     for item in students.items():
#         csv_writer.writerow(item)

students = {
    'asdf': {
        '순번': '01',
        '이름': '김성훈'
    },
    'asdf2': {
        '순번': '02',
        '이름': '김은정'
    }
}
# 리스트에 넣어도 됌

import csv
with open ('b.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름'] # 여기만 변경
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in students.values(): # 딕셔너리 만든 것 반복
        csv_writer.writerow(item)