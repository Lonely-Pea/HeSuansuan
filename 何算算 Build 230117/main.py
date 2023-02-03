# 导入模块
import tkinter as tk  # 导入tkinter模块实现窗口
from tkinter import ttk  # 导入tkinter.ttk模块实现显示系统UI，导入tkinter.messagebox模块实现系统弹窗
from functions import *


# 常量
TITLE = "何算算 Build 230117 By Lonely-Pea"  #  窗口标题
WINDOW_WIDTH = 400  # 窗口宽度
WINDOW_HEIGHT = 300  # 窗口高度
BUTTON_WIDTH = 50  # 按钮宽度
BUTTON_HEIGHT = 25  # 按钮高度
BUTTON_BACKGROUND = "White"  # 按钮背景色
BUTTON_FOREGROUND = "Black"  # 按钮文字颜色
BUTTON_BACKGROUND_MOUSE = "GhostWhite"  # 按钮被触碰后背景的颜色
BUTTON_FOREGROUND_MOUSE = "black"  # 按钮被触碰后文字的颜色
BUTTON_CURSOR = "hand2"  # 鼠标伸进按钮时的样式
BUTTON_BORDERWIDTH = 1  # 按钮边框大小
BUTTON_RELIEF = "solid"  # 按钮边框样式
LABEL_WIDTH = 80  # 标签宽度
LABEL_HEIGHT = 25  # 标签高度
ENTRY_WIDTH = 120  # 输入框宽度
ENTRY_HEIGHT = 25  # 输入框高度
NOTEBOOK_WIDTH = 400  # 选项卡宽度
NOTEBOOK_HEIGHT = 300  # 选项卡高度

SCROLLBAR_WIDTH = 20  # 滚动条的宽度
SCROLLBAR_HEIGHT = 255  # 滚动条的高度

HELP_TEXT = """
帮助信息
一、关于软件
1. 软件名称: 何算算 build 230117
2. 软件作者: Lonely-Pea
3. 软件使用操作系统: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11及更高的Windows操作系统
4. 软件收费: 免费
5. 软件官网: https://lonely-pea.github.io/HeSuansuan/

二、软件使用说明
1. 适用的几何计算: 圆形、梯形、方形、三角形、函数
2. 几何计算时的注意事项: 
①在计算梯形时，要注意三边之和大于第4边
②在计算三角形是，要注意两边之和大于第三边，两边之差小于第三边
③在进行计算时，请不要输入不能被转化为数字的字符串(包括π、e和运算符号)
④在计算圆周率时，请不要输入过大的数，否则会导致计算错误
⑥该软件目前仅支持面的计算，暂不支持体的计算，请及时查看软件官网获取关于支持计算体的软件
⑦软件自配计算器，可以进行简单的科学计算

三、鸣谢
感谢QQ号为1625396311的人对该软件的编写！
"""


# 主窗口对象
class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # 导入常量
        self.title_ = TITLE
        self.width, self.height = WINDOW_WIDTH, NOTEBOOK_HEIGHT
        self.x = (self.winfo_screenwidth() - self.width) / 2  # 窗口的x位置
        self.y = (self.winfo_screenheight() - self.height) / 2  # 窗口的y位置
        
        # 设置窗口
        self.title(self.title_)  # 设置窗口标题
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))  # 设置窗口位置
        self.resizable(False, False)  # 设置窗口不可更改大小


# 顶部选项卡对象
class NoteBook(ttk.Notebook):
    def __init__(self, master):
        super().__init__(master)

        # 导入常量
        self.master = master
        self.width, self.height = NOTEBOOK_WIDTH, WINDOW_HEIGHT
        self.x, self.y = 0, 0

        # 设置选项卡
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

        # 添加选项卡
        self.add(CircleFrame(master=self.master), text="圆形计算")
        self.add(TrapeziumFrame(master=self.master), text="梯形计算")
        self.add(ParallelogramFrame(master=self.master), text="方形计算")
        self.add(TriangleFrame(master=self.master), text="三角形计算")
        self.add(FucntionFrame(master=self.master), text="函数计算")
        self.add(CalcFrame(master=self.master), text="计算器")
        self.add(AboutFrame(master=self.master), text="帮助")
        self.add(LevelUpDataFrame(master=self.master), text="日志")


