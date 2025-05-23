#The main obstacle avoiding car code (saved as main.py)
import machine
import utime
from machine import Pin
import lib

servo = machine.PWM(Pin(15))
servo.freq(50)

trig = Pin(13, Pin.OUT)
echo = Pin(14, Pin.IN, Pin.PULL_DOWN)

def get_distance():
    trig.off()
    utime.sleep_us(1)
    trig.on()
    utime.sleep_us(10)
    trig.off()
    
    while echo.value() == 0:
        send_time = utime.ticks_us()
    while echo.value() == 1:
        received_time = utime.ticks_us()
    
    duration = received_time - send_time
    distance = (0.0343 * duration) / 2
    return distance

while True:
    
    a = 90
    formula0 = int(2000000 * a / 180) + 500000
    servo.duty_ns(formula0)
    utime.sleep(0.1)

    lib.car().forward()
    utime.sleep(0.5)

    object_distance = get_distance()

    if object_distance <= 25:
        lib.car().stop()

        
        x = 180
        formula = int(2000000 * x / 180) + 500000
        servo.duty_ns(formula)
        utime.sleep(0.5)
        left_distance = get_distance()

        
        y = 0
        formula2 = int(2000000 * y / 180) + 500000
        servo.duty_ns(formula2) 
        utime.sleep(0.5)
        right_distance = get_distance()

        
        if left_distance > right_distance:
            lib.car().leftdrift()
        elif right_distance > left_distance:
            lib.car().rightdrift()
        else:
            lib.car().leftdrift()
        
        utime.sleep(1)
        lib.car().forward()  
    else:
        utime.sleep(0.1)

    utime.sleep(0.1)
