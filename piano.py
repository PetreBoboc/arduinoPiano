import serial
import time
import winsound
     
ser = serial.Serial('COM13', 9600)

while True:

    var = ser.readline()
    var = float(var)

    instrument = 1

    if instrument==0:
        if var==1:
            winsound.PlaySound("res\piano\A0.wav", winsound.SND_ALIAS)
        if var==2:
            winsound.PlaySound("res\piano\A1.wav", winsound.SND_ALIAS)
        if var==3:
            winsound.PlaySound("res\piano\A2.wav", winsound.SND_ALIAS)
        if var==4:
            winsound.PlaySound("res\piano\A3.wav", winsound.SND_ALIAS)
        if var==5:
            winsound.PlaySound("res\piano\A4.wav", winsound.SND_ALIAS)
        if var==6:
            winsound.PlaySound("res\piano\A5.wav", winsound.SND_ALIAS)
    else:
        if var==1:
            winsound.PlaySound("res\drums\A0.wav", winsound.SND_ALIAS)
        if var==2:
            winsound.PlaySound("res\drums\A1.wav", winsound.SND_ALIAS)
        if var==3:
            winsound.PlaySound("res\drums\A2.wav", winsound.SND_ALIAS)
        if var==4:
            winsound.PlaySound("res\drums\A3.wav", winsound.SND_ALIAS)
        if var==5:
            winsound.PlaySound("res\drums\A4.wav", winsound.SND_ALIAS)
        if var==6:
            winsound.PlaySound("res\drums\A5.wav", winsound.SND_ALIAS)