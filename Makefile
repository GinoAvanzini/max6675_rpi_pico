VENV_ACT = source venv/bin/activate
BAUDRATE = 1000000
SERIAL_DEV := $(shell $(VENV_ACT) ; python get_dev_port.py serial)
RPICO_DEV := $(shell $(VENV_ACT) ; python get_dev_port.py cdc)

environment:
	python -m venv venv ; $(VENV_ACT) ; pip install --upgrade pip ; pip install -r requirements.txt

clean:
	rm -rf venv/

flash:
	$(VENV_ACT) ; rshell -p $(RPICO_DEV) cp src/max6675.py /pyboard/main.py

repl: 
	$(VENV_ACT) ; rshell repl
serial:
	#minicom -o -w -D $(SERIAL_DEV) -b $(BAUDRATE) 
	$(VENV_ACT) ; python -m serial.tools.miniterm $(SERIAL_DEV) $(BAUDRATE) --eol LF
