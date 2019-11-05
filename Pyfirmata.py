#TO Import Arduino firmware (ig)
from pyfirmata import Arduino, util
import time

#To configure the port to which arduino is connected
board = Arduino("COM3")
#Creating a variable for storing the input 
loopTimes = input('How many times would you like the LED to blink: ')
#Printing what its doing
print("Blinking " + loopTimes + " times.")
#Loop the program how many times the input is 
for x in range(int(loopTimes)):
  board.digital[13].write(1)#Turning the led on
  time.sleep(0.2)#Time to stay on
  board.digital[13].write(0)#Turning the led off
  time.sleep(0.2)#time to stay off