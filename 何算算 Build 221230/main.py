import tkinter as tk
from tkinter import ttk, messagebox as msg

import math
import random

import threading as thread

import time

import webbrowser as web

import os


# 主窗口
class Win(tk.Tk):
    def __init__(self):
        super().__init__()

        # 常量
        self.width, self.height = 800, 400
        self.screenwidth, self.screenheight = self.winfo_screenwidth(), self.winfo_screenheight()
        self.size = "%dx%d+%d+%d" % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.title_text = "何算算 Build 221230 by Lonely-Pea"
        
        # 设置基本信息
        self.geometry(self.size)
        self.resizable(False, False)
        self.title(self.title_text)  # 设置标题


# 主界面
class Desktop(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # 设置基本信息
        self.pack(fill=tk.BOTH, expand=True)

        # 变量
        self.circle_var_r_entry = tk.StringVar()
        self.circle_var_s_entry = tk.StringVar()
        self.circle_var_c_entry = tk.StringVar()
        self.circle_var_s_and_c_answer = tk.StringVar()
        self.circle_var_r_answer = tk.StringVar()
        self.circle_var_throw_entry = tk.StringVar()
        self.circle_var_pi_answer = tk.StringVar()

        self.parallelogram_width_entry = tk.StringVar()
        self.parallelogram_height_entry = tk.StringVar()
        self.parallelogram_s_c_diagonal_answer = tk.StringVar()

        self.triangle_a_entry = tk.StringVar()
        self.triangle_b_entry = tk.StringVar()
        self.triangle_c_entry = tk.StringVar()
        self.triangle_answer = tk.StringVar()

        self.trapezium_s_up_entry = tk.StringVar()
        self.trapezium_s_down_entry = tk.StringVar()
        self.trapezium_h_entry = tk.StringVar()
        self.trapezium_s_answer = tk.StringVar()
        self.trapezium_c_up_entry = tk.StringVar()
        self.trapezium_c_down_entry = tk.StringVar()
        self.trapezium_a_entry = tk.StringVar()
        self.trapezium_b_entry = tk.StringVar()
        self.trapezium_c_answer = tk.StringVar()

        self.function_one_x1_entry = tk.StringVar()
        self.function_one_y1_entry = tk.StringVar()
        self.fucntion_one_x2_entry = tk.StringVar()
        self.fucntion_one_y2_entry = tk.StringVar()
        self.function_one_answer = tk.StringVar()

        # 圆形计算界面框架
        self.circle_frame = ttk.LabelFrame(self, text="圆形相关计算")
        self.circle_frame.place(x=0, y=0, width=self.master.width / 3, height=self.master.height / 2)

        # 方形计算界面框架
        self.parallelogram_frame = ttk.LabelFrame(self, text="方形相关计算")
        self.parallelogram_frame.place(x=self.master.width / 3, y=0, width=self.master.width / 3, height=self.master.height / 2)

        # 三角形计算界面框架
        self.triangle_frame = ttk.LabelFrame(self, text="三角形相关计算")
        self.triangle_frame.place(x=self.master.width / 3 * 2, y=0, width=self.master.width / 3, height=self.master.height / 2)

        # 梯形计算界面框架
        self.trapezium_frame = ttk.LabelFrame(self, text="梯形相关计算")
        self.trapezium_frame.place(x=0, y=self.master.height / 2, width=self.master.width / 3, height=self.master.height / 2)

        # 函数计算界面框架
        self.function_frame = ttk.LabelFrame(self, text="函数相关计算")
        self.function_frame.place(x=self.master.width / 3, y=self.master.height / 2, width=self.master.width / 3 * 2 - 20, height=self.master.height / 2 - 20)

        # 帮助栏界面框架
        self.help_frame = tk.Frame(self, background="white")
        self.help_frame.place(x=self.master.width-20, y=self.master.height/2, width=20, height=self.master.height/2)
 
        # 点名基本信息
        self.basic_label = tk.Label(self, text="何算算 v1.0 by", anchor=tk.E, font=("微软雅黑", 10))
        self.basic_label.place(x=self.master.width / 3, y=self.master.height - 20, width=self.master.width / 3 - 10, height=20) 
        self.author_label = tk.Label(self, text="Lonely-Pea", anchor=tk.W, font=("微软雅黑", 10, "underline"), cursor="hand2", foreground="blue")
        self.author_label.place(x=self.master.width / 3 * 2 - 10, y=self.master.height - 20, width=self.master.width / 3 - 10, height=20)

        # 事件
        self.author_label.bind("<Button-1>", lambda x: web.open("https://space.bilibili.com/543334144?spm_id_from=333.1007.0.0"))

        # 界面显示
        self.circle()
        self.parallelogram()
        self.triangle()
        self.trapezium()
        self.function()
        self.help_()

    # 圆形界面
    def circle(self):
        tk.Label(self.circle_frame, text="计算面积/周长").place(x=0, y=0, width=self.master.width / 3, height=20)
        tk.Label(self.circle_frame, text="输入半径:", anchor="w").place(x=0, y=20, width=60, height=20)
        ttk.Entry(self.circle_frame, textvariable=self.circle_var_r_entry).place(x=60, y=20, width=self.master.width / 3 - 100, height=20)
        tk.Label(self.circle_frame, text="结果：", anchor="w").place(x=0, y=40, width=60, height=20)
        ttk.Entry(self.circle_frame, textvariable=self.circle_var_s_and_c_answer).place(x=60, y=40, width=self.master.width / 3 - 100, height=20)
        ttk.Button(self.circle_frame, text="计算", cursor="hand2", command=self.circle_s_and_c).place(x=self.master.width/3-40, y=20, width=40, height=40)

        ttk.Separator(self.circle_frame).place(x=1, y=62, width=self.master.width / 3 - 2, height=1)  # 分隔线

        tk.Label(self.circle_frame, text="计算半径").place(x=0, y=65, width=self.master.width / 3, height=20)
        tk.Label(self.circle_frame, text="输入面积/周长：", anchor="w").place(x=0, y=85, width=120, height=20)
        ttk.Entry(self.circle_frame, textvariable=self.circle_var_s_entry).place(x=120, y=85, width=(self.master.width / 3 - 120 - 50) / 2, height=20)
        tk.Label(self.circle_frame, text="/").place(x=120+(self.master.width/3-120-50)/2, y=85, width=10, height=20)
        ttk.Entry(self.circle_frame, textvariable=self.circle_var_c_entry).place(x=120+10+(self.master.width/3-120-50)/2, y=85, width=(self.master.width/3-120-50)/2, height=20)
        tk.Label(self.circle_frame, text="结果：", anchor="w").place(x=0, y=105, width=60, height=20)
        ttk.Entry(self.circle_frame, textvariable=self.circle_var_r_answer).place(x=60, y=105, width=self.master.width/3-100, height=20)
        ttk.Button(self.circle_frame, text="计算", cursor="hand2", command=self.circle_r).place(x=self.master.width/3-40, y=85, width=40, height=40)

        ttk.Separator(self.circle_frame).place(x=1, y=137, width=self.master.width / 3 - 2, height=1)  # 分隔线

        tk.Label(self.circle_frame, text="计算π").place(x=0, y=140, width=self.master.width / 3 - 40, height=20)
        tk.Label(self.circle_frame, text="投点数：", anchor="w").place(x=0, y=160, width=60, height=20)
        ttk.Entry(self.circle_frame, textvariable=self.circle_var_throw_entry).place(x=60, y=160, width=60, height=20)
        tk.Label(self.circle_frame, text="结果：", anchor="w").place(x=120, y=160, width=45, height=20)
        ttk.Entry(self.circle_frame, textvariable=self.circle_var_pi_answer).place(x=165, y=160, width=60, height=20)
        ttk.Button(self.circle_frame, text="计算", cursor="hand2", command=self.circle_pi).place(x=self.master.width/3-40, y=140, width=40, height=40)

    # 圆形界面 - 计算面积/周长
    def circle_s_and_c(self):
        try:
            if self.circle_var_r_entry.get() == "":
                self.entry_text_shine(var=self.circle_var_r_entry, text_shine="不能为空！")
            else:
                r_entry = float(self.circle_var_r_entry.get())
                self.circle_var_s_and_c_answer.set(f"S={r_entry**2}π; C={2*r_entry}π")
        except Exception:
            self.entry_text_shine(var=self.circle_var_r_entry, text_shine="无法计算！")

    # 圆形界面 - 计算半径
    def circle_r(self):
        try:
            if self.circle_var_s_entry.get() == "" and self.circle_var_c_entry.get() == "":
                self.entry_text_shine(var=self.circle_var_s_entry, text_shine="至少有一个不为空！")
            else:
                if self.circle_var_s_entry.get() != "":
                    s_entry = float(self.circle_var_s_entry.get())
                    self.circle_var_r_answer.set(f"r=({s_entry}/π)**0.5")
                else:
                    c_entry = float(self.circle_var_c_entry.get())
                    self.circle_var_r_answer.set(f"r={c_entry/2}π")
        except Exception:
            self.entry_text_shine(var=self.circle_var_s_entry, text_shine="无法计算！")

    # 圆形界面 - 计算π
    def circle_pi(self):
        def calc_pi(n):  # 计算π
            hits=0
            dist=0
            pi_num=0
            N=int(n)
            for i in range(1,N):
                x,y=random.random(),random.random()
                dist=math.sqrt(x**2+y**2)
                if dist<=1.0:
                    hits=hits+1
                pi_num=4*(hits/N)
                pi=str(pi_num)
                self.master.update()
                self.circle_var_pi_answer.set(f"π={pi}")

        try:
            if self.circle_var_throw_entry.get() == "":
                self.entry_text_shine(var=self.circle_var_throw_entry, text_shine="不能为空！")
            else:
                throw_entry = float(self.circle_var_throw_entry.get())
                calc_pi(n=throw_entry)
        except Exception:
            self.entry_text_shine(var=self.circle_var_throw_entry, text_shine="无法计算！")

    # 方形界面
    def parallelogram(self):
        tk.Label(self.parallelogram_frame, text="计算面积/周长/对角线").place(x=0, y=0, width=self.master.width/3, height=20)
        tk.Label(self.parallelogram_frame, text="长：", anchor="w").place(x=0, y=20, width=60, height=20)
        ttk.Entry(self.parallelogram_frame, textvariable=self.parallelogram_width_entry).place(x=60, y=20, width=self.master.width/3-100, height=20)
        tk.Label(self.parallelogram_frame, text="宽：", anchor="w").place(x=0, y=40, width=60, height=20)
        ttk.Entry(self.parallelogram_frame, textvariable=self.parallelogram_height_entry).place(x=60, y=40, width=self.master.width/3-100, height=30)
        tk.Label(self.parallelogram_frame, text="结果：", anchor="w").place(x=0, y=60, width=60, height=20)
        ttk.Entry(self.parallelogram_frame, textvariable=self.parallelogram_s_c_diagonal_answer).place(x=60, y=60, width=self.master.width/3-100, height=20)
        ttk.Button(self.parallelogram_frame, text="计算", cursor="hand2", command=self.parallelogram_s_c_diagonal).place(x=(self.master.width/3-50)/2, y=80, width=50, height=30)

    # 方形界面 - 计算
    def parallelogram_s_c_diagonal(self):
        try:
            if self.parallelogram_width_entry.get() == "" or self.parallelogram_height_entry.get() == "":
                self.entry_text_shine(var=self.parallelogram_width_entry, text_shine="不能为空！") if self.parallelogram_width_entry.get() == "" else self.entry_text_shine(var=self.parallelogram_height_entry, text_shine="不能为空！")
            else:
                width_entry = float(self.parallelogram_width_entry.get())
                height_entry = float(self.parallelogram_height_entry.get())
                self.parallelogram_s_c_diagonal_answer.set(f"S={width_entry*height_entry}; C={width_entry*2+height_entry*2}; 对角线={(width_entry**2+height_entry**2)**0.5}")
        except Exception:
            self.entry_text_shine(var=self.parallelogram_width_entry, text_shine="无法计算！")

    # 三角形界面
    def triangle(self):
        tk.Label(self.triangle_frame, text="计算面积/周长/高").place(x=0, y=0, width=self.master.width/3, height=20)
        tk.Label(self.triangle_frame, text="a边长：", anchor="w").place(x=0, y=20, width=60, height=20)
        ttk.Entry(self.triangle_frame, textvariable=self.triangle_a_entry).place(x=60, y=20, width=self.master.width/3-100, height=20)
        tk.Label(self.triangle_frame, text="b边长：", anchor="w").place(x=0, y=40, width=60, height=20)
        ttk.Entry(self.triangle_frame, textvariable=self.triangle_b_entry).place(x=60, y=40, width=self.master.width/3-100, height=20)
        tk.Label(self.triangle_frame, text="c边长：", anchor="w").place(x=0, y=60, width=60, height=20)
        ttk.Entry(self.triangle_frame, textvariable=self.triangle_c_entry).place(x=60, y=60, width=self.master.width/3-100, height=20)
        tk.Label(self.triangle_frame, text="结果：", anchor="w").place(x=0, y=80, width=60, height=20)
        ttk.Entry(self.triangle_frame, textvariable=self.triangle_answer).place(x=60, y=80, width=self.master.width/3-100, height=20)
        ttk.Button(self.triangle_frame, text="计算", cursor="hand2", command=self.triangle_s_c_h).place(x=self.master.width/3-40, y=20, width=40, height=80)

        tk.Label(self.triangle_frame, text="注意：两边之和大于第三边, \n两边之差小于第三边！", anchor="w", justify="left").place(x=0, y=100, width=self.master.width/3, height=40)

    # 三角形界面 - 计算
    def triangle_s_c_h(self):
        try:
            if self.triangle_a_entry.get() == "" or self.triangle_b_entry.get() == "" or self.triangle_c_entry.get() == "":
                thread1 = thread.Thread(target=self.entry_text_shine, args=(self.triangle_a_entry, "不能为空！", ))
                thread2 = thread.Thread(target=self.entry_text_shine, args=(self.triangle_b_entry, "不能为空！", ))
                thread3 = thread.Thread(target=self.entry_text_shine, args=(self.triangle_c_entry, "不能为空！", ))

                for i in [thread1, thread2, thread3]:
                    i.start()
            
            else:
                a_entry, b_entry, c_entry = float(self.triangle_a_entry.get()), float(self.triangle_b_entry.get()), float(self.triangle_c_entry.get())
                c_answer = a_entry + b_entry + c_entry
                s_answer = (0.5*c_answer*(0.5*c_answer-a_entry)*(0.5*c_answer-b_entry)*(0.5*c_answer-c_entry))**0.5
                h_a, h_b, h_c = s_answer * 2 / a_entry, s_answer * 2 / b_entry, s_answer * 2 / c_entry
                self.triangle_answer.set(f"C={c_answer}; S={s_answer}; 在a边长上的h={h_a}; 在b边长上的h={h_b}; 在c边长上的h={h_c}")
        except Exception:
            thread1 = thread.Thread(target=self.entry_text_shine, args=(self.triangle_a_entry, "无法计算！", ))
            thread2 = thread.Thread(target=self.entry_text_shine, args=(self.triangle_b_entry, "无法计算！", ))
            thread3 = thread.Thread(target=self.entry_text_shine, args=(self.triangle_c_entry, "无法计算！", ))

            for i in [thread1, thread2, thread3]:
                i.start()

    # 梯形界面
    def trapezium(self):
        tk.Label(self.trapezium_frame, text="计算面积").place(x=0, y=0, width=self.master.width/3, height=20)
        tk.Label(self.trapezium_frame, text="上底：", anchor="w").place(x=0, y=20, width=50, height=20)
        ttk.Entry(self.trapezium_frame, textvariable=self.trapezium_s_up_entry).place(x=50, y=20, width=50, height=20)
        tk.Label(self.trapezium_frame, text="下底：", anchor="w").place(x=120, y=20, width=50, height=20)
        ttk.Entry(self.trapezium_frame, textvariable=self.trapezium_s_down_entry).place(x=170, y=20, width=50, height=20)
        tk.Label(self.trapezium_frame, text="高：", anchor="w").place(x=0, y=40, width=50, height=20)
        ttk.Entry(self.trapezium_frame, textvariable=self.trapezium_h_entry).place(x=50, y=40, width=50, height=20)
        tk.Label(self.trapezium_frame, text="结果：", anchor="w").place(x=120, y=40, width=50, height=20)
        ttk.Entry(self.trapezium_frame, textvariable=self.trapezium_s_answer).place(x=170, y=40, width=50, height=20)
        ttk.Button(self.trapezium_frame, text="计算", cursor="hand2", command=self.trapezium_s).place(x=self.master.width/3-40, y=20, width=40, height=40)

        ttk.Separator(self.trapezium_frame).place(x=1, y=62, width=self.master.width/3-2, height=2)
        
        tk.Label(self.trapezium_frame, text="计算周长").place(x=0, y=65, width=self.master.width/3, height=20)
        tk.Label(self.trapezium_frame, text="上底：", anchor="w").place(x=0, y=85, width=50, height=20)
        ttk.Entry(self.trapezium_frame, textvariable=self.trapezium_c_up_entry).place(x=50, y=85, width=50, height=20)
        tk.Label(self.trapezium_frame, text="下底：", anchor="w").place(x=120, y=85, width=50, height=20)
        ttk.Entry(self.trapezium_frame, textvariable=self.trapezium_c_down_entry).place(x=170, y=85, width=50, height=20)
        tk.Label(self.trapezium_frame, text="左边长：", anchor="w").place(x=0, y=105, width=50, height=20)
        ttk.Entry(self.trapezium_frame, textvariable=self.trapezium_a_entry).place(x=50, y=105, width=50, height=20)
        tk.Label(self.trapezium_frame, text="右边长：", anchor="w").place(x=120, y=105, width=50, height=20)
        ttk.Entry(self.trapezium_frame, textvariable=self.trapezium_b_entry).place(x=170, y=105, width=50, height=20)
        tk.Label(self.trapezium_frame, text="结果：", anchor="w").place(x=0, y=125, width=50, height=20)
        ttk.Entry(self.trapezium_frame, textvariable=self.trapezium_c_answer).place(x=50, y=125, width=170, height=20)
        ttk.Button(self.trapezium_frame, text="计算", cursor="hand2", command=self.trapezium_c).place(x=self.master.width/3-40, y=85, width=40, height=60)

        ttk.Separator(self.trapezium_frame).place(x=1, y=147, width=self.master.width/3-2, height=1)

        tk.Label(self.trapezium_frame, text="注意：三边之和大于第四边！", anchor="w").place(x=0, y=150, width=self.master.width/3, height=20)

    # 梯形界面 - 计算面积
    def trapezium_s(self):
        try:
            if self.trapezium_s_up_entry.get() == "" or self.trapezium_s_down_entry.get() == "" or self.trapezium_h_entry.get() == "":
                for i in [self.trapezium_s_up_entry, self.trapezium_s_down_entry, self.trapezium_h_entry]:
                    thread_i = thread.Thread(target=self.entry_text_shine, args=(i, "不能为空！", ))
                    thread_i.start()
            else:
                up_entry = float(self.trapezium_s_up_entry.get())
                down_entry = float(self.trapezium_s_down_entry.get())
                h_entry = float(self.trapezium_h_entry.get())
                s_answer = (up_entry + down_entry) * h_entry / 2
                self.trapezium_s_answer.set(f"S={s_answer}")
        except Exception:
            for i in [self.trapezium_s_up_entry, self.trapezium_s_down_entry, self.trapezium_h_entry]:
                thread_i = thread.Thread(target=self.entry_text_shine, args=(i, "无法计算！", ))
                thread_i.start()

    # 梯形界面 - 计算周长
    def trapezium_c(self):
        try:
            if self.trapezium_c_up_entry.get() == "" or self.trapezium_c_down_entry.get() == "" or self.trapezium_a_entry.get() == "" or self.trapezium_b_entry.get() == "":
                for i in [self.trapezium_c_up_entry, self.trapezium_c_down_entry, self.trapezium_a_entry, self.trapezium_b_entry]:
                    thread_i = thread.Thread(target=self.entry_text_shine, args=(i, "不能为空！", ))
                    thread_i.start()
            else:
                up_entry = float(self.trapezium_c_up_entry.get())
                down_entry = float(self.trapezium_c_down_entry.get())
                a_entry = float(self.trapezium_a_entry.get())
                b_entry = float(self.trapezium_b_entry.get())
                c_answer = up_entry + down_entry + a_entry + b_entry
                self.trapezium_c_answer.set(f"C={c_answer}")
        except Exception:
            for i in [self.trapezium_c_up_entry, self.trapezium_c_down_entry, self.trapezium_a_entry, self.trapezium_b_entry]:
                    thread_i = thread.Thread(target=self.entry_text_shine, args=(i, "无法计算！", ))
                    thread_i.start()

    # 函数界面
    def function(self):
        tk.Label(self.function_frame, text="一次函数").place(x=0, y=0, width=self.master.width / 3 * 2 - 20, height=20)
        tk.Label(self.function_frame, text="x1:", anchor="w").place(x=0, y=20, width=50, height=20)
        ttk.Entry(self.function_frame, textvariable=self.function_one_x1_entry).place(x=50, y=20, width=50, height=20)
        tk.Label(self.function_frame, text="y1:", anchor="w").place(x=100, y=20, width=50, height=20)
        ttk.Entry(self.function_frame, textvariable=self.function_one_y1_entry).place(x=150, y=20, width=50, height=20)
        tk.Label(self.function_frame, text="x2:", anchor="w").place(x=200, y=20, width=50, height=20)
        ttk.Entry(self.function_frame, textvariable=self.fucntion_one_x2_entry).place(x=250, y=20, width=50, height=20)
        tk.Label(self.function_frame, text="y2:", anchor="w").place(x=300, y=20, width=50, height=20)
        ttk.Entry(self.function_frame, textvariable=self.fucntion_one_y2_entry).place(x=350, y=20, width=50, height=20)
        tk.Label(self.function_frame, text="结果:", anchor="w").place(x=0, y=40, width=50, height=20)
        ttk.Entry(self.function_frame, textvariable=self.function_one_answer).place(x=50, y=40, width=350, height=20)
        ttk.Label(self.function_frame, text="格式:y=kx+b", anchor="w").place(x=0, y=60, width=100, height=20)
        ttk.Button(self.function_frame, text="计算", cursor="hand2", command=self.function_one).place(x=150, y=60, width=100, height=25)

        tk.Label(self.function_frame, text="提示:目前仅支持1次函数的计算!", anchor="w").place(x=0, y=85, width=200, height=20)

    # 函数界面 - 一元一次方程计算
    def function_one(self):
        try:
            x1, y1, x2, y2 = float(self.function_one_x1_entry.get()), float(self.function_one_y1_entry.get()), float(self.fucntion_one_x2_entry.get()), float(self.fucntion_one_y2_entry.get())
            k_answer = (y2 - y1) / (x2 - x1)
            b_answer = y1 - (y2 - y1) / (x2 - x1) * x1
            b = ""
            if b_answer > 0:
                b = "+"+str(b_answer)
            elif b_answer < 0:
                b = str(b_answer)
            else:
                b = ""
            text = f"y={k_answer}x{b}"
            self.function_one_answer.set(text)

        except Exception as e:
            msg.showerror("错误", "不能为空,或无法计算!")

    # 帮助界面
    def help_(self):
        ttk.Button(self.help_frame, text="计\n算\n器", cursor="hand2", command=self.start_calc).place(x=0, y=0, width=20, height=60)
        ttk.Button(self.help_frame, text="关\n于\n软\n件", cursor="hand2", command=self.about_software).place(x=0, y=60, width=20, height=80)

    def start_calc(self):
        thread_calc = thread.Thread(target=os.system, args=("calc.exe", ))
        thread_calc.start()

    def about_software(self):
        with open("help.txt", "r", encoding="utf-8") as f:
            text_word = f.read()

        toplevel = Toplevel(master=self.master, title="关于软件")
        text = Text(master=toplevel, x=0, y=0, width=200, height=170, state="disabled", text=text_word)

        ttk.Button(toplevel, text="确定", command=lambda: toplevel.destroy(), cursor="hand2").place(x=150, y=170, width=50, height=30)

    # 输入框内容闪烁
    def entry_text_shine(self, var, text_shine=""):
        text = text_shine
        for i in range(0, 6):
            if i in [0, 2, 4]:
                var.set("")
            else:
                var.set(text)
            self.master.update()
            time.sleep(0.1)


# 二级窗口
class Toplevel(tk.Toplevel):
    def __init__(self, master, title):
        super().__init__(master)
        self.master = master

        self.title(title)

        self.width, self.height = 200, 200
        self.screenwidth, self.screenheight = self.winfo_screenwidth(), self.winfo_screenheight()

        self.geometry("%dx%d+%d+%d" % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2))
        self.resizable(False, False)


# 文本框
class Text(tk.Frame):
    def __init__(self, master, x, y, width, height, state, text):
        super().__init__(master)
        self.master = master

        self.x, self.y, self.width, self.height = x, y, width, height
        self.state = state
        self.text_word = text

        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

        self.text = tk.Text(self, wrap="none")
        self.text.place(x=0, y=0, width=self.width - 20, height=self.height - 20)

        self.scrollbar_x = ttk.Scrollbar(self, command=self.text.xview, orient=tk.HORIZONTAL)
        self.scrollbar_x.place(x=0, y=self.height - 20, width=self.width - 20, height=20)

        self.scrollbar_y = ttk.Scrollbar(self, command=self.text.yview)
        self.scrollbar_y.place(x=self.width - 20, y=0, width=20, height=self.height - 20)

        self.text.config(xscrollcommand=self.scrollbar_x.set)
        self.text.config(yscrollcommand=self.scrollbar_y.set)

        self.text.insert(tk.END, self.text_word)
        self.text.config(state=self.state)


# 测试
if __name__ == "__main__":
    win = Win()
    desktop = Desktop(master=win)

    win.mainloop()
