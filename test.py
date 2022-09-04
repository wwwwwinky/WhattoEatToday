import tkinter
from ttkbootstrap import *
from PIL import Image, ImageTk
import wenxin_api
from wenxin_api.tasks.cloze import Cloze

wenxin_api.ak = "KUpphXTVYdcwyZchPBfFGrDRYlmbDYkz"
wenxin_api.sk = "7hggpWL14vIPDu8XFU9Y2u2cLMrHXNhX"


def click_button(data, label):
    label.config(text="")
    text ="午饭想吃" + data + "，那我吃_吧！"
    input_dict = {
        "text": text,
        "seq_len": 512,
        "topp": 0.3,
        "penalty_score": 1.2,
        "min_dec_len": 1,
        "is_unidirectional": 0,
        "task_prompt": "cloze"
    }
    rst = Cloze.create(**input_dict)
    print(rst['result'])
    label.config(text="吃"+ rst['result'])


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
window = style.master
window.title('今天吃什么')
window.geometry('400x150')
img = Image.open("1.jpg").resize((130,130))
photo = ImageTk.PhotoImage(img)
label3 = tkinter.Label(window, image=photo)
label3.place(relx=0.65,rely=0.25)
set_window()
window.mainloop()
