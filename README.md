# MAX6675 communication using an RP2040-based board

The goal of this project is to give my first steps using micropyton on an RP2040-based board.

## Step by step

1. Configure the board to use micropython. Follow the official documentation if in doubts https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf but, in a nutshell:
- while pressing the BOOTSEL button, connect the board through USB and then release the button
- a USB mass-storage device will appear; copy the micropython firmware (under assets/)
- reset the board by reconnecting it. 

2. Generate the environment

```
make environment
```

This will create a virtual environment which you can access by:

```
$ source venv/bin/activate
```

3. Flash the firmware using ```rshell```

```
make flash
```
and reset the board.

4. If you have a USB2serial adapter, you can enter the serial terminal with

```
make serial
```