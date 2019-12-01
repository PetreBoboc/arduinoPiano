import serial
import time
import os
     
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:

    var = ser.readline()
    var = float(var)

    instrument = 0 # 0 = piano; 1 = drum machine

    if instrument==0:
        if var==1:
            os.system("aplay ./res/piano/A0.wav")
        if var==2:
            os.system("aplay ./res/piano/A1.wav")
        if var==3:
            os.system("aplay ./res/piano/A2.wav")
        if var==4:
            os.system("aplay ./res/piano/A3.wav")
        if var==5:
            os.system("aplay ./res/piano/A4.wav")
        if var==6:
            os.system("aplay ./res/piano/A5.wav")
    else:
        if var==1:
            os.system("aplay ./res/drums/A0.wav")
        if var==2:
            os.system("aplay ./res/drums/A1.wav")
        if var==3:
            os.system("aplay ./res/drums/A2.wav")
        if var==4:
            os.system("aplay ./res/drums/A3.wav")
        if var==5:
            os.system("aplay ./res/drums/A4.wav")
        if var==6:
            os.system("aplay ./res/drums/A5.wav")
