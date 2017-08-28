import time
import RPi.GPIO as GPIO
import wiringpi as pi

INTAVAL = 1
SLEEPTIME = 3
SENSOR_PIN = 18
LED_PIN = 4

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

pi.wiringPiSetupGpio()
pi.pinMode(led_pin, 1)

st = time.time() - INTAVAL

while True:
  print( GPIO.input(SENSOR_PIN))
  if(GPIO.input(SENSOR_PIN) == GPIO.HIGH) and (st + INTAVAL < time.time()):
    st = time.time()
    print("人を感知しました")
    pi.digitalWrite(LED_PIN, 1)
  else:
    pi.digitalWrite(LED_PIN, 0)

  time.sleep(SLEEPTIME)
