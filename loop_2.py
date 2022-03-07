#리스트 안의 리스트
persons = [
    ['egoing','seoul','web'],
    ['sori','seoul','iot'],
    ['lily','busan','idot'],
]
print(persons[0][1])

name, adress, info = ['egoing','seoul','web']

for name,adress,info in persons:
    print(name, adress, info)

