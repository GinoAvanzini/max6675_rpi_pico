from machine import SPI, Pin, UART
import time
import json


class MAX6675:
    def __init__(self, SPI, CS):
        self.SPI = SPI
        self.CS = CS

    def get_temperature_bytes(self):
        rxdata = bytearray(2)
        try:
            self.CS.value(0)
            time.sleep_us(1)
            rxdata = self.SPI.read(2)
        finally:
            time.sleep_us(1)
            self.CS.value(1)
        return rxdata

    def get_temperature_C(self):
        temperature_binary = int.from_bytes(self.get_temperature_bytes(), 'big')
        bitmask = ~(0b1000_0000_0000_0111)
        temp_dec = int( (temperature_binary & bitmask) >> 3)
        return temp_dec*0.25


def main():
    # Initialize SPI and chip select objects
    spi = SPI(0, sck=Pin(18), mosi=None, miso=Pin(16), 
            baudrate=4_000_000, polarity=0, phase=1, bits=8)
    cs = Pin(17, mode=Pin.OUT, value=1)
    
    uart1 = UART(1)
    uart1.init(baudrate=1_000_000, tx=Pin(4), rx=Pin(5))

    max6675 = MAX6675(spi, cs)

    time.sleep(2)
    uart1.flush()

    while(True):
        temperature = max6675.get_temperature_C()
        temp_as_json = json.dumps({"T_thc": temperature,
                                    "ts": time.ticks_ms() % 2**16})
        uart1.write("{}".format(temp_as_json) + "\n")
        time.sleep_ms(250)


if __name__ == "__main__":
    main()
