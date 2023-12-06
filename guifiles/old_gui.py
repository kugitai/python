import PySimpleGUI as sg
import datetime
layout = [[sg.Text(key='output')],
          [sg.Text('西暦でお願いします')],
          [sg.Input(key='berthyear')],
          [sg.Button('年齢確認')]]
window = sg.Window('年齢',layout)
dt_now = datetime.datetime.now()
year_now = dt_now.year
while True:
    event,value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if value['berthyear'] == '':
        window['output'].update('生まれた年を入力して下さい')
        continue
    if value['berthyear'] < 0:
        window['output'].update('正の値をいれてください')
    old = year_now - int(value['berthyear'])
    if old < 0:
        window['output'].update('現在の年数を超える数値は入れないでください')
        continue
    window['output'].update(f'年齢は{old}歳です')