# 圆形计算界面框架对象
class CircleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 导入常量
        self.master = master

        # 设置变量
        self.calc_s_c_entry_r = tk.StringVar()
        self.calc_r_entry_s = tk.StringVar()
        self.calc_r_entry_c = tk.StringVar()
        self.calc_pi_entry_number = tk.StringVar()
        
        self.answer_s_c = tk.StringVar()
        self.answer_r = tk.StringVar()
        self.answer_pi = tk.StringVar()

        # 设置界面
        self.s_c()
        self.r()
        self.pi()

    # 圆的面积和周长计算
    def s_c(self):
        frame = ttk.LabelFrame(self, text="计算面积/周长")
        frame.place(x=0, y=0, width=NOTEBOOK_WIDTH, height=NOTEBOOK_HEIGHT / 3)

        tk.Label(frame, text="输入半径:", anchor="w").place(x=0, y=0, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_s_c_entry_r).place(x=LABEL_WIDTH, y=0, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="计算结果:", anchor="w").place(x=0, y=LABEL_HEIGHT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.answer_s_c).place(x=LABEL_WIDTH, y=LABEL_HEIGHT, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        Button(master=frame, text="x", command=lambda x: self.calc_s_c_entry_r.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(master=frame, text="复制", command=lambda x: copy(self.answer_s_c.get())).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(master=frame, text="开始计算", command=lambda x: circle_calc_s_c(master=self.master, var_r=self.calc_s_c_entry_r, var_answer=self.answer_s_c)).place(x=LABEL_WIDTH+ENTRY_WIDTH+BUTTON_WIDTH+1, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

    # 圆的半径计算
    def r(self):
        frame = ttk.LabelFrame(self, text="计算半径")
        frame.place(x=0, y=NOTEBOOK_HEIGHT / 3, width=NOTEBOOK_WIDTH, height=NOTEBOOK_HEIGHT / 3)

        tk.Label(frame, text="输入面积:", anchor="w").place(x=0, y=0, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_r_entry_s).place(x=LABEL_WIDTH, y=0, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="或输入周长:", anchor="w").place(x=0, y=LABEL_HEIGHT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_r_entry_c).place(x=LABEL_WIDTH, y=LABEL_HEIGHT, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="计算结果:", anchor="w").place(x=0, y=LABEL_HEIGHT*2, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.answer_r).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*2, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        Button(frame, text="x", command=lambda x: self.calc_r_entry_s.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x", command=lambda x: self.calc_r_entry_c.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="复制", command=lambda x: copy(self.answer_r.get())).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="开始计算", command=lambda x: circle_calc_r(master=self.master, var_s=self.calc_r_entry_s, var_c=self.calc_r_entry_c, var_answer=self.answer_r)).place(x=LABEL_WIDTH+ENTRY_WIDTH+BUTTON_WIDTH+1, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

    # 圆周率计算
    def pi(self):
        frame = ttk.LabelFrame(self, text="计算π")
        frame.place(x=0, y=NOTEBOOK_HEIGHT / 3 * 2, width=NOTEBOOK_WIDTH, height=NOTEBOOK_HEIGHT / 3)

        tk.Label(frame, text="输入投点数:", anchor="w").place(x=0, y=0, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_pi_entry_number).place(x=LABEL_WIDTH, y=0, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="计算结果:", anchor="w").place(x=0, y=LABEL_HEIGHT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.answer_pi).place(x=LABEL_WIDTH, y=LABEL_HEIGHT, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        Button(frame, text="x", command=lambda x: self.calc_pi_entry_number.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="复制", command=lambda x: copy(self.answer_pi.get())).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="开始计算", command=lambda x: circle_calc_pi(self.master, self.calc_pi_entry_number, self.answer_pi)).place(x=LABEL_WIDTH+ENTRY_WIDTH+BUTTON_WIDTH+1, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# 梯形计算界面框架
class TrapeziumFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 导入常量
        self.master = master

        # 设置变量
        self.calc_s_enter_up = tk.StringVar()
        self.calc_s_enter_down = tk.StringVar()
        self.calc_s_enter_h = tk.StringVar()
        self.answer_s = tk.StringVar()

        self.calc_c_enter_up = tk.StringVar()
        self.calc_c_enter_down = tk.StringVar()
        self.calc_c_enter_left = tk.StringVar()
        self.calc_c_enter_right = tk.StringVar()
        self.answer_c = tk.StringVar()

        # 设置界面
        self.s()
        self.c()

    # 梯形的面积计算
    def s(self):  
        frame = ttk.LabelFrame(self, text="计算面积")
        frame.place(x=0, y=0, width=NOTEBOOK_WIDTH, height=NOTEBOOK_HEIGHT / 2 - 25)

        tk.Label(frame, text="上底:", anchor="w").place(x=0, y=0, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_s_enter_up).place(x=LABEL_WIDTH, y=0, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="下底:", anchor="w").place(x=0, y=LABEL_HEIGHT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_s_enter_down).place(x=LABEL_WIDTH, y=LABEL_HEIGHT, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="高:", anchor="w").place(x=0, y=LABEL_HEIGHT*2, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_s_enter_h).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*2, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="计算结果:", anchor="w").place(x=0, y=LABEL_HEIGHT*3, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.answer_s).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*3, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)

        Button(frame, text="x", command=lambda x: self.calc_s_enter_up.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x", command=lambda x: self.calc_s_enter_down.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x", command=lambda x: self.calc_s_enter_h.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="复制", command=lambda x: copy(self.answer_s.get())).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="开始计算", command=lambda x: trapezium_calc_s(self.master, self.calc_s_enter_up, self.calc_s_enter_down, self.calc_s_enter_h, self.answer_s)).place(x=LABEL_WIDTH+ENTRY_WIDTH+BUTTON_WIDTH+1, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

    # 梯形的周长计算
    def c(self):
        frame = ttk.LabelFrame(self, text="计算周长")
        frame.place(x=0, y=NOTEBOOK_HEIGHT / 2 - 25, width=NOTEBOOK_WIDTH, height=NOTEBOOK_HEIGHT / 2 + 25)

        tk.Label(frame, text="上底:", anchor="w").place(x=0, y=0, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_c_enter_up).place(x=LABEL_WIDTH, y=0, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="下底:", anchor="w").place(x=0, y=LABEL_HEIGHT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_c_enter_down).place(x=LABEL_WIDTH, y=LABEL_HEIGHT, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="左边长:", anchor="w").place(x=0, y=LABEL_HEIGHT*2, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_c_enter_left).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*2, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="右边长:", anchor="w").place(x=0, y=LABEL_HEIGHT*3, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.calc_c_enter_right).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*3, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="结果:", anchor="w").place(x=0, y=LABEL_HEIGHT*4, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.answer_c).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*4, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)

        Button(frame, text="x", command=lambda x: self.calc_c_enter_up.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x", command=lambda x: self.calc_c_enter_down.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x", command=lambda x: self.calc_c_enter_left.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x", command=lambda x: self.calc_c_enter_right.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="复制", command=lambda x: copy(self.answer_c.get())).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="开始计算", command=lambda x: trapezium_calc_c(self.master, self.calc_c_enter_up, self.calc_c_enter_down, self.calc_c_enter_left, self.calc_c_enter_right, self.answer_c)).place(x=LABEL_WIDTH+ENTRY_WIDTH+BUTTON_WIDTH+1, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)


# 方形计算界面框架
class ParallelogramFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 导入常量
        self.master = master

        # 设置变量
        self.enter_a = tk.StringVar()
        self.enter_b = tk.StringVar()
        self.answer = tk.StringVar()

        # 设置界面
        self.s_c_diagonal()

    # 方形的面积/周长/对角线计算
    def s_c_diagonal(self):
        frame = ttk.LabelFrame(self, text="计算面积/周长/对角线")
        frame.place(x=0, y=0, width=NOTEBOOK_WIDTH, height=NOTEBOOK_HEIGHT)

        tk.Label(frame, text="长:", anchor="w").place(x=0, y=0, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.enter_a).place(x=LABEL_WIDTH, y=0, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="宽:", anchor="w").place(x=0, y=LABEL_HEIGHT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.enter_b).place(x=LABEL_WIDTH, y=LABEL_HEIGHT, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="计算结果:", anchor="w").place(x=0, y=LABEL_HEIGHT*2, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.answer).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*2, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        
        Button(frame, text="x", command=lambda x: self.enter_a.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x", command=lambda x: self.enter_b.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="复制", command=lambda x: copy(self.answer.get())).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="开始计算", command=lambda x: parallelogram_calc_s_c_diagonal(self.master, self.enter_a, self.enter_b, self.answer)).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# 三角形计算界面框架
class TriangleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 导入常量
        self.master = master

        # 设置变量
        self.enter_a = tk.StringVar()
        self.enter_b = tk.StringVar()
        self.enter_c = tk.StringVar()
        self.answer = tk.StringVar()

        # 设置界面
        self.s_c_h()

    # 三角形的面积/周长/高计算
    def s_c_h(self):
        frame = ttk.LabelFrame(self, text="计算面积/周长/高")
        frame.place(x=0, y=0, width=NOTEBOOK_WIDTH, height=NOTEBOOK_HEIGHT)

        tk.Label(frame, text="a边长:", anchor="w").place(x=0, y=0, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.enter_a).place(x=LABEL_WIDTH, y=0, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="b边长:", anchor="w").place(x=0, y=LABEL_HEIGHT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.enter_b).place(x=LABEL_WIDTH, y=LABEL_HEIGHT, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="c边长:", anchor="w").place(x=0, y=LABEL_HEIGHT*2, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.enter_c).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*2, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="计算结果:", anchor="w").place(x=0, y=LABEL_HEIGHT*3, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.answer).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*3, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        
        Button(frame, text="x", command=lambda x: self.enter_a.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x", command=lambda x: self.enter_b.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x", command=lambda x: self.enter_c.set("")).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="复制", command=lambda x: copy(self.answer.get())).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="开始计算", command=lambda x: triangle_calc_s_c_h(self.master, self.enter_a, self.enter_b, self.enter_c, self.answer)).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)


