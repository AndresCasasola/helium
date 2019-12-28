import serial
import sys
import time

arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)

t0 = time.time()
data = 0

arduino.reset_input_buffer()	# Clean buffer

while True:

	arduino.reset_input_buffer()	# Clean buffer

	data = arduino.readline()
	# if data:
	# 	data.rstrip('\n')

	alldata = data.split(',')

	tdata = alldata[0]
	hdata = alldata[1]
	ldata = alldata[2]

	t = time.time() - t0
	sys.stdout.write(tdata + ' ' + hdata + ' ' + ldata + '\n')

	time.sleep(1)

arduino.close()



