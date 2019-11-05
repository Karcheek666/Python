import serial
import time

ser = serial.Serial('COM3', 9600) 

time.sleep(2)

ser.write(b'1') ##sends '1' to serial 

time.sleep(5) ##motor runs for this period

ser.write(b'0') ##sends '0' to serial on arduino to turn motor off

ser.close()