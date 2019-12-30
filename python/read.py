import serial
import sys
import time

def checkPacket(alldata):
	r = ((len(alldata) == 4) and (float(alldata[0]) < 150) and float(alldata[0]) >= 0.0 and float(alldata[1]) < 150 and float(alldata[1]) >= 0.0 and float(alldata[2]) < 150 and float(alldata[2]) >= 0.0)
	return r

arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)

t0 = time.time()
data = 0

arduino.reset_input_buffer()	# Clean buffer

while True:

	arduino.reset_input_buffer()	# Clean buffer
	data = arduino.readline()		# Clean possible cut data

	data = arduino.readline()
	# if data:
	# 	data.rstrip('\n')

	alldata = data.split(',')
	if (checkPacket(alldata)):
		tdata = float(alldata[0])
		hdata = float(alldata[1])
		ldata = float(alldata[2])
		sys.stdout.write(str(tdata) + ' ' + str(hdata) + ' ' + str(ldata) + '\n')
		time.sleep(1)

	else:
		print('Packet discarded')	

arduino.close()



