#sudo pip3 install adafruit-circuitpython-charlcd
import board
import digitalio
#import pulseio
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#GPIO.setup(16, GPIO.OUT) # blue
#GPIO.setup(20, GPIO.OUT) # green
#GPIO.setup(21, GPIO.OUT) # red

GPIO.setup(26, GPIO.OUT) # contrast
contrast = GPIO.PWM(26, 50)
contrast.start(0)

time.sleep(0.1) # get it ready

contrast.ChangeDutyCycle(50)

#GPIO.output(16, GPIO.HIGH)
#GPIO.output(20, GPIO.LOW) # green
#GPIO.output(21, GPIO.HIGH)

# convert to PWM
red =    digitalio.DigitalInOut(board.D16)
green =  digitalio.DigitalInOut(board.D20)
blue =   digitalio.DigitalInOut(board.D21)

lcd_rs = digitalio.DigitalInOut(board.D11)
lcd_en = digitalio.DigitalInOut(board.D9)
lcd_d7 = digitalio.DigitalInOut(board.D5)
lcd_d6 = digitalio.DigitalInOut(board.D6)
lcd_d5 = digitalio.DigitalInOut(board.D13)
lcd_d4 = digitalio.DigitalInOut(board.D19)

#red =   pulseio.PWMOut(board.D3)
#green = pulseio.PWMOut(board.D5)
#blue =  pulseio.PWMOut(board.D6)

lcd_columns = 16
lcd_rows = 2

#import adafruit_character_lcd.character_lcd as characterlcd
#lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

import adafruit_character_lcd.character_lcd as characterlcd
lcd = characterlcd.Character_LCD_RGB(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, red, green, blue)

#lcd.create_char(1, [2, 3, 2, 2, 14, 30, 12, 0])

#lcd.backlight = True
lcd.color = [100, 0, 0]
#lcd.message = "6500 RPM\n              \x01N"

n = 0
for x in range(0, 10):
	list = [6500 + n, " RPM\n               N"]
	lcd.message = ''.join(str(y) for y in list)
	n=n+10
	time.sleep(0.5)

time.sleep(5)