# 函数计算框架
class FucntionFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 导入常量
        self.master = master

        # 设置变量
        self.first_enter_x1, self.first_enter_y1 = tk.StringVar(), tk.StringVar()
        self.first_enter_x2, self.first_enter_y2 = tk.StringVar(), tk.StringVar()
        self.answer_first = tk.StringVar()

        # 设置界面
        self.first()

    # 一次函数计算
    def first(self):
        frame = ttk.LabelFrame(self, text="计算一次函数")
        frame.place(x=0, y=0, width=NOTEBOOK_WIDTH, height=7*BUTTON_HEIGHT)

        tk.Label(frame, text="x1:", anchor="w").place(x=0, y=0, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.first_enter_x1).place(x=LABEL_WIDTH, y=0, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="y1:", anchor="w").place(x=0, y=LABEL_HEIGHT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.first_enter_y1).place(x=LABEL_WIDTH, y=LABEL_HEIGHT, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="x2:", anchor="w").place(x=0, y=LABEL_HEIGHT*2, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.first_enter_x2).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*2, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="y2:", anchor="w").place(x=0, y=LABEL_HEIGHT*3, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.first_enter_y2).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*3, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)
        tk.Label(frame, text="计算结果:", anchor="w").place(x=0, y=LABEL_HEIGHT*4, width=LABEL_WIDTH, height=LABEL_HEIGHT)
        tk.Entry(frame, textvariable=self.answer_first).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*4, width=ENTRY_WIDTH, height=ENTRY_HEIGHT)

        # 生成清空输入框的按钮
        vars = [self.first_enter_x1, self.first_enter_y1, self.first_enter_x2, self.first_enter_y2]
        for var in vars:
            Button(frame, text="x", command=lambda x, arg="", var_=var: var_.set(arg)).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*vars.index(var), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        Button(frame, text="复制", command=lambda x: copy(self.answer_first.get())).place(x=LABEL_WIDTH+ENTRY_WIDTH, y=LABEL_HEIGHT*4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="开始计算", command=lambda x: fucntion_first(self.master, self.first_enter_x1, self.first_enter_x2, self.first_enter_y1, self.first_enter_y2, self.answer_first)).place(x=LABEL_WIDTH, y=LABEL_HEIGHT*5, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)


