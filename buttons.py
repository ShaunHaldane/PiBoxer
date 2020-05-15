from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1 = 12
button2 = 16
button3 = 18
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while 1:
    if GPIO.input(button1)==0:
        print("Button 1 was pressed")
        sleep(1)
    if GPIO.input(button2)==0:
        print("Button 2 was pressed")
        sleep(1)
    if GPIO.input(button3)==0:
        print("Button 3 was pressed")
        sleep(1)
