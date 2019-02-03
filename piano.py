import serial
import time
import winsound
     
ser = serial.Serial('COM13', 9600)

while True:
    A0 = ser.readline()
    A0 = int(A0)
    if A0<800:
        print(A0)

    A1 = ser.readline()
    A1 = int(A1)
    if A1<800:
        print(A1)

    A2 = ser.readline()
    A2 = int(A2)
    if A2<800:
        print(A2)

    A3 = ser.readline()
    A3 = int(A3)
    if A3<800:
        print(A3)

    A4 = ser.readline()
    A4 = int(A4)
    if A4<800:
        print(A4)
    
    A5 = ser.readline()
    A5 = int(A5)
    if A5<800:
        print(A5)
