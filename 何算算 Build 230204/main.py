"""
软件的主要界面
版本: Build 230204 Test
没有计算功能
"""
import tkinter as tk
from tkinter import ttk


# 常量
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 450

WINDOW_TITLE = "何算算 Build 230204 Test"

SIDEBAR_WIDTH = 50
SIDEBAR_HEIGHT = WINDOW_HEIGHT

SIDEBAR_BUTTON_WIDTH = 40
SIDEBAR_BUTTON_HEIGHT = 50

SIDEBAR_LABEL_WIDTH = SIDEBAR_WIDTH - SIDEBAR_BUTTON_WIDTH
SODEBAR_LABEL_HEIGHT = SIDEBAR_BUTTON_HEIGHT

SIDEBAR_BUTTON_TEXTS = ["基本\n图形", "计算器", "帮助"]

SIDEBAR_FRAME_WIDTH = WINDOW_WIDTH - SIDEBAR_WIDTH
SIDEBAR_FRAME_HEIGHT = SIDEBAR_HEIGHT

OPTION_HEIGHT = 30

LABEL_WIDTH = 80
LABEL_HEIGHT = OPTION_HEIGHT

ENTRY_WIDTH = 80
ENTRY_HEIGHT = OPTION_HEIGHT

BUTTON_WIDTH = 40
BUTTON_HEIGHT = OPTION_HEIGHT

BUTTON_CURSOR = "hand2"
BUTTON_BORDERWIDTH = 1
BUTTON_RELIEF = "solid"

BUTTON_BACKGROUND = "White"
BUTTON_FOREGROUND = "Black"
BUTTON_BACKGROUND_MOUSE = "GhostWhite"

SCROLLBAR_WIDTH = 20

HELP_TEXT = """帮助信息
一、关于软件
1. 软件名称: 何算算 Build 230202 Test
2. 软件作者: Lonely-Pea
3. 软件使用操作系统: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11及更高的Windows操作系统
4. 软件收费: 免费
5. 软件官网: https://lonely-pea.github.io/HeSuansuanDownload/

二、软件使用说明
该版本为内测版本，没有软件计算功能。

三、鸣谢
感谢QQ号为1625396311的人对该软件的编写！
"""


# 主窗口
class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # 设置变量
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.x = (self.screenwidth - WINDOW_WIDTH) / 2
        self.y = (self.screenheight - WINDOW_HEIGHT) / 2
        self.size = "%dx%d+%d+%d" % (WINDOW_WIDTH, WINDOW_HEIGHT, self.x, self.y)

        # 设置窗口
        self.title(WINDOW_TITLE)
        self.geometry(self.size)
        self.resizable(False, False)


# 框架 - 基本计算
class BasicFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master

        tk.Label(self, text="基本计算").pack(fill=tk.BOTH, expand=True)


# 框架 - 计算器
class CalcFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master

        tk.Label(self, text="计算器").pack(fill=tk.BOTH, expand=True)


# 框架 - 帮助
class HelpFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # 设置变量
        self.master = master
        
        # 读取内容
        with open("data/update.log", "r", encoding="utf-8") as file_update:
            update_text = file_update.read()

        # 设置界面
        text_help = Text(master=self, text=HELP_TEXT)
        text_update = Text(master=self, text=update_text, y=SIDEBAR_FRAME_HEIGHT/2)


