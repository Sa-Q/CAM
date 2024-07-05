#!/usr/bin/python

"""
###########################################################################
カメラで静止画、動画を撮影する。

#Filename      :cam.py

#Update        :2024/07/06
2024/07/06  Ver. α　0.01 SW ブッシュ で LED 点灯
############################################################################
"""
# タイマー用時刻取得拡張
import time

# ボタンスイッチ用 gpio 拡張
from gpiozero import Button

# ボタンスイッチ初期設定
SW_1 = Button(5,pull_up=False)
SW_2 = Button(6,pull_up=False)


# LED 用拡張
from gpiozero import LED

# LED 初期設定
LEDPIN1 = LED(17)
LEDPIN2 = LED(27)

#print message at the begining ---custom function
def print_message():
    print ('|********************************|')
    print ('|   カメラ撮影（Still & Movie）  |')
    print ('|********************************|\n')
    print ('Program is running...')
    print ('Press Green Switch = Still')
    print ('Press Red Switch = Movie')
    print ('Please press Ctrl+C to end the program...')

# Switch 状態把握
#read SW_PI_1's level
def ReadSW_1():
    if SW_1.is_pressed:
        sw_ = 'on'
    else:
        sw_ = 'off'
    return sw_

#read SW_PI_2's level
def ReadSW_2():
    if SW_2.is_pressed:
        sw_ = 'on'
    else:
        sw_ = 'off'
    return sw_

#main function
def main():
    loop_n = 0
    # Switch状態初期化
    sw_ = 'off'
    # 初期メッセージ表示
    print_message()
    # ループ処理開始
    while True:
        # スイッチ１状態取得
        sw_ = ReadSW_1()
        # スイッチ１プッシュ時
        if sw_ =='on':
            # LED１点灯
            LEDPIN1.on()
            time.sleep(1)
            # LED１消灯
            LEDPIN1.off()
#            break

        # スイッチ２状態取得
        sw_ = ReadSW_2()
        # スイッチ２プッシュ時
        if sw_ =='on':
            # LED２点灯
            LEDPIN2.on()
            time.sleep(1)
            # LED２消灯
            LEDPIN2.off()
#            break
    pass
    # ループ処理ここまで
#
# if run this script directly ,do:
if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)
