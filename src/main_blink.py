from machine import Pin, Timer

led = Pin("LED", Pin.OUT)
tim = Timer()
def tick(timer):
    global led
    led.toggle()

tim.init(period=250, mode=Timer.PERIODIC, callback=tick)
