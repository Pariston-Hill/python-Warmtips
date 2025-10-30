import tkinter as tk
import random
import threading
import time
import sys

def show_warm_tip():
    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = 250
    window_height = 60
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)

    window.title("温馨提示")
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tips = [
        '多喝水哦~', '保持微笑呀~', '每天都要元气满满~',
        '记得吃水果~', '保持好心情~', '好好爱自己~',
        '我想你了~', '梦想成真~', '期待下一次见面~',
        '金榜题名~', '顺顺利利~', '早点休息~',
        '愿所有烦恼都消失~', '别熬夜~', '今天过得开心嘛~',
        '天冷了，多穿衣服~'
    ]
    tip = random.choice(tips)

    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque',
        'aquamarine', 'mistyrose', 'honeydew',
        'lavenderblush', 'oldlace'
    ]
    bg = random.choice(bg_colors)

    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 16),
        width=30,
        height=3
    ).pack()

    window.attributes('-topmost', True)
    window.after(10000, window.destroy)  # 每个弹窗10秒后关闭
    window.mainloop()


# 主程序
threads = []
for i in range(300):
    t = threading.Thread(target=show_warm_tip)
    threads.append(t)
    t.start()
    time.sleep(0.005)

# 等待所有弹窗结束
time.sleep(10)

# 显示最后一句话
final_window = tk.Tk()
final_window.title("温馨提示")
final_window.geometry("400x100+600+400")
final_window.configure(bg='lightyellow')
tk.Label(
    final_window,
    text="祝你未来都好好的 💛",
    bg='lightyellow',
    font=('微软雅黑', 20, 'bold'),
    width=30,
    height=3
).pack()
final_window.attributes('-topmost', True)
final_window.after(8000, lambda: (final_window.destroy(), sys.exit()))
final_window.mainloop()
