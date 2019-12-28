import serial
import sys
import time

arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)

t0 = time.time()
data = 0

while True:

	#sdata = arduino.readline();
	#data = int(sdata.strip('\n'))
	arduino.read(size=50) # Clean buffer
	arduino.reset_input_buffer()

	tdata = float( arduino.read(size=4) )
	hdata = float( arduino.read(size=4) )
	ldata = float( arduino.read(size=4) )

	t = time.time() - t0
	sys.stdout.write(str(tdata) + ' ' + str(hdata) + ' ' + str(ldata) + ' - ' + str(int(t)) + 's' + '\n')

	time.sleep(1)

arduino.close()



