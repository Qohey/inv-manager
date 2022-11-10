import PySimpleGUI as sg
import cv2
from icecream import ic
sg.theme("DarkGrey10")
heads = ["在庫名", "個数"]
vals = [["bottle", "1"], ["apple", 2]]


inv_result = sg.Table(vals, headings=heads, auto_size_columns=False,
                      select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                      vertical_scroll_only=True, key="inv_result")


detect_result = sg.Image(filename="", key="detect")


io_result = sg.Multiline(key="io_result", autoscroll=True,
                         size=(120, 10), disabled=True, )

reset_btn = sg.Button("RESET", key="reset_btn")

reset_col = sg.Column(layout=[[reset_btn]], justification="right")

left_col = sg.Column(layout=[[inv_result],[reset_col]], vertical_alignment="top", justification="right")

top_col = sg.Column(layout=[[left_col, detect_result]], justification="left", vertical_alignment="top")

layout = [
    [top_col],
    [io_result]
]

window = sg.Window(
    title="Inv Management App",
    layout=layout,
    resizable=True
)

cap = cv2.VideoCapture(0)
i = 0

while True:
    i += 1
    event, value = window.read(timeout=10)  # イベント入力を待つ
    if event == sg.WIN_CLOSED:
        break
    if event == "reset_btn":
        selected_val = inv_result.SelectedRows
        ic(inv_result.Values[selected_val[0]])
    ret, frame = cap.read()
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window['detect'].update(data=imgbytes)
    if i % 100 == 0:
        window["io_result"].print("aaa")
        values = window["inv_result"].get()
        values += [[1, 2]]
        window["inv_result"].update(values=values)
        ic(inv_result.SelectedRows)

window.close()
