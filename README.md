# MAX6675 communication using an RP2040-based board

The goal of this project is to give my first steps using micropyton on an RP2040-based board.

## Step by step

1. Get the pico-sdk

2. Configure the microcontroller to use micropython. Follow the official documentation https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf

3. Connect to the board using rshell

```
python -m venv venv
source venv/bin/activate
pip install rshell
```

```
$ rshell
```