# 计算器界面框架
class CalcFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 导入常量
        self.master = master

        # 设置变量
        self.entry_var = tk.StringVar()

        # 设置界面
        self.calc()

    # 计算器界面
    def calc(self):
        global entry
        frame = tk.Frame(self)
        frame.place(x=0, y=0, width=NOTEBOOK_WIDTH, height=NOTEBOOK_HEIGHT)
        
        tk.Label(frame, text="输入框:").place(x=0, y=0, width=LABEL_WIDTH, height=LABEL_HEIGHT)

        entry = tk.Entry(frame, textvariable=self.entry_var)
        entry.place(x=(NOTEBOOK_WIDTH-ENTRY_WIDTH*2)/2, y=0, width=ENTRY_WIDTH*2, height=ENTRY_HEIGHT)

        Button(frame, text="复制", command=lambda x: copy(self.entry_var.get())).place(x=(NOTEBOOK_WIDTH-ENTRY_WIDTH*2)/2+ENTRY_WIDTH*2+2, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        
        Button(frame, text="C", command=lambda x: self.entry_var.set("")).place(x=0, y=ENTRY_HEIGHT+1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="<-", command=lambda x: entry.delete(len(self.entry_var.get())-1, tk.END)).place(x=BUTTON_WIDTH+1, y=ENTRY_HEIGHT+1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="(", command=lambda x: self.add("(")).place(x=BUTTON_WIDTH*2+2, y=ENTRY_HEIGHT+1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text=")", command=lambda x: self.add(")")).place(x=BUTTON_WIDTH*3+3, y=ENTRY_HEIGHT+1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="√", command=lambda x: self.add("**0.5")).place(x=BUTTON_WIDTH*4+4, y=ENTRY_HEIGHT+1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        
        Button(frame, text="7", command=lambda x: self.add("7")).place(x=0, y=BUTTON_HEIGHT*2+2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="8", command=lambda x: self.add("8")).place(x=BUTTON_WIDTH+1, y=BUTTON_HEIGHT*2+2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="9", command=lambda x: self.add("9")).place(x=BUTTON_WIDTH*2+2, y=BUTTON_HEIGHT*2+2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="÷", command=lambda x: self.add("/")).place(x=BUTTON_WIDTH*3+3, y=BUTTON_HEIGHT*2+2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x²", command=lambda x: self.add("**2")).place(x=BUTTON_WIDTH*4+4, y=BUTTON_HEIGHT*2+2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        Button(frame, text="4", command=lambda x: self.add("4")).place(x=0, y=BUTTON_HEIGHT*3+3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="5", command=lambda x: self.add("5")).place(x=BUTTON_WIDTH+1, y=BUTTON_HEIGHT*3+3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="6", command=lambda x: self.add("6")).place(x=BUTTON_WIDTH*2+2, y=BUTTON_HEIGHT*3+3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="×", command=lambda x: self.add("*")).place(x=BUTTON_WIDTH*3+3, y=BUTTON_HEIGHT*3+3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="x^y", command=lambda x: self.add("**")).place(x=BUTTON_WIDTH*4+4, y=BUTTON_HEIGHT*3+3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        Button(frame, text="1", command=lambda x: self.add("1")).place(x=0, y=BUTTON_HEIGHT*4+4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="2", command=lambda x: self.add("2")).place(x=BUTTON_WIDTH+1, y=BUTTON_HEIGHT*4+4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="3", command=lambda x: self.add("3")).place(x=BUTTON_WIDTH*2+2, y=BUTTON_HEIGHT*4+4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="-", command=lambda x: self.add("-")).place(x=BUTTON_WIDTH*3+3, y=BUTTON_HEIGHT*4+4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="=", command=lambda x: calc_(self.master, self.entry_var, entry)).place(x=BUTTON_WIDTH*4+4, y=BUTTON_HEIGHT*4+4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT*2+1)

        Button(frame, text="0", command=lambda x: self.add("0")).place(x=0, y=BUTTON_HEIGHT*5+5, width=BUTTON_WIDTH*2+1, height=BUTTON_HEIGHT)
        Button(frame, text=".", command=lambda x: self.add(".")).place(x=BUTTON_WIDTH*2+2, y=BUTTON_HEIGHT*5+5, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="+", command=lambda x: self.add("+")).place(x=BUTTON_WIDTH*3+3, y=BUTTON_HEIGHT*5+5, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        Button(frame, text="n!", command=lambda x: calc_jiecheng(self.master, self.entry_var)).place(x=BUTTON_WIDTH*5+15, y=ENTRY_HEIGHT+1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="log", command=lambda x: calc_log(self.master, self.entry_var, entry)).place(x=BUTTON_WIDTH*6+16, y=ENTRY_HEIGHT+1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        Button(frame, text="sin", command=lambda x: triangle_fucntions_calc(self.master, self.entry_var, 1, entry)).place(x=BUTTON_WIDTH*5+15, y=BUTTON_HEIGHT*2+2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="cos", command=lambda x: triangle_fucntions_calc(self.master, self.entry_var, 2, entry)).place(x=BUTTON_WIDTH*6+16, y=BUTTON_HEIGHT*2+2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        Button(frame, text="tan", command=lambda x: triangle_fucntions_calc(self.master, self.entry_var, 3, entry)).place(x=BUTTON_WIDTH*5+15, y=BUTTON_HEIGHT*3+3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="sinh", command=lambda x: triangle_fucntions_calc(self.master, self.entry_var, 4, entry)).place(x=BUTTON_WIDTH*6+16, y=BUTTON_HEIGHT*3+3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        Button(frame, text="cosh", command=lambda x: triangle_fucntions_calc(self.master, self.entry_var, 5, entry)).place(x=BUTTON_WIDTH*5+15, y=BUTTON_HEIGHT*4+4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        Button(frame, text="tanh", command=lambda x: triangle_fucntions_calc(self.master, self.entry_var, 6, entry)).place(x=BUTTON_WIDTH*6+16, y=BUTTON_HEIGHT*4+4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

        Button(frame, text="π", command=lambda x: pi_display(self.master, self.entry_var, entry)).place(x=BUTTON_WIDTH*5+15, y=BUTTON_HEIGHT*5+5, width=BUTTON_WIDTH*2+1, height=BUTTON_HEIGHT)

    def add(self, add_):
        entry.insert(tk.END, add_)


# 帮助界面框架
class AboutFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 导入常量
        self.master = master

        # 设置变量
        self.help_word = HELP_TEXT

        # 设置界面
        self.text = Text(self, text=self.help_word)


# 软件更新日志界面
class LevelUpDataFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 导入常量
        self.master = master

        # 设置变量
        with open("text.log", "r", encoding="utf-8") as log:
            self.text = log.read()

        # 设置界面
        self.text_ = Text(self, text=self.text)


# 按钮对象
class Button(tk.Label):
    def __init__(self, master, text, command):
        super().__init__(master)

        # 导入常量
        self.master = master
        self.text = text
        self.command = command
        self.background, self.foreground = BUTTON_BACKGROUND, BUTTON_FOREGROUND
        self.background_mouse, self.foreground_mouse = BUTTON_BACKGROUND_MOUSE, BUTTON_FOREGROUND_MOUSE
        self.cursor = BUTTON_CURSOR
        self.borderwidth = BUTTON_BORDERWIDTH
        self.relief = BUTTON_RELIEF

        # 设置对象
        self.config(text=self.text)
        self.config(cursor=self.cursor)
        self.config(borderwidth=self.borderwidth)
        self.config(relief=self.relief)
        self.config(background=self.background)
        self.config(foreground=self.foreground)

        # 添加对象功能
        self.bind("<Button-1>", self.command)  # 鼠标点击对象的事件
        self.bind("<Enter>", self.enter)  # 鼠标伸进对象的事件
        self.bind("<Leave>", self.leave)  # 鼠标离开对象的事件

    def enter(self, event=None):  # 鼠标伸进对象的事件
        self.config(background=self.background_mouse)
        self.config(foreground=self.foreground_mouse)

    def leave(self, event=None):  # 鼠标离开对象的事件
        self.config(background=self.background)
        self.config(foreground=self.foreground)


# 文本框对象
class Text(tk.Frame):
    def __init__(self, master, text):
        super().__init__(master)

        # 导入常量
        self.master = master
        self.width, self.height = NOTEBOOK_WIDTH-SCROLLBAR_WIDTH, NOTEBOOK_HEIGHT-SCROLLBAR_WIDTH-LABEL_HEIGHT
        self.scrollbar_width, self.scrollbar_height = SCROLLBAR_WIDTH, SCROLLBAR_HEIGHT

        # 设置变量
        self.text_ = text

        # 设置对象
        self.place(x=0, y=0, width=NOTEBOOK_WIDTH, height=NOTEBOOK_HEIGHT)
        self.text = tk.Text(self)
        self.text.place(x=0, y=0, width=self.width, height=self.height)
        self.scrollbar_x = ttk.Scrollbar(self, command=self.text.xview, orient=tk.HORIZONTAL)
        self.scrollbar_x.place(x=0, y=self.height, width=NOTEBOOK_WIDTH-self.scrollbar_width, height=self.scrollbar_width)
        self.scrollbar_y = ttk.Scrollbar(self, command=self.text.yview)
        self.scrollbar_y.place(x=self.width, y=0, width=self.scrollbar_width, height=self.scrollbar_height)
        self.text.config(xscrollcommand=self.scrollbar_x.set)
        self.text.config(yscrollcommand=self.scrollbar_y.set)

        self.text.insert(tk.END, self.text_)
        self.text.config(state="disabled")
        self.text.config(wrap="none")


# 测试
if __name__ == "__main__":
    window = Window()  # 生成窗口
    notebook = NoteBook(master=window)  # 生成选项卡

    window.mainloop()
