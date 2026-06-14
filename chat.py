name = input('名前を入力してください')
while True:
    chat = input()
    if chat == 'quit':
        break
    else:
        print(f'{name}:{chat}')