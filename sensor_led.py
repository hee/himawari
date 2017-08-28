import time
import RPi.GPIO as GPIO

INTAVAL = 1
SLEEPTIME = 3
SENSOR_PIN = 18
LED_PIN = 4

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

st = time.time() - INTAVAL

while True:
  print(GPIO.input(SENSOR_PIN))
  if(GPIO.input(SENSOR_PIN) == GPIO.HIGH) and (st + INTAVAL < time.time()):
    st = time.time()
    print("人を感知しました")
    GPIO.output(LED_PIN, GPIO.HIGH)
  else:
    GPIO.output(LED_PIN, GPIO.LOW)

  time.sleep(SLEEPTIME)
