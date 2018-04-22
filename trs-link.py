
# TRS80 Model 100 serial link 
#
# Leonardo Cardoso, 2018

import argparse
import serial
import time


options = argparse.ArgumentParser(description='Transfer data between a TRS80 and your computer through a serial port')
options.add_argument('--dev', help='serial device', default='/dev/cu.usbserial')
options.add_argument('--fname', help='file to process', required=True)
options.add_argument('--rate', help='baudrate (default: 1200)', type=int, default=1200)
options.add_argument('--send', help='send file to TRS80', action='store_true', default=False)
options.add_argument('--recv', help='receive file from TRS80 (default)', action='store_true', default=False)

args = options.parse_args()

# If direction not specified dafault to receive
if (args.send == False and args.recv == False):
	args.recv = True

# Serial stuff
ser = serial.Serial()
ser.port=args.dev
ser.baudrate=args.rate
ser.timeout=0
ser.open()

if (args.recv == True):
	# We poll the serial line to detect a transmission
	print("start the transmission from TELCOM with no width")
	binary_in = ser.read(1)
	contents = ""
	print("Waiting for serial data...")

	# Wait for it to start
	while (len(binary_in) == 0):
		binary_in = ser.read(1)

	# Actual reception loop
	print("Receiving...")
	while (len(binary_in) != 0):
		# Replace all line feeds to new lines
		temp_str = binary_in.decode("ascii").replace("\r", "\n")
		# Remove the TRS-80's EOF
		temp_str = temp_str.replace("\x1A", "")
		contents = contents + temp_str
		time.sleep(0.1)
		binary_in = ser.read(100)

	# Write it to disk
	fid = open(args.fname, 'w')
	fid.write(contents)

	print("done")

elif (args.send == True):
	input("start the reception from TELCOM with no width, press Enter when ready")
	fid = open(args.fname, 'r')
	contents = fid.read()

	# replace all newlines by linefeeds
	contents = contents.replace("\n", "\r")
	# Add the TRS-80's EOF
	contents = contents + "\x1A"
	binary_out = contents.encode('ascii')

	print("Sending...")
	ser.write(binary_out)
	ser.flush()

	print("done")

# Clean up
fid.close()
ser.close()