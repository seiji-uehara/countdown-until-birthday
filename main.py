from datetime import datetime
from calendar import isleap
import time
import PySimpleGUI as sg

sg.theme("Default")

def get_date(month):
    # 入力された月を受け取り、日付のリストを返す
    date_dict = {
        "1":  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        "2":  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"],
        "3":  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        "4":  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"],
        "5":  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        "6":  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"],
        "7":  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        "8":  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        "9":  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"],
        "10": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        "11": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"],
        "12": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    }
    return date_dict[month]


layout = [
    [sg.Text("誕生日を入力してください。")],
    [sg.Combo(values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], size=(5, 1), key="MONTH", enable_events=True, readonly=True), sg.Text("月"), sg.Combo(values=[""], size=(5, 1), key="DAY", enable_events=True, readonly=True), sg.Text("日")],
    [sg.Text("次の誕生日まであと", key="COUNTDOWN_TEXT1"), sg.Text("", key="COUNTDOWN_TEXT2", font=("Arial",20), size=(3, 1), justification="right"), sg.Text("日です。", key="COUNTDOWN_TEXT3")]
]


window = sg.Window("誕生日カウントダウン", size=(300, 120)).Layout(layout)


while True:
    event, values = window.Read()
    # ウィンドウの×ボタンで終了
    if event == sg.WIN_CLOSED:
        break

    if event == "MONTH":
        dt_month = values["MONTH"]
        list_day = get_date(dt_month)
        window.FindElement("DAY").Update(values=list_day)

        window["COUNTDOWN_TEXT1"].Update("次の誕生日まであと")
        window["COUNTDOWN_TEXT2"].Update("")
        window["COUNTDOWN_TEXT3"].Update("日です。")

    if event == "DAY" and values["DAY"] != "":
        dt1 = datetime.today()                       # 今日
        today = datetime(dt1.year,dt1.month,dt1.day) # 今日
        thisyear = today.year                        # 今年

        # うるう年以外の2/29は3/1として計算
        if isleap(thisyear) == False and values["MONTH"] == "2" and values["DAY"] == "29":
            dt2 = datetime(thisyear, 3, 1)
        else:
            dt2 = datetime(thisyear, int(values["MONTH"]), int(values["DAY"]))

        if today < dt2:
            dt3 = dt2 - today
            window["COUNTDOWN_TEXT1"].Update("次の誕生日まであと")
            window["COUNTDOWN_TEXT2"].Update(str(dt3.days))
            window["COUNTDOWN_TEXT3"].Update("日です。")
        elif today > dt2:
            dt2 = datetime(thisyear + 1, int(values["MONTH"]), int(values["DAY"]))
            dt3 = dt2 - today
            window["COUNTDOWN_TEXT1"].Update("次の誕生日まであと")
            window["COUNTDOWN_TEXT2"].Update(str(dt3.days))
            window["COUNTDOWN_TEXT3"].Update("日です。")
        else:
            window["COUNTDOWN_TEXT1"].Update("お誕生日おめでとう!")
            window["COUNTDOWN_TEXT2"].Update("")
            window["COUNTDOWN_TEXT3"].Update("")


window.Close()