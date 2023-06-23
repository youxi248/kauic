import time
import os

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"倒计时: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("时间到！")

def start_focus_clock():
    print("欢迎使用专注时钟")
    while True:
        try:
            minutes = int(input("请输入专注时长（分钟）："))
            break
        except ValueError:
            print("无效的输入，请输入一个整数！")

    countdown(minutes)

    # 播放音乐或其他提醒操作
    # 这里可以根据需要自定义

    # 清除控制台输出
    os.system("clear")  # For Linux/OS X
    # os.system("cls")  # For Windows

    print("专注时间已结束，祝你工作愉快！")

start_focus_clock()
