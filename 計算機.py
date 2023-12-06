while True:
    try:
        b = int(input('一つ目の数字は？'))
        if b == '終了':
            break
        a = input('+,-,*,/を選択してください(英数入力で)')
        c = int(input('二つ目の数字は？'))
        if a == '+':
            d = (b+c)
        elif a == '-':
            d = (b-c)        
        elif a == '*':
            d = (b*c)
        elif a == '/':
            if c == 0:
                print('0では割れません')
                e = input('終了する際はここに終了と入れてください')
                if e == '終了':
                    break
                continue
            d = (b//c)
        else:
            print('演算子が異なるようです')
            continue    
        print(f'答えは{d}です')
        f = input('終了する際はここに終了と入れてください')
        if f == '終了':
            break
    except ValueError:
        print('数字を入力してください')
        f = input('終了する際はここに終了と入れてください')
        if f == '終了':
            break
        continue