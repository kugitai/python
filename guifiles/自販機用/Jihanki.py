import PySimpleGUI as sg
layout =[[sg.Text(key='change')],
         [sg.Text(key='billout')],
         [sg.Text(key='incoin')],
         [sg.Image('desktop/code/python/自販機用/can_coffee.png',size=(31,40)),
          sg.Image('desktop/code/python/自販機用/can_cola.png',size=(31,40)),
          sg.Image('desktop/code/python/自販機用/can_juice.png',size=(31,40)),
          sg.Image('desktop/code/python/自販機用/drink_energy_can.png',size=(40,40))],
         [sg.T('150円'),sg.T('130円'),sg.T('100円'),sg.T('110円')],
         [sg.B('購入',key='1'),sg.B('購入',key='2'),sg.B('購入',key='3'),sg.B('購入',key='4')],
         [sg.B('',key='1000',image_filename='desktop/code/python/自販機用/money_1000.png'),
          sg.B('',key='500',image_filename='desktop/code/python/自販機用/money_coin_blank_500.png'),
          sg.B('',key='100',image_filename='desktop/code/python/自販機用/money_coin_blank_100.png'),
          sg.B('',key='50',image_filename='desktop/code/python/自販機用/money_coin_blank_50.png'),
          sg.B('',key='10',image_filename='desktop/code/python/自販機用/money_coin_blank_10.png')],
         [sg.B('リセット')]]
window = sg.Window('自販機',layout)
price_dict = {'1': 150, '2': 130, '3': 100,'4': 110}
bills_dict = {'1000':1000,'500':500,'100':100,'50':50,'10':10}
bills = [1000,500,100,50,10]
sumlist = []
buylist = []
changelist = []
summoney = 0
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event in bills_dict:
            incoin = bills_dict[event]
            sumlist.append(incoin)
            summoney = sum(sumlist)
            window['incoin'].update(str(summoney)+'円投入されました')
    if event in price_dict:
        buycoin = price_dict[event]
        buylist.append(buycoin)
        price = sum(buylist)
        change = int(summoney) - int(price)
        if change < 0:
            window['change'].update('お金が足りません')
        elif change == 0:
            window['change'].update('お釣りはありません')
            window['billout'].update('') 
        else:
            window['change'].update('お釣りは'+str(change)+'円です')
            for bill in bills:
                    if change >= bill:
                        n = change // bill
                        for i in range(n):
                            changelist.append(bill)
                            window['billout'].update(changelist)
                            change = change - sum(changelist)
                            
                                
    if event == 'リセット':
        sumlist.clear()
        summoney = sum(sumlist)
        buylist.clear()
        price = sum(buylist)
        changelist.clear()
        window['change'].update('')
        window['billout'].update('')
        window['incoin'].update('')