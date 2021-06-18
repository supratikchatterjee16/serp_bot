import socket
import datetime
global_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def pscan(target, port):
	global global_socket
	try:
		connection = global_socket.connect((target, port))
		connection.close()
		# print('Hit {} {}'.format(target, port))
		return target+', '+ str(port)+ ', 1, N'
	except Exception as e:
		return target+', '+ str(port)+ ', 0, '+str(e)

def network_scan(filename):
	# Use IPv4
	file = open(filename, 'w+')
	file.write('Address(IPv4), Port, Connected, Error\n')
	file.close()
	print('Create CSV with headers')
	file = open(filename, 'a')
	print('Running scans...')
	started = datetime.datetime.now()
	print('Started at {}'.format(started.strftime("%m/%d/%Y, %H:%M:%S")))
	for i in range(0, 256):
		for j in range(0, 256):
			for k in range(0, 256):
				for l in range(0, 256):
					for m in range(0, 1024):
						file.write(pscan(str(i)+'.'+str(j)+'.'+str(k)+'.'+str(l), m)+ '\n')
	file.close()
	ended = datetime.datetime.now()
	print('Finished at {}'.format(ended.strftime("%m/%d/%Y, %H:%M:%S")))
	print('Time transpired is {}'.format((ended-started).strftime("%m/%d/%Y, %H:%M:%S")))
	return True

def run_scans():
	print('Starting')
	scan = network_scan('scan_results.csv')
	if scan:
		print('Succeeded')
	else:
		print('Failed')
	print('Done')

run_scans()
