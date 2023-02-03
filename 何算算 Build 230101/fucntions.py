import math  # 导入math模块实现数学计算
import random  # 导入random模块实现随机数的生成
import threading as thread  # 导入threading模块实现多线程
import time  # 导入time模块实现程序暂停
import clipboard as clip  # 导入clipboard模块实现复制内容


# 复制内容
def copy(text=""):
    clip.copy(text)


# 输入框闪烁
def shine(master, var, text):
    for i in range(0, 5):
        if i in [0, 2, 4]:
            var.set(text)
        else:
            var.set("")
        master.update()
        time.sleep(0.1)


# 判断字符串能否被转化成浮点数或整数
def bool_var(var):
    try:
        float(var)
        return True
    
    except Exception:
        return False


# 判断输入的值是否符合规定并闪烁字符串“无法转化”
def bool_shine(master, vars):
    """
    vars应是列表
    
    """
    var_list = []
    thread_list = []
    for i in vars:
        if i.get() == "" or bool_var(i) == False:
            var_list.append(i)
            thread_list.append(thread.Thread(target=shine, args=(master, i, "无法转化！", )))
        
        else:
            continue
    
    for i in thread_list:
        i.start()


# 圆形
# 圆形 - 计算面积和周长
def circle_calc_s_c(master, var_r, var_answer):
    """
    S = π * r ** 2
    C = 2 * π ** r

    """
    try:
        r = float(var_r.get())
        s = var_r.get() + "**2" + "π"
        c = str(r * 2) + "π"
        var_answer.set("S=%s; C=%s" % (s, c))  

    except Exception:
        bool_shine(master, vars=[var_r])


# 圆形 - 计算半径
def circle_calc_r(master, var_s, var_c, var_answer):
    """
    r = (S / π) ** 0.5
    r = C / 2 * π
    
    """
    try:
        s = float(var_s.get())
        r = "(" + var_s.get() + " / π)" + " ** 0.5"
        var_answer.set("r=%s" % r)
    
    except Exception:
        bool_shine(master, vars=[var_s, var_c])


# 圆形 - 计算圆周率
def circle_calc_pi(master, var_number, var_answer):
    """
    使用投点法求圆周率
    
    """
    try:
        number = int(var_number.get())
        hits=0
        dist=0
        pi_num=0
        for i in range(1, number):
            x,y=random.random(),random.random()
            dist=math.sqrt(x**2+y**2)
            if dist<=1.0:
                hits=hits+1
            pi_num=4*(hits/number)
            pi=str(pi_num)
            master.update()
            var_answer.set(f"π={pi}")
    
    except Exception as e:
        bool_shine(master, vars=[var_number])


# 梯形
# 梯形 - 计算面积
def trapezium_calc_s(master, var_up, var_down, var_h, var_answer):
    """
    S = (a+b) * h / 2
    
    """    
    try:
        a = float(var_up.get())
        b = float(var_down.get())
        h = float(var_h.get())
        s = str((a + b) * h / 2)
        var_answer.set("S=%s" % s)
    
    except Exception:
        bool_shine(master, vars=[var_up, var_down, var_h])


# 梯形 - 计算周长
def trapezium_calc_c(master, var_up, var_down, var_left, var_right, var_answer):
    """
    C = a + b + c + d
    
    """
    try:
        c = str(float(var_up.get()) + float(var_down.get()) + float(var_left.get()) + float(var_right.get()))
        var_answer.set("C=%s" % c)

    except Exception:
        bool_shine(master, vars=[var_up, var_down, var_left, var_right])


# 方形
# 方形 - 计算面积/周长/对角线
def parallelogram_calc_s_c_diagonal(master, var_a, var_b, var_answer):
    """
    S = a * b
    C = (a + b) * 2
    D = (a ** 2 + b ** 2) ** 0.5

    """
    try:
        a, b = float(var_a.get()), float(var_b.get())
        s = str(a * b)
        c = str((a + b) * 2)
        d = str((a ** 2 + b ** 2) ** 0.5)
        var_answer.set("S=%s; C=%s; D=%s" % (s, c, d))

    except Exception:
        bool_shine(master, vars=[var_a, var_b])


# 三角形
# 三角形 - 计算面积/周长/高
def triangle_calc_s_c_h(master, var_a, var_b, var_c, var_answer):
    """
    C = a + b + c
    S = (0.5*C*(0.5*C-a)*(0.5*C-b)*(0.5*C-c))**0.5
    h_a, h_b, h_c = S * 2 / a, S * 2 / b, S * 2 / c

    """
    try:
        a, b, c = float(var_a.get()), float(var_b.get()), float(var_c.get())
        C = float(a + b + c)
        S = float((0.5*C*(0.5*C-a)*(0.5*C-b)*(0.5*C-c))**0.5)
        h_a, h_b, h_c = str(S * 2 / a), str(S * 2 / b), str(S * 2 / c)
        var_answer.set("C=%s; S=%s; h on a=%s; h on b=%s; h on c=%s" % (str(C), str(S), h_a, h_b, h_c))
   
    except Exception as e:
        print(e)
        bool_shine(master, vars=[var_a, var_b, var_c])


# 函数
# 函数 - 求一次函数解析式
def fucntion_first(master, var_x1, var_x2, var_y1, var_y2, var_answer):
    """
    y = kx + b
    k = (y2 - y1) / (x2 - x1)
    b = y1 - (y2 - y1) / (x2 - x1) * x1

    """
    try:
        x1, x2, y1, y2 = float(var_x1.get()), float(var_x2.get()), float(var_y1.get()), float(var_y2.get())
        k = str((y2 - y1) / (x2 - x1))
        b = y1 - (y2 - y1) / (x2 - x1) * x1
        if b == 0:
            b_ = ""
        elif b > 0:
            b_ = "+" + str(b)
        else:
            b_ = str(b)
        var_answer.set(f"y={k}x{b_}")

    except Exception:
        bool_shine(master, vars=[var_x1, var_x2, var_y1, var_y2])


# 计算器
# 计算器 - 计算
def calc_(master, var):
    try:
        var.set(eval(var.get()))

    except Exception:
        bool_shine(master, vars=[var])
    