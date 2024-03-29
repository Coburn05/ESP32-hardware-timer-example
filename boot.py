from machine import Pin, Timer

red = Pin(21, Pin.OUT)
blue = Pin(19, Pin.OUT)

def blink(event):
    if(red.value() == False):
       red.on()
       blue.off()
    else:
       red.off()
       blue.on()
       print("new timer system")
       
blinkTimer = Timer(1)
blinkTimer.init(period = 500, mode = Timer.PERIODIC, callback = blink)
