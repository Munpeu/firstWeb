input_id = input('id: ')
id = 'egoing'
password = '11111'

if id == input_id:
    input_password = input('password: ')
    if password == input_password:
        print('welcom')
    else:
        print('wrong password')
else:
    print('wrong id')