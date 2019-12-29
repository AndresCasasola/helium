import serial
import sys
import time

# Functions
def get_time():
    strings = time.strftime("%Y, %m, %d, %H, %M, %S")
    t = strings.split(',')
    numbers = [ int(x) for x in t ]
    return numbers

def get_date():
    numbers = get_time()
    date = str(numbers[2]) + '_' + str(numbers[1]) + '_' + str(numbers[0])
    return date

def checkPacket(alldata):
	r = ((len(alldata) == 4) and (float(alldata[0]) < 150) and float(alldata[0]) >= 0.0 and float(alldata[1]) < 150 and float(alldata[1]) >= 0.0 and float(alldata[2]) < 150 and float(alldata[2]) >= 0.0)
	return r

# Configuration
filename = 'data/' + get_date() + '.csv'
portname = '/dev/ttyACM0'

# Init config
fd = open(filename, 'w')
fd.write('day' + '\t' + 'month' + '\t' + 'year' + '\t' + 'hour' + '\t' + 'minute' + '\t' + 'second' + '\t' + 'temperature' + '\t' + 'humidity' + '\t' + 'light' + '\n')
fd.close()

# Init arduino serial
arduino = serial.Serial(portname, baudrate=115200, timeout=3.0);
print('ttyACM0 connected')

# Variables
t0 = time.time()
tdata = 0
hdata = 0
ldata = 0
rt = 0
i = 0

# Loop
while True:
    fd = open(filename, 'a')

    arduino.reset_input_buffer()    # Clean full buffer
    data = arduino.readline()
    alldata = data.split(',')

    # Get time
    numbers = get_time()
    hour    = str(numbers[3] + 1)   # +1 in Spain
    minute  = str(numbers[4])
    second  = str(numbers[5])
    day     = str(numbers[2])
    month   = str(numbers[1])
    year    = str(numbers[0])

    if (checkPacket(alldata)):
        tdata = float(alldata[0])
        hdata = float(alldata[1])
        ldata = float(alldata[2])
		# Write to file
        fd.write(day + '\t' + month + '\t' + year + '\t' + hour + '\t' + minute + '\t' + second + '\t' + str(tdata) + '\t' + str(hdata) + '\t' + str(ldata) + '\n')
        # Print data
        print(day + '\t' + month + '\t' + year + '\t' + hour + '\t' + minute + '\t' + second + '\t' + str(tdata) + '\t' + str(hdata) + '\t' + str(ldata))
		
        fd.close()
        time.sleep(150)

    else:
        print('Packet discarded')
    

# Close
arduino.close()
fd.close()



