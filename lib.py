#Library (saved as lib.py)
#Has all the essential functions and actions that the car can do
from machine import Pin
import utime

class car:
    def __init__(self):
        self.enable_A = Pin(21, Pin.OUT)
        self.enable_B = Pin(25, Pin.OUT)
        
        self.left_f = Pin(18, Pin.OUT)
        self.left_b = Pin(19, Pin.OUT)
        
        self.right_f = Pin(23, Pin.OUT)
        self.right_b = Pin(22, Pin.OUT)
        
        self.enable_A.on()
        self.enable_B.on()

    def forward(self):
        self.left_b.off()
        self.right_b.off()
        self.left_f.on()
        self.right_f.on()

    def backward(self):
        self.left_f.off()
        self.right_f.off()
        self.left_b.on()
        self.right_b.on()

    def left(self):
        self.left_f.off()
        self.right_b.off()
        self.left_b.off()
        self.right_f.on()
        utime.sleep(1)
        self.right_f.off()

    def leftinfinitydrift(self):
        self.left_f.off()
        self.right_b.off()
        self.left_b.off()
        self.right_f.on()
        self.left_b.on()

    def leftdrift(self):
        self.left_f.off()
        self.right_b.off()
        self.left_b.on()
        self.right_f.on()
        utime.sleep(0.57)
        self.right_f.off()
        self.left_b.off()

    def right(self):
        self.left_b.off()
        self.right_b.off()
        self.right_f.off()
        self.left_f.on()
        utime.sleep(1)
        self.left_f.off()

    def rightinfinitydrift(self):
        self.left_b.off()
        self.right_b.off()
        self.right_f.off()
        self.left_f.on()
        self.right_b.on()

    def rightdrift(self):
        self.left_b.off()
        self.right_f.off()
        self.left_f.on()
        self.right_b.on()
        utime.sleep(0.57)
        self.right_b.off()
        self.left_f.off()

    def stop(self):
        self.left_b.off()
        self.right_b.off()
        self.left_f.off()
        self.right_f.off()
