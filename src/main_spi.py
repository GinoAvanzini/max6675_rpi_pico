from machine import SPI, Pin, UART
import time
import sys

spi = SPI(0, sck=Pin(18), mosi=None, miso=Pin(16), baudrate=400000, polarity=0, phase=1, bits=8)
cs = Pin(17, mode=Pin.OUT, value=1)

uart1 = UART(1)

def main():
    uart1.init(baudrate=115200  , tx=Pin(4), rx=Pin(5))
    time.sleep(2)
    uart1.write("Hello from pico!")
    #spi.init(baudrate=400000, polarity=0, phase=1, bits=16,
    #             firstbit=SPI.MSB)
    while(True):
        temperature_binary = int.from_bytes(read_max6675(), 'big')
        bitmask = ~(0b1000_0000_0000_0111)
        temp_dec = int( (temperature_binary & bitmask) >> 3)
        uart1.write(str(temp_dec*0.25) + "\r\n")
        time.sleep_ms(500)


def read_max6675():
    rxdata = bytearray(2)
    try:
        cs.value(0)
        time.sleep_ms(10)
        rxdata = spi.read(2)
    finally:
        time.sleep_ms(10)
        cs.value(1)
    return rxdata

if __name__ == "__main__":
    main()

