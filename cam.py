#!/home/pi/V_CAM/bin/python3

"""
###########################################################################
カメラで静止画、動画を撮影する。

#Filename      :cam.py

#Update        :2024/07/15
2024/07/15  Ver. α 0.02 OLED に文字、プログレスバー表示
2024/07/06  Ver. α 0.01 SW ブッシュ で LED 点灯
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


# OLED ディスプレイ用拡張
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

# OLED ディスプレイ用初期設定
# Raspberry Pi 4以降の場合、port=1を指定
serial = i2c(port=1, address=0x3C)
# その他の初期化パラメータを設定（必要に応じて）
device = ssd1306(serial, width=128, height=32) # 必要に応じ64

from PIL import  ImageFont
def oled_text(text,size):
    # フォントを指定
    font = ImageFont.truetype("fonts-japanese-gothic.ttf", size)
    with canvas(device) as draw:
        draw.text((0, 0), text, font=font, fill="white")

def oled_square(x1,y1,x2,y2,color):
    if color == 0:
        #矩形の描画:
        with canvas(device) as draw:
            draw.rectangle((x1,y1,x2,y2), outline="white",fill="black")
    if color == 1:
        #矩形の描画:
        with canvas(device) as draw:
            draw.rectangle((x1,y1,x2,y2), outline="white",fill="white")



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
            # OLED ディスプレイ文字出力
            text = "静止画撮影！"
            oled_text(text,22)
            time.sleep(1)
            # LED１消灯
            LEDPIN1.off()
            # １秒待って OLED ディスプレイクリア
            time.sleep(1)
            device.clear()
#            break

        # スイッチ２状態取得
        sw_ = ReadSW_2()
        # スイッチ２プッシュ時
        if sw_ =='on':
            # LED２点灯
            LEDPIN2.on()
            # プログレスバー描画
            for x in range(0,127,1):
                oled_square(0, 10, x, 21,1)
                time.sleep(0.1)
#            time.sleep( rec_time )
            # OLED ディスプレイクリア
            device.clear()
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
