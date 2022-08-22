import tkinter
import requests
import json
from ttkbootstrap import *
from PIL import Image, ImageTk

url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernie/3.0/zeus"


def get_token():
    token = requests.request("POST",
                             "https://wenxin.baidu.com/younger/portal/api/oauth/token",
                             data={"grant_type": "client_credentials",
                                   "client_id": "KUpphXTVYdcwyZchPBfFGrDRYlmbDYkz",
                                   "client_secret": "7hggpWL14vIPDu8XFU9Y2u2cLMrHXNhX"},
                             timeout=3)
    return json.loads(token.text)["data"]


def click_button(data, label):
    label.config(text="")
    text ="午饭想吃" + data + "，那我吃[MASK]" + "吧！"
    payload = {
        'text': text,
        'seq_len': 256,
        'task_prompt': '',
        'dataset_prompt': '',
        'access_token': token,
        'topk': 10,
        'stop_token': '',
        'min_dec_len': 1
    }
    response = requests.request("POST", url, data=payload)
    answer = json.loads(response.text)["data"]["result"]
    label.config(text="吃"+ answer)


def set_window():
    label1 = tkinter.Label(window, text="食物特点描述：", font=("黑体", 15))
    label1.grid(row=0)
    label2 = tkinter.Label(window, font=("黑体", 15), text="")
    label2.place(relx=0.3, rely=0.6)
    entry = tkinter.Entry(window, font=("黑体", 15))
    entry.grid(row=0, column=1)
    data = tkinter.StringVar()
    entry["textvariable"] = data
    button = tkinter.Button(window, text="推荐", font=("楷体", 15), command=lambda: click_button(data.get(), label2))
    button.place(relx=0.4, rely=0.3)

style = Style()
style = Style(theme='sandstone')
token = get_token()
window = style.master
window.title('今天吃什么')
window.geometry('400x150')
img = Image.open("1.jpg").resize((130,130))
photo = ImageTk.PhotoImage(img)
label3 = tkinter.Label(window, image=photo)
label3.place(relx=0.65,rely=0.25)
set_window()
window.mainloop()