# 边框
class Sidebar(tk.Frame):
    def __init__(self, master, frames, texts, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, sidebar_width=SIDEBAR_WIDTH, sidebar_height=SIDEBAR_HEIGHT):
        super().__init__(master)

        # 设置变量
        self.master = master
        self.frames = frames
        self.texts = texts
        self.width = width
        self.height = height
        self.sidebar_width = sidebar_width
        self.sidebar_height = sidebar_height
        self.frame_width = self.width - self.sidebar_width
        self.frame_height = self.height

        self.x, self.y = 0, 0
        self.frame_x, self.frame_y = self.sidebar_width, self.y

        self.button_list = []
        for i in range(len(self.texts)):
            self.button_list.append(0)

        # 设置组件
        self.sidebar()
        self.label()
        self.frame()
        self.bottom_button()
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)
    
    # 生成边框
    def sidebar(self):
        global sidebar_frame
        sidebar_frame = tk.Frame(self)
        sidebar_frame.place(x=self.x, y=self.y, width=self.sidebar_width, height=self.sidebar_height)
        
        for index in range(len(self.texts)):
           self.button_list[index] = Button(master=sidebar_frame, text=self.texts[index], command=lambda event, index=index: self.change_frame(index), width=SIDEBAR_BUTTON_WIDTH, height=SIDEBAR_BUTTON_HEIGHT)
           self.button_list[index].put(x=self.x, y=index*SIDEBAR_BUTTON_HEIGHT)

    # 生成指针
    def label(self):
        global label_
        label_ = tk.Label(sidebar_frame, text="|")
        label_.place(x=SIDEBAR_BUTTON_WIDTH, y=0, width=SIDEBAR_LABEL_WIDTH, height=SODEBAR_LABEL_HEIGHT)

    # 生成框架
    def frame(self):
        for frame in self.frames:
            frame.place(x=self.frame_x, y=self.frame_y, width=self.frame_width, height=self.frame_height)
        
        self.frames[0].tkraise()  # 将第一个frame置于顶层

    # 更改显示的框架
    def change_frame(self, index):
        self.frames[index].tkraise()
        label_.place(x=SIDEBAR_BUTTON_WIDTH, y=index*SIDEBAR_BUTTON_HEIGHT, width=SIDEBAR_LABEL_WIDTH, height=SODEBAR_LABEL_HEIGHT)

    # 底部的退出按钮
    def bottom_button(self):
        button = Button(master=sidebar_frame, text="退出", command=lambda event: self.master.destroy(), width=SIDEBAR_BUTTON_WIDTH, height=SIDEBAR_BUTTON_HEIGHT)
        button.put(x=0, y=self.sidebar_height-SIDEBAR_BUTTON_HEIGHT)

# 按钮
class Button(tk.Label):
    def __init__(self, master, text, command, width=BUTTON_WIDTH, height=BUTTON_HEIGHT):
        super().__init__(master)

        # 设置变量
        self.master = master
        self.text = text
        self.width = width - 1
        self.height = height - 1
        self.command = command

        self.x, self.y = 0, 0

        # 设置组件
        self.config(text=text)

        self.config(cursor=BUTTON_CURSOR)

        self.config(borderwidth=BUTTON_BORDERWIDTH)
        self.config(relief=BUTTON_RELIEF)

        self.config(background=BUTTON_BACKGROUND)
        self.config(foreground=BUTTON_FOREGROUND)

        # 组件功能
        self.bind("<Enter>", lambda event: self.config(background=BUTTON_BACKGROUND_MOUSE))
        self.bind("<Leave>", lambda event: self.config(background=BUTTON_BACKGROUND))
        self.bind("<Button-1>", self.command)

    # 放置组件
    def put(self, x, y):
        self.x = x
        self.y = y
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

    # 重新设置组建的长和宽
    def reset(self, width, height):
        self.width = width - 1
        self.height = height - 1
        self.put(x=self.x, y=self.y, width=self.width, height=self.height)


# 输入框
class Text(tk.Text):
    def __init__(self, master, text, x=0, y=0, width=SIDEBAR_FRAME_WIDTH-SCROLLBAR_WIDTH, height=SIDEBAR_FRAME_HEIGHT/2):
        super().__init__(master)

        # 设置变量
        self.master = master
        self.text = text
        self.x, self.y = x, y
        self.width, self.height = width, height

        # 设置组件
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)
        self.scrollbar_y = ttk.Scrollbar(self.master, command=self.yview)
        self.scrollbar_y.place(x=self.width, y=self.y, width=SCROLLBAR_WIDTH, height=self.height)
        self.config(yscrollcommand=self.scrollbar_y.set)

        self.insert(tk.END, self.text)


# 测试
if __name__ == "__main__":
    window = Window()  # 生成窗口
    frames = [BasicFrame(window), CalcFrame(window), HelpFrame(window)]
    sidebar = Sidebar(master=window, frames=frames, texts=SIDEBAR_BUTTON_TEXTS)  # 生成边框

    window.mainloop()  # 显示窗口
