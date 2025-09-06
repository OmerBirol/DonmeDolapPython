from machine import ADC, Pin,I2C, PWM
import utime
import time
import machine
from picobricks import SHTC3, MotorDriver, IR_RX, NEC_16, APDS9960, CY8CMBR3116
POT_PIN = 4
SLOW = 0
FAST = 255
pot = ADC(Pin(POT_PIN))
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
motor = MotorDriver(i2c)

while True:
    pot_value = pot.read()
    speed = 0

    
    if pot_value < 1000:
        speed = 0
        utime.sleep_ms(300)
        
    elif pot_value < 2000:
        speed = int((SLOW + FAST) / 4)
        utime.sleep_ms(300)
    elif pot_value < 3000:
        speed = int((SLOW + FAST) / 3)
    else:
        speed = int(FAST/2)
        utime.sleep_ms(300)

    motor.dc(1, speed, 0)  

    print("pot_value:", pot_value, "- speed:", speed)
    utime.sleep_ms(100)