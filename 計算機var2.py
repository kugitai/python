while True:
    try:
        d = 0
        a = float(input('一つ目の数字は？(終了する際は終了と入力)'))
        b = input('+,-,*,/を入れてください')
        c = float(input('二つ目の数字は？'))
        if b == '+':
            d = (a+c)
        elif b == '-':
            d = (a-c)
        elif b == '*':
            d = (a*c)
        elif b == '/':
            d = (a/c)
        else:
            print('演算子以外もしくは英数以外で入力されました')
        print(f'答えは{0}です')
        e = input('終了する際は終了と入力してください')
        if e == '終了':
            break
        else:
            continue
    except ZeroDivisionError:
        print('0では割れません')
        e = input('終了する際は終了と入力してください')
        if e == '終了':
            break
        continue
    except ValueError:
        print('数字を入力してください')
        e = input('終了する際は終了と入力してください')
        if e == '終了':
            break
        continue