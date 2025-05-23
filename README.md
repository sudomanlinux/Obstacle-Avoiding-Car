# Obstacle-Avoiding-Car
ATTENTION: All code is in micropython and was flashed into the ESP32's firmware first.

This is a modified version of an obstacle-avoiding car using a custom ESP32 board, an ultrasonic sensor and a servo motor. It has two motors and two lithium-ion batteries (3.7V). On startup, it moves to the front. Suppose an obstacle is detected (using the ultrasonic sensor). In that case, it moves its neck using the servo motor (The neck has the ultrasonic sensor attached on the head) to the left, and it calculates the distance of the closest object. It then turns right and does the same. Whichever side has a greater free path to move in, it turns in that direction and starts moving. This continues in a loop. 
