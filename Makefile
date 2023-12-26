VENV_ACT = source venv/bin/activate

environment:
	python -m venv venv ; ${VENV_ACT} ; pip install -r requirements.txt

clean:
	rm -rf venv/

flash:
	${VENV_ACT} ; rshell cp src/main_spi.py /pyboard/main.py

serial:
	minicom -o -D /dev/ttyACM1 -b 1000000
